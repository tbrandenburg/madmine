"""
World Generation System - Where Python Code Becomes 3D Worlds!

This is the magic part of MadMine where your Python functions
create block worlds that you can walk around inside.

How it works:
1. You write a Python function that returns block positions
2. This system reads your function and creates 3D blocks
3. You can walk around and explore what your code created!
"""

from ursina import Entity, Vec3, color
from typing import List, Tuple, Callable
import random


class Block:
    """
    A single block in our 3D world.

    Think of this like a LEGO brick that has:
    - A position (where it is in 3D space)
    - A color (what it looks like)
    - A type (what kind of block it is)
    """

    def __init__(self, position: Vec3, block_type: str = "grass", block_color=color.green):
        """
        Create a new block!

        Args:
            position: Where to put the block (x, y, z coordinates)
            block_type: What kind of block (like "grass", "stone", "water")
            block_color: What color the block should be
        """
        self.position = position
        self.block_type = block_type
        self.color = block_color

        # Create the actual 3D object that appears in the game
        self.entity = Entity(
            model='cube',           # Make it look like a cube
            position=position,      # Put it at the right spot
            color=block_color,      # Give it the right color
            scale=(1, 1, 1)        # Make it normal size (1x1x1)
        )


class WorldGenerator:
    """
    This class turns your Python code into 3D worlds!

    It takes functions that you write and uses them to decide
    where to place blocks in the 3D world.
    """

    def __init__(self):
        """Set up the world generator."""
        self.blocks: List[Block] = []  # List to store all our blocks
        self.world_size = 16          # How big our world is (16x16 blocks)

    def generate_world(self, generator_function: Callable = None) -> List[Block]:
        """
        Generate a 3D world using your Python function!

        Args:
            generator_function: A Python function that decides where blocks go
                               If None, we'll make a simple random world

        Returns:
            List of all the blocks we created
        """
        # Clear any existing blocks
        self.clear_world()

        # Use the function you provided, or make a simple random world
        if generator_function is None:
            generator_function = self.simple_random_world

        # Generate blocks using your function
        block_positions = generator_function()

        # Create actual 3D blocks from the positions
        for pos_data in block_positions:
            if isinstance(pos_data, tuple) and len(pos_data) == 3:
                # Simple position: (x, y, z)
                position = Vec3(*pos_data)
                block = Block(position)
            elif isinstance(pos_data, dict):
                # Detailed block: {"position": (x,y,z), "color": color.red, "type": "stone"}
                position = Vec3(*pos_data["position"])
                block_color = pos_data.get("color", color.green)
                block_type = pos_data.get("type", "grass")
                block = Block(position, block_type, block_color)
            else:
                continue  # Skip invalid data

            self.blocks.append(block)

        print(f"🌍 Created world with {len(self.blocks)} blocks!")
        return self.blocks

    def clear_world(self):
        """Remove all blocks from the world."""
        for block in self.blocks:
            if block.entity:
                block.entity.removeNode()  # Remove from 3D scene
        self.blocks.clear()
        print("🧹 World cleared!")

    def simple_random_world(self) -> List[Tuple[int, int, int]]:
        """
        A simple example world generator function.

        This creates a flat ground with some random blocks on top.
        You can write your own functions like this!

        Returns:
            List of (x, y, z) positions where blocks should be placed
        """
        blocks = []

        # Create a flat ground layer
        for x in range(self.world_size):
            for z in range(self.world_size):
                blocks.append((x, 0, z))  # Ground level at y=0

        # Add some random blocks on top
        for _ in range(20):  # Create 20 random blocks
            x = random.randint(0, self.world_size - 1)
            z = random.randint(0, self.world_size - 1)
            y = random.randint(1, 3)  # Stack them 1-3 blocks high
            blocks.append((x, y, z))

        return blocks

    def get_block_count(self) -> int:
        """Get the total number of blocks in the world."""
        return len(self.blocks)

    def get_world_info(self) -> dict:
        """Get information about the current world."""
        return {
            "total_blocks": len(self.blocks),
            "world_size": self.world_size,
            "block_types": list(set(block.block_type for block in self.blocks))
        }


# Example generator functions that kids can use as templates!

def flat_world() -> List[Tuple[int, int, int]]:
    """Create a simple flat world - perfect for beginners!"""
    blocks = []
    for x in range(10):
        for z in range(10):
            blocks.append((x, 0, z))
    return blocks


def pyramid_world() -> List[dict]:
    """Create a pyramid - shows how to use colors and types!"""
    blocks = []

    # Build a pyramid layer by layer
    for y in range(5):  # 5 layers tall
        size = 5 - y    # Each layer gets smaller
        for x in range(size):
            for z in range(size):
                blocks.append({
                    "position": (x + y, y, z + y),
                    "color": [color.red, color.blue, color.green, color.yellow, color.orange][y],
                    "type": f"pyramid_layer_{y}"
                })

    return blocks


def checkerboard_world() -> List[dict]:
    """Create a checkerboard pattern - great for learning patterns!"""
    blocks = []

    for x in range(8):
        for z in range(8):
            # Checkerboard pattern: alternate colors
            if (x + z) % 2 == 0:
                block_color = color.white
            else:
                block_color = color.black

            blocks.append({
                "position": (x, 0, z),
                "color": block_color,
                "type": "checkerboard"
            })

    return blocks