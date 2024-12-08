from grid_map import GridMap

print("// Advent of Code 2024 - Day 8: Resonant Collinearity //////////////////////////")
EXAMPLE = [ "......#....#\n",
            "...#....0...\n",
            "....#0....#.\n",
            "..#....0....\n",
            "....0....#..\n",
            ".#....A.....\n",
            "...#........\n",
            "#......#....\n",
            "........A...\n",
            ".........A..\n",
            "..........#.\n",
            "..........#.\n" ]

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        INPUT = file.readlines()
    map = GridMap(EXAMPLE)

