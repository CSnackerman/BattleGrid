from tile import Tile

class BattleGrid:

    def __init__ (self, width, height):

        self.w = width
        self.h = height

        return


    def __str__ (self):

        output_string = "Hi! I'm a "
        output_string += str ( self.w ) + 'x' + str ( self.h )
        output_string += " battlegrid object. I was created by __init__()."

        return output_string




if __name__ == '__main__':

    test_battlegrid = BattleGrid (10, 10)

    print (test_battlegrid)