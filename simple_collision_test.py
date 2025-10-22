"""
Simple Collision Test - Minimal test to understand the issue
"""

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Create the app
app = Ursina()

# Create a simple floor at y=0
ground = Entity(
    model='cube',
    position=(0, 0, 0),
    color=color.green,
    scale=(10, 1, 10),  # Large flat platform
    collider='box'
)

# Create player high above the ground
player = FirstPersonController()
player.position = (0, 5, 0)  # Start 5 units above ground

print(f"Initial player position: {player.position}")
print(f"Ground position: {ground.position}")
print(f"Ground has collider: {ground.collider is not None}")

# Simple update to track position
def update():
    # Print position every second
    if int(time.time()) % 1 == 0 and time.dt < 0.02:  # Approximately once per second
        print(f"Player position: {player.position:.2f}")

print("🧪 Starting simple collision test...")
print("Player should fall from y=5 to y=1 (on top of green platform)")
print("Use WASD to move around once you land")

app.run()