"""
Debug version of main.py to track what's happening with player movement
"""

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time as python_time

# Simple debug app
app = Ursina()

# Create a simple flat world like in collision test
print("Creating debug world...")
blocks = []
for x in range(10):
    for z in range(10):
        block = Entity(
            model='cube',
            position=(x, 0, z),
            color=color.green,
            collider='box'
        )
        blocks.append(block)

print(f"Created {len(blocks)} blocks")

# Create player exactly like in collision test
player = FirstPersonController()
player.position = Vec3(5, 2, 5)  # Middle of 10x10 world, 2 units high

print(f"Player starting position: {player.position}")
print(f"Player has collider: {hasattr(player, 'collider')}")
print(f"Example block position: {blocks[0].position}")
print(f"Example block has collider: {blocks[0].collider is not None}")

# Debug update function
def update():
    # Print player position every frame for first few seconds
    if app.time < 5:  # First 5 seconds
        if int(app.time * 2) % 2 == 0:  # Twice per second
            print(f"Time: {app.time:.1f}s - Player pos: {player.position}")

print("🔍 Debug mode - watch player position for first 5 seconds")
print("Player should fall from y=2 to y=1 and stay there")
print("Use WASD to move around")

app.run()