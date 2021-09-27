from settings import EMPTY_CHARACTER

# This one is done for you!

class Tile:

    # this an extremely common magic-function that
    # creates a TILE object in the computer memory
    def __init__ (self, width, height):

        self.w = width
        self.h = height

        self.grid = []
        
        # A for-loop inside of a for-loop!
        for r in range (self.h):

            new_row = []

            for c in range (self.w):
                new_row.append (EMPTY_CHARACTER)

            self.grid.append (new_row)



    # This is the magic-function which is called
    # whenever we use PRINT on a TILE
    def __str__ (self):

        string_representation = ''


        # go through every item in the grid
        for r in range (self.h):
            for c in range (self.w):

                string_representation += self.grid [r] [c]

            if r < self.w - 1:
                string_representation += '\n'


        return string_representation




# Here is where we can test our tiles!
if __name__ == '__main__':

    test_tile = Tile(3, 3)

    print (test_tile)