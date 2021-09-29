from settings import EMPTY_CHARACTER

class Tile:

    def __init__ (self, width, height):

        self.w = width
        self.h = height

        self.grid = []
        
        for r in range (self.h):

            new_row = []

            for c in range (self.w):
                new_row.append (EMPTY_CHARACTER)

            self.grid.append (new_row)


    def __str__ (self):

        string_representation = ''

        for r in range (self.h):
            for c in range (self.w):

                string_representation += self.grid [r] [c]

            if r < self.w - 1:
                string_representation += '\n'


        return string_representation



if __name__ == '__main__':

    test_tile = Tile(3, 3)

    print (test_tile)