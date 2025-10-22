"""
MadMine - Main Game File

This is the heart of MadMine! It brings together all the pieces:
- World generation (turning your Python code into 3D worlds)
- Player movement (WASD controls and camera)
- User interface (showing information on screen)

To run MadMine:
1. Make sure you have Python installed
2. Run: python main.py
3. Use WASD to move, mouse to look around
4. Press H for help, R to reload the world

This is where the magic happens! 🎮✨
"""

from ursina import *
import time as python_time
import sys
import os

# Add our src directory to the Python path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import our custom modules
from world.world_generator import WorldGenerator, flat_world, pyramid_world, checkerboard_world
from game.player_controller import Player, CameraController
from ui.game_ui import GameUI, WorldGeneratorUI


class MadMineGame:
    """
    The main MadMine game class.

    This coordinates all the different parts of the game:
    - Creates the 3D world
    - Handles player movement
    - Updates the user interface
    - Manages the game loop
    """

    def __init__(self):
        """Initialize MadMine game."""
        print("🎮 Starting MadMine...")

        # Initialize Ursina (the 3D engine)
        self.app = Ursina()

        # Set up the game window
        window.title = 'MadMine - Python 3D World Sandbox'
        window.borderless = False
        window.fullscreen = False
        window.fps_counter.enabled = False  # We'll make our own FPS counter

        # Initialize game systems
        self.world_generator = WorldGenerator()
        self.player = Player(start_position=Vec3(8, 5, 8))  # Start in middle of world, up high
        self.camera_controller = CameraController()
        self.game_ui = GameUI()
        self.world_ui = WorldGeneratorUI()

        # Game state
        self.current_world = "random"
        self.last_fps_update = 0
        self.frame_count = 0
        self.current_fps = 0

        # Set up the environment
        self.setup_environment()

        # Generate the initial world
        self.reload_world()

        print("🚀 MadMine ready! Press H for help.")

    def setup_environment(self):
        """Set up the basic 3D environment."""

        # Add a sky so the world looks nice
        Sky()

        # Add some basic lighting
        DirectionalLight().look_at(Vec3(1, -1, -1))

        # Set a nice background color
        camera.fov = 90  # Field of view (how much you can see)

    def reload_world(self, generator_name: str = None):
        """
        Reload the world with a new generator.

        Args:
            generator_name: Which world generator to use
        """
        print(f"🔄 Reloading world...")

        # Choose which world generator to use
        if generator_name == "flat":
            generator_function = flat_world
            world_name = "Flat World"
        elif generator_name == "pyramid":
            generator_function = pyramid_world
            world_name = "Pyramid World"
        elif generator_name == "checkerboard":
            generator_function = checkerboard_world
            world_name = "Checkerboard World"
        else:
            generator_function = None  # Use default random world
            world_name = "Random World"

        # Generate the new world
        self.world_generator.generate_world(generator_function)

        # Update UI
        self.game_ui.update_main_title(world_name)
        self.game_ui.show_message(f"🌍 {world_name} loaded!")

        # Hide welcome message after first world load
        self.game_ui.hide_welcome_message()

        self.current_world = generator_name or "random"

    def update(self):
        """
        Main game update loop.

        This function gets called many times per second by Ursina.
        It updates all the game systems and keeps everything running smoothly.
        """

        # Update player movement
        self.player.update()

        # Update UI with current player info
        player_info = self.player.get_movement_info()
        self.game_ui.update_player_info(
            player_info["position"],
            player_info["is_moving"],
            player_info["is_running"]
        )

        # Update world info
        world_info = self.world_generator.get_world_info()
        self.game_ui.update_world_info(world_info)

        # Update FPS counter (every second)
        current_time = python_time.time()
        self.frame_count += 1

        if current_time - self.last_fps_update >= 1.0:  # Update every second
            self.current_fps = self.frame_count / (current_time - self.last_fps_update)
            self.game_ui.update_fps(self.current_fps)
            self.frame_count = 0
            self.last_fps_update = current_time

    def input(self, key):
        """
        Handle keyboard input.

        This function gets called whenever a key is pressed.
        It handles things like help, world reloading, and other commands.

        Args:
            key: The key that was pressed
        """

        # Toggle help display
        if key == 'h':
            self.game_ui.toggle_help()

        # Reload current world
        elif key == 'r':
            self.reload_world(self.current_world)

        # Number keys for different world types
        elif key == '1':
            self.reload_world("flat")
        elif key == '2':
            self.reload_world("pyramid")
        elif key == '3':
            self.reload_world("checkerboard")
        elif key == '4':
            self.reload_world("random")

        # Toggle world generator menu
        elif key == 'g':
            self.world_ui.toggle_menu()

        # Quit game
        elif key == 'escape':
            self.quit_game()

    def quit_game(self):
        """Safely quit the game."""
        print("👋 Thanks for playing MadMine!")
        self.app.quit()

    def run(self):
        """Start the game loop."""
        print("🎮 Game loop starting...")

        # Set up Ursina's update and input functions to use our methods
        def ursina_update():
            self.update()

        def ursina_input(key):
            self.input(key)

        # Tell Ursina to use our functions
        import builtins
        builtins.update = ursina_update
        builtins.input = ursina_input

        # Start the game!
        self.app.run()


def main():
    """
    Main function - this is where MadMine starts!
    """
    try:
        # Create and run the game
        game = MadMineGame()
        game.run()

    except KeyboardInterrupt:
        print("\n👋 Game interrupted by user")
    except Exception as e:
        print(f"❌ Error running MadMine: {e}")
        print("Make sure you have all the required packages installed!")
        print("Try running: uv sync")


if __name__ == "__main__":
    main()
