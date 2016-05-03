#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
import random, math

"""CREATE GRID FOR AI:

OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO

[16x6]


"""


class grid_(object):
    def __init__(self, x_len=16, y_len=6, chr_sp='O', chr_e='*'):
        assert type(x_len) is int, "%s is of %s, not an integer" % (str(x_len), type(x_len))
        assert type(y_len) is int, "%s is of %s, not an integer" % (str(y_len), type(y_len))
        assert type(chr_sp) is str, "%s is of %s, not a string" % (chr_sp, type(chr_sp))
        assert type(chr_e) is str, "%s is of %s, not a string" % (chr_e, type(chr_e))
        self.x_len = x_len
        self.y_len = y_len
        self.chr_sp = chr_sp
        self.chr_e = chr_e
        self.__gen()

    def __gen(self):
        ##create grid and locations
        x_len = self.x_len
        y_len = self.y_len
        grid_x = {}
        grid_y = {}
        chr_sp = self.chr_sp
        for i in range(x_len):
            grid_x[i] = chr_sp
        for i in range(y_len):
            grid_y[i] = chr_sp
        ##print (grid_x)
        ##print (grid_y)
        self.grid_x = grid_x
        self.grid_y = grid_y

    def update(self, loc, chr_):
        assert ((type(loc) is str) and len(loc) == 2), "location must be str with a len of 2"
        assert ((type(chr_) is int) and (chr_ == 0 or chr_ == 1)), "character must be int and 0 or 1"
        x_len = self.x_len
        y_len = self.y_len
        chr_sp = self.chr_sp
        chr_e = self.chr_e
        grid_x = self.grid_x
        grid_y = self.grid_y
        x_loc = int(loc[0])
        y_loc = int(loc[1])
        if chr_ == 1:
            char = chr_e
            grid_x[x_loc] = char
            grid_y[y_loc] = char
        else:
            char = chr_sp
            grid_x[x_loc] = char
            grid_y[y_loc] = char
        print (grid_x)
        print (grid_y)
        
    

grid = grid_()

grid.update('01', 1)
grid.update('12', 1)




        
        
