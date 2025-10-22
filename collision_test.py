"""
Collision Test - Simple test to verify collision detection works
"""

from ursina import *

# Create the app
app = Ursina()

# Create some test blocks
for x in range(5):
    for z in range(5):
        Entity(
            model='cube',
            position=(x, 0, z),
            color=color.green,
            collider='box'  # Important: collision detection
        )

# Create player with explicit collision settings
player = FirstPersonController()
print(f"Player created at: {player.position}")
print(f"Player has gravity: {hasattr(player, 'gravity')}")
print(f"Player attributes: {[attr for attr in dir(player) if not attr.startswith('_')]}")

# Add some debug info
def update():
    if held_keys['space']:
        print(f"Space pressed - Player pos: {player.position}")

# Run the test
if __name__ == "__main__":
    print("🧪 Collision test starting...")
    print("Use WASD to move, mouse to look, Space to jump")
    print("Player should land on green blocks at y=1 (on top of blocks)")
    app.run()