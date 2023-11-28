#!/usr/bin/python3
"""Island Perimeter."""


def island_perimeter(grid: list) -> int:
    """Return the perimeter of the grid."""
    if len(grid) == 0 or [] in grid:
        return -1

    perimeter: int = 0
    for r_idx, row in enumerate(grid):
        for c_idx, col in enumerate(row):
            if col == 1:
                if c_idx in (0, len(row) - 1):
                    perimeter += 1
                else:
                    if row[c_idx - 1] == 0:
                        perimeter += 1
                    if row[c_idx + 1] == 0:
                        perimeter += 1

                if r_idx in (0, len(grid) - 1):
                    perimeter += 1
                else:
                    if grid[r_idx - 1][c_idx] == 0:
                        perimeter += 1
                    if grid[r_idx + 1][c_idx] == 0:
                        perimeter += 1

    return perimeter
