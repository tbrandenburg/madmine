"""
Test Setup - Check if MadMine is ready to run!

This script tests if all the pieces are working without opening a 3D window.
It's perfect for checking if everything is set up correctly.
"""

import sys
import os

# Add our src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

print("🧪 Testing MadMine setup...")

# Test 1: Can we import Ursina?
try:
    from ursina import Vec3, color, Entity
    print("✅ Ursina imported successfully!")
except ImportError as e:
    print(f"❌ Ursina import failed: {e}")
    exit(1)

# Test 2: Can we import our world generator?
try:
    from world.world_generator import WorldGenerator, flat_world, pyramid_world
    print("✅ World generator imported successfully!")
except ImportError as e:
    print(f"❌ World generator import failed: {e}")
    exit(1)

# Test 3: Can we create a world generator?
try:
    world_gen = WorldGenerator()
    print("✅ WorldGenerator created successfully!")
except Exception as e:
    print(f"❌ WorldGenerator creation failed: {e}")
    exit(1)

# Test 4: Can we generate a simple world (without 3D display)?
try:
    blocks = flat_world()
    print(f"✅ Generated flat world with {len(blocks)} blocks!")

    blocks = pyramid_world()
    print(f"✅ Generated pyramid world with {len(blocks)} blocks!")
except Exception as e:
    print(f"❌ World generation failed: {e}")
    exit(1)

# Test 5: Can we import our player controller?
try:
    from game.player_controller import Player, CameraController
    print("✅ Player controller imported successfully!")
except ImportError as e:
    print(f"❌ Player controller import failed: {e}")
    exit(1)

# Test 6: Can we import our UI system?
try:
    from ui.game_ui import GameUI, WorldGeneratorUI
    print("✅ UI system imported successfully!")
except ImportError as e:
    print(f"❌ UI system import failed: {e}")
    exit(1)

print("\n🎉 ALL TESTS PASSED! 🎉")
print("\nMadMine is ready to run!")
print("\nNext steps:")
print("1. Run: uv run python main.py")
print("2. Use WASD to move around")
print("3. Press H for help")
print("4. Press 1, 2, 3, 4 to try different worlds")
print("\nNote: If you get display errors, that's normal in some environments.")
print("The core functionality is working perfectly! 🚀")