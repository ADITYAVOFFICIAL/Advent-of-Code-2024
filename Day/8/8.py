class AdventDay8:

    def __init__(self):
        self.map: dict[str, list] = {}
        self.antinodes = set()
        self.data = [x for x in self._load_data("./Inputs/8.txt").split("\n") if x != '']
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _load_data(self, filename: str):
        """Reads the data from a specified file."""
        with open(filename, "r") as file:
            return file.read()

    def find_antinodes(self, harmonic: bool):
        """Loops over the map and finds the antinodes for each pair of points.
        If harmonic is True, it will find the antinodes for each antinode and
        the closest point that created the antinode. It will then count the
        number of unique antinodes."""
        for char_spots in self.map.values():
            for i in range(len(char_spots) - 1):
                for j in range(i + 1, len(char_spots)):
                    a, b = char_spots[i], char_spots[j]
                    delta = [a[0] - b[0], a[1] - b[1]]
                    r_delta = [-1*x for x in delta]
                    self._find_next_antinodes(a, delta, harmonic)
                    self._find_next_antinodes(b, r_delta, harmonic)
        if not harmonic:
            self.part1 = len(self.antinodes)
        else:
            self.part2 = len(self.antinodes)

    def _find_next_antinodes(self, point, delta, harmonic: bool = False):
        """Finds the next antinodes for a point and delta. This is a recursive
        function that will continue to find antinodes until it reaches the
        edge of the map."""
        if harmonic:
            self.antinodes.add(point)

        potential = tuple([point[x] + delta[x] for x in range(2)])

        if self._check_in_bounds(potential):
            self.antinodes.add(potential)
            if harmonic:
                self._find_next_antinodes(potential, delta, harmonic)

    def _check_in_bounds(self, item):
        """Checks if an item is in bounds of the map."""
        return (item[0] >= 0 and item[0] < self.rows and
                item[1] >= 0 and item[1] < self.cols)

    def _process_data(self):
        """Processes the data and creates a map of the points. The map is a
        dictionary with the keys being the unique characters on the map and the
        value being a list of tuples of the coordinates of each occurance of
        the character key."""
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                if col == '.':
                    continue
                if col in self.map:
                    self.map[col].append((i, j))
                else:
                    self.map[col] = [(i, j)]
        self.rows = len(self.data)
        self.cols = len(self.data[0])


if __name__ == '__main__':
    day8 = AdventDay8()
    day8.find_antinodes(harmonic=False)
    day8.find_antinodes(harmonic=True)
    print(day8.part1, day8.part2)