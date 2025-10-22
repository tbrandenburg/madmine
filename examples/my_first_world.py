"""
My First World - An Example for Learning!

This is where you can experiment with creating your own worlds!
Try changing the numbers and see what happens.

To use this:
1. Edit the function below
2. Save the file
3. In MadMine, press R to reload and see your changes!
"""

from ursina import color


def my_awesome_world():
    """
    Create your own awesome world!

    This function should return a list of block positions.
    Each position is a tuple with (x, y, z) coordinates.
    """

    blocks = []  # This will store all our block positions

    # Let's make a simple house!

    # Floor (5x5 squares at ground level)
    for x in range(5):
        for z in range(5):
            blocks.append((x, 0, z))  # y=0 is ground level

    # Walls (only the edges, so we can walk inside!)
    for x in range(5):
        # Front and back walls
        blocks.append((x, 1, 0))    # Front wall
        blocks.append((x, 1, 4))    # Back wall

    for z in range(1, 4):  # Skip corners (already done above)
        # Left and right walls
        blocks.append((0, 1, z))    # Left wall
        blocks.append((4, 1, z))    # Right wall

    # Add a simple roof
    for x in range(5):
        for z in range(5):
            blocks.append((x, 2, z))

    return blocks


def colorful_tower():
    """
    Create a colorful tower with different colored blocks!

    This shows how to use colors and make more complex shapes.
    """

    blocks = []

    # Create a tower that gets smaller as it goes up
    for y in range(8):  # 8 blocks tall
        size = 5 - y // 2  # Get smaller every 2 levels

        # Pick a color based on the height
        if y == 0:
            block_color = color.red
        elif y < 3:
            block_color = color.orange
        elif y < 5:
            block_color = color.yellow
        else:
            block_color = color.blue

        # Create a square platform at this height
        for x in range(size):
            for z in range(size):
                blocks.append({
                    "position": (x, y, z),
                    "color": block_color,
                    "type": f"tower_level_{y}"
                })

    return blocks


def maze_world():
    """
    Create a simple maze to explore!

    This shows how to make more complex patterns using loops.
    """

    blocks = []

    # Create the maze walls using a pattern
    maze_size = 11  # Must be odd number for the pattern to work

    for x in range(maze_size):
        for z in range(maze_size):
            # Create walls in a pattern
            if x % 2 == 0 or z % 2 == 0:
                blocks.append((x, 0, z))  # Ground
                blocks.append((x, 1, z))  # Wall

    # Add some gaps to make it a real maze
    # (Try adding your own gaps!)
    gaps = [
        (2, 1, 1), (4, 1, 3), (6, 1, 5),  # Remove some wall blocks
        (1, 1, 2), (3, 1, 4), (5, 1, 6)   # Remove more wall blocks
    ]

    # Remove the gap blocks from our wall list
    for gap in gaps:
        if gap in [(x, y, z) for x, y, z in blocks]:
            blocks.remove(gap)

    return blocks


# Try experimenting with these ideas:

def rainbow_path():
    """Can you create a rainbow-colored path?"""
    # Hint: Use a loop and different colors for each position!
    pass


def mountain():
    """Can you create a mountain shape?"""
    # Hint: Start with a big base and make each layer smaller and higher!
    pass


def spiral():
    """Can you create a spiral staircase?"""
    # Hint: As you go up (increase y), also change x and z in a circular pattern!
    pass


# Add your own functions here!
# Remember: they should return a list of positions like (x, y, z)
# or dictionaries with position, color, and type!