from settings import EMPTY_CHARACTER
from settings import TILE_SIZE

class Tile:

    def __init__ (self, name=None):

        self.grid = []
        
        for r in range (TILE_SIZE):

            new_row = []

            for c in range (TILE_SIZE):

                new_row.append (EMPTY_CHARACTER)

            self.grid.append (new_row)


        self.createTile (name)


    def __str__ (self):

        string_representation = ''

        for r in range (TILE_SIZE):
            for c in range (TILE_SIZE):

                string_representation += self.grid [r] [c]

            if r < TILE_SIZE - 1:
                string_representation += '\n'


        return string_representation



    def createTile (self, name):

        if name == None:
            return


        if name == 'E':
            self.create_E()
            return

        if name == 'A':
            self.create_A()
            return


    def create_E (self):

        self.grid [TILE_SIZE // 2] [TILE_SIZE // 2] = 'E'
        self.grid [TILE_SIZE // 2] [TILE_SIZE // 2 + 1] = '-'

    def create_A (self):
        
        self.grid [TILE_SIZE // 2] [TILE_SIZE // 2] = 'A'
        self.grid [TILE_SIZE // 2] [TILE_SIZE // 2 + 1] = '-'



if __name__ == '__main__':

    test_tile = Tile('A')

    print (test_tile)