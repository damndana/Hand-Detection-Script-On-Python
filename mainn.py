import cv2
import numpy as np
import mediapipe as mp
import websockets
import asyncio
import json
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

async def send_hand_position():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    try:
        async with websockets.connect("ws://localhost:your host") as websocket:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Failed to grab frame.")
                    break

                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = hands.process(rgb_frame)

                height, width, _ = frame.shape
                movement = "none"

                if result.multi_hand_landmarks:
                    for hand_landmarks in result.multi_hand_landmarks:
                        x_coords = [lm.x * width for lm in hand_landmarks.landmark]
                        avg_x = np.mean(x_coords)


                        if avg_x < width * 0.4:
                            movement = "left"
                        elif avg_x > width * 0.6:
                            movement = "right"


                        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    print(f"Hand Detected! Avg X: {avg_x:.2f} | Movement: {movement}")


                data_to_send = json.dumps({"direction": movement})
                try:
                    await websocket.send(data_to_send)
                except websockets.exceptions.ConnectionClosed as e:
                    print(f"WebSocket Connection Closed: {e}")
                    break


                cv2.putText(frame, f"Move: {movement}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Hand Control", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        asyncio.run(send_hand_position())
    except KeyboardInterrupt:
        print("\nProcess terminated by user.")