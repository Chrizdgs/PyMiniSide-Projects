"""
You're given a 7x7 grid representing an area covered in Holi powders. Each cell contains an emoji representing one of these colors:

["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]

Some colors may be missing from the grid. Can you find which ones are missing? 🤫

Complete the function that finds and returns all the colors missing from the area (in that order).

Example 1

Input:

  [["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟥"],
  ["🟨", "🟩", "🟦", "🟪", "🟥", "🟧", "🟨"],
  ["🟦", "🟥", "🟧", "🟨", "🟩", "🟪", "🟦"],
  ["🟩", "🟦", "🟪", "🟥", "🟧", "🟨", "🟩"],
  ["🟧", "🟨", "🟩", "🟦", "🟪", "🟥", "🟧"],
  ["🟪", "🟧", "🟨", "🟩", "🟦", "🟥", "🟪"],
  ["🟥", "🟦", "🟩", "🟪", "🟨", "🟧", "🟦"]]
Output: "[🟫"]
The brown emoji is missing from the 7x7.
"""

def find_missing_colors(grid):
    all_colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
    
    found_colors = set()
    
    # Traverse the 2D grid
    for row in grid:
        for cell in row:
            found_colors.add(cell)
    
    # Find missing colors while preserving order
    missing = []
    for color in all_colors:
        if color not in found_colors:
            missing.append(color)
    
    return missing