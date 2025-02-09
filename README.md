# Hand Detection & WebSocket Communication

This project provides a Python-based hand detection system using OpenCV, MediaPipe, and WebSockets. The scripts enable real-time hand tracking and send movement data over a WebSocket connection, making them useful for interactive applications like gesture-controlled interfaces or games.

## Features
- Real-time hand tracking using **MediaPipe Hands**
- Uses **OpenCV** for video capture and display
- Sends movement direction over **WebSockets**
- Supports left and right hand gestures for controlling external applications

## Requirements
Ensure you have the following installed:

```sh
pip install opencv-python mediapipe websockets numpy asyncio
```

## Files
- `hand_tracking_client.py` – Captures video, detects hand position, and sends movement data over WebSocket.
- `websocket_server.py` – A simple WebSocket server to receive movement data.

## Usage
### 1. Run the WebSocket Server
Start the server to listen for incoming movement data:

```sh
python websocket_server.py
```

### 2. Run the Hand Tracking Client
Once the server is running, launch the hand tracking client:

```sh
python hand_tracking_client.py
```

### 3. Interpreting the Output
- The console will print messages like:
  ```
  Hand Detected! Avg X: 320.00 | Movement: left
  📤 Sending: {"direction": "left"}
  ```
- The OpenCV window will display real-time hand movement along with detected gestures.

## How to Use in Your Project
You can import and modify `hand_tracking_client.py` to integrate hand tracking into your own projects:

```python
from hand_tracking_client import send_hand_position

asyncio.run(send_hand_position())
```

Modify the WebSocket server to process hand movement data as needed.

## Troubleshooting
- If the WebSocket server doesn't start, ensure no other processes are using the same port (`8766`).
- If the hand movement isn't detected correctly, adjust the `min_detection_confidence` or `min_tracking_confidence` values in `hand_tracking_client.py`.
- Press `q` to exit the OpenCV window.

## License
This project is open-source and can be freely used in your own applications.

---

### Contributions & Support
Feel free to modify the scripts and adapt them to your needs. If you encounter any issues or improvements, you can submit feedback or contribute to the codebase.
