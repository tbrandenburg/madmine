"""
Game UI System - Simple and Kid-Friendly Interface

This handles all the text and buttons you see on screen.
We keep it simple so kids can focus on the world-building code!

UI Elements:
- Info display (showing position, block count, etc.)
- Help text (showing controls)
- World generator selector
"""

from ursina import Text, Button, Entity, color, camera, window, Vec3
from typing import Dict, Any


class GameUI:
    """
    The main user interface for MadMine.

    This shows information on screen and handles simple menus.
    Everything is designed to be readable and not distracting.
    """

    def __init__(self):
        """Set up the game's user interface."""
        self.ui_elements = {}
        self.is_help_visible = False
        self.setup_ui()

    def setup_ui(self):
        """Create all the UI elements."""

        # Info panel (top-left corner)
        self.ui_elements['info_panel'] = Text(
            text="MadMine - Loading...",
            position=(-0.8, 0.45),        # Top-left
            scale=1.5,                    # Make it readable
            color=color.white,
            background=True               # Dark background for readability
        )

        # Position display
        self.ui_elements['position_text'] = Text(
            text="Position: (0, 0, 0)",
            position=(-0.8, 0.35),
            scale=1.2,
            color=color.cyan,
            background=True
        )

        # World info display
        self.ui_elements['world_info'] = Text(
            text="Blocks: 0",
            position=(-0.8, 0.25),
            scale=1.2,
            color=color.yellow,
            background=True
        )

        # Controls help (bottom-left, initially hidden)
        self.ui_elements['help_text'] = Text(
            text="Controls:\nWASD - Move\nMouse - Look\nSpace - Jump\nShift - Run\nH - Toggle Help\nR - Reload World",
            position=(-0.8, -0.4),
            scale=1.0,
            color=color.white,
            background=True,
            visible=False  # Start hidden
        )

        # Welcome message (center, fades after a few seconds)
        self.ui_elements['welcome'] = Text(
            text="🌍 Welcome to MadMine! 🌍\nPress H for help",
            position=(0, 0.1),
            scale=2.0,
            color=color.green,
            background=True,
            origin=(0, 0)  # Center the text
        )

        # FPS counter (top-right, small)
        self.ui_elements['fps'] = Text(
            text="FPS: --",
            position=(0.7, 0.45),
            scale=1.0,
            color=color.gray,
            background=True
        )

        print("🖥️ UI system initialized")

    def update_player_info(self, player_pos: Vec3, is_moving: bool, is_running: bool):
        """
        Update the player information display.

        Args:
            player_pos: Current player position
            is_moving: Whether the player is moving
            is_running: Whether the player is running
        """
        # Format position nicely (round to 1 decimal place)
        pos_text = f"Position: ({player_pos.x:.1f}, {player_pos.y:.1f}, {player_pos.z:.1f})"

        # Add movement indicators
        if is_running:
            pos_text += " 🏃‍♂️"  # Running emoji
        elif is_moving:
            pos_text += " 🚶‍♂️"  # Walking emoji

        self.ui_elements['position_text'].text = pos_text

    def update_world_info(self, world_data: Dict[str, Any]):
        """
        Update the world information display.

        Args:
            world_data: Dictionary with world information (block count, etc.)
        """
        block_count = world_data.get('total_blocks', 0)
        world_size = world_data.get('world_size', 0)

        world_text = f"Blocks: {block_count} | Size: {world_size}x{world_size}"
        self.ui_elements['world_info'].text = world_text

    def update_fps(self, fps: float):
        """
        Update the FPS counter.

        Args:
            fps: Current frames per second
        """
        self.ui_elements['fps'].text = f"FPS: {fps:.0f}"

    def toggle_help(self):
        """Show or hide the help text."""
        self.is_help_visible = not self.is_help_visible
        self.ui_elements['help_text'].visible = self.is_help_visible

        if self.is_help_visible:
            print("📖 Help displayed")
        else:
            print("📖 Help hidden")

    def show_message(self, message: str, duration: float = 3.0, message_color=color.white):
        """
        Show a temporary message in the center of the screen.

        Args:
            message: Text to display
            duration: How long to show it (seconds)
            message_color: What color the text should be
        """
        # Create temporary message
        temp_message = Text(
            text=message,
            position=(0, 0),
            scale=2.0,
            color=message_color,
            background=True,
            origin=(0, 0)
        )

        # Remove it after the specified duration
        # (In a real implementation, you'd use a timer system)
        print(f"💬 Message: {message}")

    def hide_welcome_message(self):
        """Hide the welcome message."""
        if 'welcome' in self.ui_elements:
            self.ui_elements['welcome'].visible = False

    def update_main_title(self, world_name: str = "MadMine"):
        """
        Update the main title text.

        Args:
            world_name: Name of the current world
        """
        self.ui_elements['info_panel'].text = f"🎮 {world_name}"

    def get_ui_info(self) -> Dict[str, Any]:
        """Get information about the current UI state."""
        return {
            "help_visible": self.is_help_visible,
            "elements_count": len(self.ui_elements),
            "welcome_visible": self.ui_elements['welcome'].visible
        }


class WorldGeneratorUI:
    """
    Simple UI for selecting different world generators.

    This lets kids easily switch between different world types
    without having to edit code files.
    """

    def __init__(self):
        """Set up the world generator selection UI."""
        self.generator_buttons = []
        self.is_visible = False
        self.setup_generator_menu()

    def setup_generator_menu(self):
        """Create buttons for different world generators."""

        # This would create buttons for different world types
        # For now, we'll just print available options
        self.available_generators = [
            "Random World",
            "Flat World",
            "Pyramid World",
            "Checkerboard World"
        ]

        print(f"🎛️ World Generator UI ready with {len(self.available_generators)} options")

    def toggle_menu(self):
        """Show or hide the world generator menu."""
        self.is_visible = not self.is_visible

        if self.is_visible:
            print("🎛️ Generator menu opened")
            print("Available worlds:")
            for i, generator in enumerate(self.available_generators):
                print(f"  {i+1}. {generator}")
        else:
            print("🎛️ Generator menu closed")

    def select_generator(self, index: int) -> str:
        """
        Select a world generator by index.

        Args:
            index: Index of the generator to select (0-based)

        Returns:
            Name of the selected generator
        """
        if 0 <= index < len(self.available_generators):
            selected = self.available_generators[index]
            print(f"🌍 Selected: {selected}")
            return selected
        else:
            print(f"❌ Invalid generator index: {index}")
            return "Random World"  # Default fallback