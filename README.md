# Keystroke Overlay for OBS

This repository contains a Python script that creates a graphical overlay of certain keystrokes. The overlay can be captured in OBS (Open Broadcaster Software) as a window capture, providing a visual representation of key presses in real-time. This is particularly useful for live streaming or recording where viewers may benefit from seeing the keys being pressed.

## How it Works

The script uses the `tkinter` and `pygame` libraries to create a window with labeled boxes representing the keys 'A', 'S', 'D', 'W', 'F', and 'Y'. When one of these keys is pressed, its corresponding box lights up in the window. The script also listens for input from a game controller, if one is connected, and displays the movement of the joystick on a separate part of the window.

## Usage

1. Ensure you have Python installed on your machine. The script requires Python 3.6 or later.

2. Install the required libraries by running `pip install tkinter pygame`.

3. Run the script using `python keystroke_overlay.py`. This will open a new window with the key overlay.

4. In OBS, add a new Window Capture source and select the window titled "Key Light Up".

5. Position and scale the window capture source as desired in your OBS scene.

Please note that the script stops listening to 'A', 'S', 'D', 'W', 'F', and 'Y' when a game controller is connected.

## Customization

You can customize the script to suit your needs. For example, you can change the keys that are listened for, the colors of the boxes, or the layout of the window. To do this, you will need to modify the script. If you're not familiar with Python, you may need to spend some time learning the basics before you can effectively customize the script.

## Contributing

Contributions are welcome! If you have a feature request, bug report, or want to contribute to the code, please open an issue or pull request.
