#Alex Ozdemir
#aozdemir@hmc.edu

# cell and grid classes, which represent memetic agents and arrangements respectively

from random import random, choice, randrange

PROBABILITY_OF_INNOVATION = 0.25

def VALUE(color):
    sum1 = sum(color)
    return max(sum1, 255 * 3 - sum1)

class Cell(object):
    """Represents one Cell in a memetic grid"""
    def __init__(self, r, c, color = [127., 127., 127.]):
        self.r = r
        self.c = c
        self.color = [x for x in color]
        self.last_color = [x for x in color]
        self.neighbors = None

    def set_neighbors(self, neighbors):
        """Sets the neighbors the Cell thinks it has (Cells it is next to)"""
        self.neighbors = neighbors

    def change(self):
        """Change the cel, either innovating or coppying neighbors"""
        self.last_color = [x for x in self.color]
        if random() < PROBABILITY_OF_INNOVATION:
            self.mutate()
        else:
            self.copy_neighbors()

    def mutate(self):
        """Change a Cell according to mutation"""
        n =  random()
        # An icky calculation to determin change amount
        #  we choose which color component to change
        m = randrange(len(self.color))
        #  we choose an up-or down change
        #  and we choose a random change magnitude
        #  (^3 makes it favor small changes)
        self.color[m] += choice([-1,1]) * (20.0 * n ** 3.0)
        # Correct colors into valid range
        if self.color[m] > 255:
            self.color[m] = 255
        if self.color[m] < 0:
            self.color[m] = 0

    def copy_neighbors(self):
        """Change a Cell by imitating a best neighbor"""
        value_color_pairs = [(VALUE(n.last_color), n.last_color)\
                             for n in self.neighbors]
        best_value = max(value_color_pairs)[0]
        new_color = choice(filter(lambda x: x[0] == best_value, value_color_pairs))[1]
        self.color = [x for x in new_color]

    def __str__(self):
        #return "<Cell at (%d, %d)>" % (self.r, self.c)
        return "|%d, %d, %d|" % tuple(self.color)
        
class Grid(object):
    def __init__(self, side_length):
        self.cells = [[Cell(r, c) for c in range(side_length)] \
                      for r in range(side_length)]
        self.side_length = side_length
        self.set_all_neighbors()

    def get_neighbors(self, r, c):
        """Gets a list of neighbors of the r,c cell"""
        if not (0 <= r < self.side_length and 0 <= c < self.side_length):
            raise IndexError("The row, column pair (%d, %d) is outside the grid"\
                             % (r, c))
        neighbors = []

        # We go through each of the eight neighbors, 
        # and add them if edges check out
        
        # Top
        if r != 0:
            neighbors.append(self.cells[r - 1][c])
        # Bottom
        if r != self.side_length - 1:
            neighbors.append(self.cells[r + 1][c])
        # Left
        if c != 0:
            neighbors.append(self.cells[r][c - 1])
        # Right
        if c != self.side_length - 1:
            neighbors.append(self.cells[r][c + 1])
        # Top Left
        if r != 0 and c != 0:
            neighbors.append(self.cells[r - 1][c - 1])
        # Top Right
        if r != 0 and c != self.side_length - 1:
            neighbors.append(self.cells[r - 1][c + 1])
        # Bottom Left
        if r != self.side_length - 1 and c != 0:
            neighbors.append(self.cells[r + 1][c - 1])
        # Bottom Right
        if r != self.side_length - 1 and c != self.side_length - 1:
            neighbors.append(self.cells[r + 1][c + 1])

        return neighbors

    def set_all_neighbors(self):
        """Sets each cells' neighbors to its grid-neighbors"""
        for r in range(self.side_length):
            for c in range(self.side_length):
                self.cells[r][c].set_neighbors(self.get_neighbors(r, c))
    def __iter__(self):
        self.iter_count = 0
        return self

    def next(self):
        if self.iter_count == self.side_length ** 2:
            raise StopIteration
        else:
            r = self.iter_count / self.side_length
            c = self.iter_count % self.side_length
            self.iter_count += 1
            return self.cells[r][c]

    def execute_evolution(self, n):
        """Does 'n' rounds of memetic evolution"""
        for i in range(n):
            for cell in self:
                cell.change()
                
    def __str__(self):
        res = ""
        for r in self.cells:
            for c in r:
                res += str(c) + " "
            res += "\n"
        return res

