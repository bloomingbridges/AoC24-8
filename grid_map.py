from copy import deepcopy

class GridMap:
    def __init__(self, data):
        self.data = data
        self.width = len(data[0]) - 1 # Newline character
        self.height = len(data)
        self.antennae = {}
        self.antinodes = []
        self.grid = []
        self.setup_grid()
        print("// New {w}x{h} GridMap created".format(w=self.width, h=self.height))

    def setup_grid(self):
        for r in range(self.height):
            row = []
            for c, char in enumerate(self.data[r]):
                row.append('.')
            self.grid.append(row)

    def find_antennae(self):
        print("// Tuning in..")
        for y, row in enumerate(self.data):
            for x, char in enumerate(row):
                if char != '.' and char != '#' and char != '\n':
                    self.record_antenna_position(char, x, y)
        # print(self.antennae)

    def record_antenna_position(self, frequency, x, y):
        print("// Found antenna with frequency {f} at x:{x}, y:{y}".format(f=frequency, x=x, y=y))
        if self.antennae.get(frequency):
            self.antennae[frequency].append((x, y))
        else:
            self.antennae[frequency] = [(x, y)]

    def project_antinodes(self):
        pass

    def print_debug_maps(self):
        antinode_map = deepcopy(self.grid)
        self.draw_map(antinode_map, "Antinodes only")

        antennae_map = deepcopy(self.grid)
        for f, frequency in enumerate(self.antennae):
            for c, coords in enumerate(self.antennae[frequency]):
                antennae_map[coords[1]][coords[0]] = frequency
        self.draw_map(antennae_map, "Antennae only")

        # reference_map = deepcopy(self.grid)
        # self.draw_map(reference_map, "Reference input")

        composite_map = deepcopy(self.grid)
        self.draw_map(composite_map)

    def draw_map(self, map, name = "Composite output"):
        print("// " + name)
        for y, row in enumerate(map):
            row_string = ""
            for x, col in enumerate(row):
                if (x < self.width):
                    row_string += col
            print(row_string)
        print()