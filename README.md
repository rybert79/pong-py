# Pong Game 🏓

A simple two-player Pong game built with **Python** and **Pygame**, featuring an optional web-based remote controller for Player 2.

This project is part of my learning journey in Python, object-oriented programming (OOP), game development, and basic networking.

## Features

- Two-player Pong gameplay
- Keyboard controls for both players
- Optional web-based remote controller for Player 2
- Control Player 2 using a smartphone or another device
- HTTP communication over a local network (LAN)
- Ball and paddle collision detection
- Wall collision detection
- Delta-time-based movement
- Automatic winner detection
- Paddle boundary constraints

## Controls

| Player | Controls |
|---|---|
| Player 1 | `W` to move up, `S` to move down |
| Player 2 | `E` to move up, `D` to move down |
| Player 2 (Optional) | Web controller with UP and DOWN buttons |

**Note:** Using the web controller is optional. Player 2 can still be controlled using the keyboard.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pygame | Game rendering and input handling |
| `http.server` | Built-in HTTP server |
| `threading` | Running the HTTP server alongside the game |
| HTML | Web controller structure |
| CSS | Web controller styling |
| JavaScript | Sending HTTP requests using `fetch()` |

No additional Python networking packages are required. The HTTP server and threading modules are included in Python's standard library.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/rybert79/pong-py.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pong-py
   ```

3. Install Pygame-CE:

   ```bash
   pip install pygame-ce
   ```

4. Run the game:

   ```bash
   python3 main.py
   ```

## Using the Optional Web Controller

1. Make sure your computer and smartphone are connected to the same Wi-Fi network.
2. Start the Pong game and its HTTP server.
3. Find your computer's local IP address.
4. Open `controller.html` and update the IP address in its JavaScript:

   ```javascript
   fetch(`http://192.168.1.10:8000/${command}`)
   ```

   Replace `192.168.1.10` with the actual local IP address of the computer running the Pong server. **The IP address must be correct**, otherwise the controller cannot communicate with the game.

5. Open `controller.html` on your smartphone.
6. Use the UP and DOWN buttons to control Player 2.

The web controller is optional. You can skip these steps and play entirely using the keyboard.

**Important:**
- Both devices must be connected to the same Wi-Fi network.
- Make sure the HTTP server is accessible through your local network.
- Allow the connection through your firewall if necessary.
- The computer's local IP address may change when reconnecting to a network.


**Made with Python, Pygame, and a little bit of JavaScript.**

A small project, but a big step in my learning journey! 🚀
