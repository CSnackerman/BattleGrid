from tile import Tile

########################
# What's a battlegrid? #
########################
# A GRID of GRIDS!?!?! #
########################

class BattleGrid:

    def __init__ (self, width, height):

        # Objectives:
        #   1. set the self width to the width argument (replace 0)
        #   2. set the self height to the height argument (replace 0)
        self.w = 0
        self.h = 0

        return


    def __str__ (self):

        # Objectives:
        #   1. Replace the zeroes inside the parenthesese with
        #      self width and self height
        output_string = "Hi! I'm a "
        output_string += str ( 0 ) + 'x' + str ( 0 )
        output_string += " battlegrid object. I was created by __init__()."

        return output_string




# Here is where we can test battlegrids!
if __name__ == '__main__':

    test_battlegrid = BattleGrid (10, 10)

    print (test_battlegrid)