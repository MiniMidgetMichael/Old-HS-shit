#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
from collections import OrderedDict
hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]
hex_dict = OrderedDict ({
    (0 , 0),
    (1 , 1),
    (2 , 2),
    (3 , 3),
    (4 , 4),
    (5 , 5),
    (6 , 6),
    (7 , 7),
    (8 , 8),
    (9 , 9),
    ("a" , 10),
    ("b" , 11),
    ("c" , 12),
    ("d" , 13),
    ("e" , 14),
    ("f" , 15)
})
hex_keys = list(hex_dict.keys())
#print (hex_keys)
hex_values = list(hex_dict.values())
