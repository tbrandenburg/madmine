"""
Debug Test - Find the exact error in MadMine

This script tries to isolate where the NoneType error is happening.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

print("🔍 Starting MadMine debug test...")

try:
    print("1. Testing Ursina import...")
    from ursina import *
    print("   ✅ Ursina imported successfully")

    print("2. Testing Ursina app creation...")
    app = Ursina()
    print("   ✅ Ursina app created successfully")

    print("3. Testing world generator import...")
    from world.world_generator import WorldGenerator
    print("   ✅ World generator imported successfully")

    print("4. Testing world generator creation...")
    world_gen = WorldGenerator()
    print("   ✅ World generator created successfully")

    print("5. Testing player controller import...")
    from game.player_controller import Player
    print("   ✅ Player controller imported successfully")

    print("6. Testing player creation...")
    player = Player(start_position=Vec3(0, 2, 0))
    print("   ✅ Player created successfully")

    print("7. Testing UI import...")
    from ui.game_ui import GameUI
    print("   ✅ UI imported successfully")

    print("8. Testing UI creation...")
    ui = GameUI()
    print("   ✅ UI created successfully")

    print("9. Testing world generation...")
    world_gen.generate_world()
    print("   ✅ World generated successfully")

    print("10. Testing player movement info...")
    player_info = player.get_movement_info()
    print(f"   ✅ Player info: {player_info}")

    print("11. Testing UI updates...")
    ui.update_player_info(
        player_info["position"],
        player_info["is_moving"],
        player_info["is_running"]
    )
    print("   ✅ UI update successful")

    print("\n🎉 All tests passed! The error must be in the game loop setup.")
    print("💡 Try running the game again - it might work now with the fixes!")

    # Don't start the actual game loop in debug mode
    app.quit()

except Exception as e:
    print(f"\n❌ Error found at step: {e}")
    print(f"Error type: {type(e).__name__}")
    import traceback
    print(f"Full traceback:\n{traceback.format_exc()}")

    print("\n🔧 This helps us identify exactly where the problem is!")