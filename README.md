# Pong Game

This is a simple implementation of the classic Pong game using Python's turtle module.

## Description

The game includes two paddles and a ball. The paddles can be moved up and down to hit the ball. The ball increases its speed with each paddle hit. The game keeps score and updates it whenever a player misses the ball.

## Files

- `main.py`: This is the main file to run the Pong game.
- `ball.py`: This file contains the Ball class which is responsible for the movement and collision of the ball.
- `paddle.py`: This file contains the Paddle class which is responsible for creating and moving the paddles.
- `scoreboard.py`: This file contains the Score class which is responsible for keeping and updating the score.

## How to Run

1. Ensure that Python 3.x is installed on your machine.
2. Clone this repository to your local machine.
3. Navigate to the cloned repository.
4. Run the command `python main.py` in your terminal.

Enjoy the game!

## Controls

- Left paddle:
    - 'w' to move up
    - 's' to move down
- Right paddle:
    - 'Up arrow' to move up
    - 'Down arrow' to move down

Notes
-The game loop runs continuously until manually closed.
-Adjustments to the game speed and paddle dimensions can be made in the respective classes.
-Feel free to customize and enhance the game as desired!
