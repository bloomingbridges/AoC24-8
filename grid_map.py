class GridMap:
    def __init__(self, data):
        self.data = data
        self.width = len(data[0]) - 1 # Newline character
        self.height = len(data)
        self.antennae = {}
        print("// New {w}x{h} GridMap created".format(w=self.width, h=self.height))
        self.find_antennae()

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