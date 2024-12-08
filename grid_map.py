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
        for f, frequency in enumerate(self.antennae):
            # print("{f}: {list}".format(f=frequency, list=self.antennae[frequency]))
            if (len(self.antennae[frequency]) < 2): 
                print("// SKIPPED DUE TO LONELINESS: " + frequency)
                continue
            print("// PROJECTING COORDS FOR: " + frequency)
            applicants = self.antennae[frequency]
            for a, antenna in enumerate(applicants):
                for b, bantenna in enumerate(applicants):
                    if (a == b): continue
                    else: self.project_antinode(antenna, bantenna)
                        
    def project_antinode(self, a, b):
        delta = (b[0] - a[0], b[1] - a[1])
        c = (b[0] + delta[0], b[1] + delta[1])
        if self.is_within_bounds(c):
            print("// {a} -> {b} --{d}--> {c}".format(a=a, b=b, c=c, d=delta))
            self.record_antinode_position(c)
        else:
            print("// OUT OF BOUNDS: {coords}".format(coords=c))
    
    def record_antinode_position(self, coords):
        # TODO Check for duplicates
        self.antinodes.append(coords)

    def is_within_bounds(self, coords):
        if coords[0] >= 0 and coords[0] < self.width and coords[1] >=0 and coords[1] < self.height:
            return True
        else:
            return False

    def print_debug_maps(self):
        composite_map = deepcopy(self.grid)
        
        antinode_map = deepcopy(self.grid)
        for n, coords in enumerate(self.antinodes):
            antinode_map[coords[1]][coords[0]] = '#'
            composite_map[coords[1]][coords[0]] = '#'

        antennae_map = deepcopy(self.grid)
        for f, frequency in enumerate(self.antennae):
            for c, coords in enumerate(self.antennae[frequency]):
                antennae_map[coords[1]][coords[0]] = frequency
                composite_map[coords[1]][coords[0]] = frequency

        self.draw_map(antennae_map, "Antennae only")
        self.draw_map(antinode_map, "Antinodes only")
        self.draw_map(self.data, "Reference input")        
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