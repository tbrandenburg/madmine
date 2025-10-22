"""
Player Controller System - Making Movement Fun and Simple!

This handles how the player moves around the 3D world.
We use Ursina's FirstPersonController to make it easy.

Controls:
- WASD: Move around
- Mouse: Look around
- Space: Jump
- Shift: Run faster
"""

from ursina import Entity, Vec3, time, held_keys, mouse, camera
from ursina.prefabs.first_person_controller import FirstPersonController


class Player:
    """
    The player character that moves around the 3D world.

    This class wraps Ursina's FirstPersonController to make it
    easier to understand and customize for educational purposes.
    """

    def __init__(self, start_position: Vec3 = Vec3(0, 2, 0)):
        """
        Create a new player!

        Args:
            start_position: Where the player starts in the world (x, y, z)
        """
        self.start_position = start_position

        # Create the first-person controller
        # This gives us WASD movement and mouse look automatically!
        self.controller = FirstPersonController(
            model='cube',                    # What the player looks like (cube for now)
            position=start_position,         # Where to start
            scale=(1, 2, 1),                # Make it person-sized (1 wide, 2 tall, 1 deep)
            speed=5,                         # How fast the player moves
            mouse_sensitivity=Vec3(50, 50),  # How fast the camera turns
            gravity=1,                       # Enable gravity so player falls onto blocks
            jump_height=2                    # How high the player can jump
        )

        # Make the player model invisible since we're in first-person
        self.controller.visible = False

        # Store movement settings
        self.normal_speed = 5
        self.run_speed = 8
        self.jump_height = 3

        print(f"🏃‍♂️ Player created at position {start_position}")

    def update(self):
        """
        Update player movement every frame.

        This gets called many times per second to handle movement.
        """
        # Handle running (hold Shift to run faster)
        # Check if held_keys exists to avoid NoneType errors
        try:
            if held_keys and (held_keys.get('left shift') or held_keys.get('right shift')):
                self.controller.speed = self.run_speed
            else:
                self.controller.speed = self.normal_speed
        except (AttributeError, KeyError):
            # If held_keys isn't available yet, use normal speed
            self.controller.speed = self.normal_speed

        # The FirstPersonController handles most movement automatically,
        # but we can add custom behaviors here if needed!

    def get_position(self) -> Vec3:
        """Get the player's current position in the world."""
        return self.controller.position

    def set_position(self, new_position: Vec3):
        """Move the player to a new position."""
        self.controller.position = new_position
        print(f"🚀 Player moved to {new_position}")

    def reset_position(self):
        """Move the player back to the starting position."""
        self.set_position(self.start_position)

    def get_looking_direction(self) -> Vec3:
        """Get the direction the player is looking."""
        return camera.forward

    def is_moving(self) -> bool:
        """Check if the player is currently moving."""
        try:
            if not held_keys:
                return False
            return any([
                held_keys.get('w', False), held_keys.get('s', False),     # Forward/backward
                held_keys.get('a', False), held_keys.get('d', False),     # Left/right
            ])
        except (AttributeError, KeyError):
            return False

    def is_running(self) -> bool:
        """Check if the player is running (holding Shift)."""
        try:
            if not held_keys:
                return False
            return held_keys.get('left shift', False) or held_keys.get('right shift', False)
        except (AttributeError, KeyError):
            return False

    def get_movement_info(self) -> dict:
        """Get information about the player's current movement state."""
        try:
            return {
                "position": self.get_position(),
                "is_moving": self.is_moving(),
                "is_running": self.is_running(),
                "speed": getattr(self.controller, 'speed', self.normal_speed),
                "looking_direction": self.get_looking_direction()
            }
        except Exception as e:
            # Return safe defaults if something goes wrong
            print(f"⚠️ Player info error: {e}")
            return {
                "position": Vec3(0, 0, 0),
                "is_moving": False,
                "is_running": False,
                "speed": self.normal_speed,
                "looking_direction": Vec3(0, 0, 1)
            }


class CameraController:
    """
    Simple camera controller for different view modes.

    This is separate from the Player class so we can easily
    switch between first-person and other camera modes.
    """

    def __init__(self):
        """Set up the camera controller."""
        self.camera_mode = "first_person"  # Default mode

    def set_first_person_mode(self):
        """Switch to first-person camera (through the player's eyes)."""
        self.camera_mode = "first_person"
        # The FirstPersonController handles this automatically
        print("📹 Switched to first-person camera")

    def set_follow_mode(self, player: Player, distance: float = 5):
        """
        Switch to follow camera (behind the player).

        Args:
            player: The player to follow
            distance: How far behind the player to stay
        """
        self.camera_mode = "follow"
        # This would need more implementation for a full follow camera
        print(f"📹 Switched to follow camera (distance: {distance})")

    def get_camera_info(self) -> dict:
        """Get information about the current camera state."""
        return {
            "mode": self.camera_mode,
            "position": camera.position,
            "rotation": camera.rotation
        }