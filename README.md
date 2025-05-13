# Asteroids Game

A classic Asteroids arcade game implementation using Python and Pygame.

## Description

This is a modern implementation of the classic Asteroids arcade game. Players control a spaceship and must destroy asteroids while avoiding collisions. The game features:

- Player-controlled spaceship with movement and shooting mechanics
- Procedurally generated asteroid field
- Collision detection between ship, asteroids, and shots
- Score tracking
- Smooth gameplay with 60 FPS

## Requirements

- Python 3.x
- Pygame 2.6.1

## Installation

1. Clone this repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. Controls:
   - WASD keys to move the spaceship
   - Space bar to shoot
   - ESC or close window to quit

## Game Features

- The player's spaceship can rotate and move in any direction
- Asteroids split into smaller pieces when shot
- Collision with asteroids results in game over
- Smooth physics-based movement
- Classic arcade-style gameplay

## Project Structure

- `main.py` - Main game loop and initialization
- `player.py` - Player spaceship implementation
- `asteroid.py` - Asteroid class and behavior
- `asteroidfield.py` - Asteroid field generation and management
- `shot.py` - Projectile implementation
- `circleshape.py` - Utility class for circular shapes
- `constants.py` - Game constants and configuration

## License

This project is open source and available for personal and educational use. 
