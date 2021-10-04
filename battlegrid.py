from settings import TILE_SIZE

from tile import Tile

class BattleGrid:

    def __init__ (self, width, height):

        self.w = width
        self.h = height

        self.grid = []

        for r in range (height):
            
            new_row = []

            for c in range (width):
                new_row.append (Tile())

            self.grid.append (new_row)


    def __str__ (self):

        output_string = '\n '

        # Letters Row
        letter_counter = 0
        for i in range (self.w * (TILE_SIZE + 1)):
            if i % 4 - 2 == 0 and i > 0:
                output_string += chr (65 + letter_counter)
                letter_counter += 1
            else:
                output_string += ' '

            

        output_string += '\n ┌'

        # top bars
        for i in range (self.w * (TILE_SIZE + 1) - 1):
            if i % 4 - 3 == 0 and i > 0:
                output_string += '┬'
            else:
                output_string += '─'

        output_string += '┐\n │'

        
        for tile_row in range (self.h):

            for r in range (TILE_SIZE):

                for tile_col in range (len (self.grid [tile_row])):

                    for c in range (TILE_SIZE):
                        tile = self.grid [tile_row] [tile_col]
                        output_string += tile.grid [r] [c]

                    if tile_col != len (self.grid[tile_row]) - 1:
                        output_string += '│'

                if tile_row == self.h - 1 and r == 2:
                    output_string += '│\n '
                else:
                    if r == 0:
                        output_string += '│\n' + str (tile_row + 1) + '│'
                    else:
                        output_string += '│\n │'

            if tile_row < self.h - 1:
                for w in range (self.w * (TILE_SIZE  + 1) - 1):
                    if w % 4 - 3 == 0 and w > 0:
                        output_string += '┼'
                    else:
                        output_string += '─'
                output_string += '│\n │'

        # bottom row


        output_string += '└'
        for i in range (self.w * (TILE_SIZE + 1) - 1):
            if i % 4 - 3 == 0 and i > 0:
                output_string += '┴'
            else:
                output_string += '─'

        output_string += '┘\n'

        return output_string


    def addTile (self, name,  position:str):
        letter = position [0]
        number = position [1]

        if not letter.isalpha() or not number.isnumeric():
            print ('invalid position given to addTile() ->', position)
            return

        letter = letter.upper()
        letter = ord (letter) - 65

        number = int (number) - 1

        print ('adding ', name,' to ',  position,  ' -> (', letter,', ', number, ')', sep='')

        self.grid [number] [letter].createTile (name)

        
        




if __name__ == '__main__':

    test_battlegrid = BattleGrid (8, 3)

    test_battlegrid.addTile ('E', 'A1')

    print (test_battlegrid)