#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
from alphabet_dict import alphabet, alphabet_items, alphabet_values, alphabet_keys
from collections import OrderedDict

##print (alphabet_keys, alphabet_values)

nums_1 = (23, 5, 12, 12, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 8, 9, 4, 4, 5, 14, 27, 8, 5, 18, 5, 27, 2, 21, 20, 27, 6, 9, 18, 19, 20, 27, 23, 5, 27, 8, 1, 22, 5, 27, 19, 15, 13, 5, 27, 20, 5, 24, 20, 27, 20, 15, 27, 3, 15, 14, 6, 21, 19, 5, 27, 25, 15, 21, 27, 14, 15, 23, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 9, 14, 27, 6, 1, 3, 20, 27, 19, 5, 3, 18, 5, 20, 19, 28, 1, 18, 5, 28, 8, 9, 4, 4, 5, 14, 28, 9, 14, 28, 20, 8, 9, 19, 28, 12, 9, 19, 20, 27, 4, 15, 14, 20, 27, 9, 14, 3, 12, 21, 4, 5, 27, 20, 8, 5, 27, 16, 1, 18, 20, 19, 27, 20, 8, 1, 20, 27, 1, 18, 5, 27, 19, 5, 16, 5, 18, 1, 20, 5, 4, 27, 23, 9, 20, 8, 27, 19, 16, 1, 3, 5, 19)
alphas = []

for i in nums_1:
    alphas += alphabet_keys[alphabet_values.index(i)]
    ##print (i)

##print (alphas)

##print (''.join(alphas))

nums_2 = [22,12,200,12,1000,212,12,1000,210,201,12,1000,202,12,200,112,1,200,221,1000,202,120,1000,21,12,202,1000,202,22,12,1000,20,110,1,21,1000,202,22,200,12,12,1001,11,100,21,100,202,201,1001,100,201,112,202,1001,211,12,200,221,1001,201,12,10,210,200,12]

def is_bin(x):
    x = str(x)
    bad = []
    index = 0
    while not(index == len(x) - 1):
        for i in x:
            if i != "0" and i != "1":
                bad += i
        index += 1
    if len(bad) > 0:
        return False
    else:
        return True

nums_2_bin = []
for index, i in enumerate(nums_2):
    ##print (index)
    ##print (is_bin(i))
    if is_bin(i):
        nums_2_bin.append(i)
        nums_2.pop(index)
        ##print (index, i)

##print (nums_2_bin)
    
##print (nums_2)

for i in nums_2_bin:
    print (b'\x%s' % i)
