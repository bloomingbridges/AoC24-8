class GridMap:
    def __init__(self, data):
        self.map = data
        self.width = len(data[0]) - 1 # Newline character
        self.height = len(data)
        print("// New {w}x{h} GridMap created".format(w=self.width, h=self.height))