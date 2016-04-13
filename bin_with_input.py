#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
from alphabet_dict import *
from number_funct import *
from macpath import *
from pathlib import *
text = input("Please type what you want to be ciphered:")
#print (alphabet)
#print (alphabet_items, alphabet_values)
text_list = []
for i in text:
    if i != " ":
        text_list.append(i)
print ("#text_list", text_list)
old_text = list(text_list)
print ("#old_text", old_text, "\n")
"""OLD_TEXT IS LAST ORDERED LIST"""
only_text = []
leftovers = []
for i in text_list:
    if is_number(i) == False:
        only_text += [i]
    else:
        leftovers += [i]
new_list = []
ordered_text = {}
for index, i in enumerate(leftovers):
    ordered_text[index] = i
"""CREATE DICTIONARY WITH KEYS = INDEX of VALUES & VALUES = TEXT"""
print ("#ordered_text", ordered_text, "\n")
print ("#only_text", only_text, "\n")
print ("#leftovers", leftovers, "\n")
test_tpl = alphabet
mapping = dict(test_tpl)
""" HERE IS WHERE LIST GETS MIXED UP"""
test_tpl = [(x,mapping[x]) for x in only_text]
for a, b in test_tpl:
    new_list.append(b)
for x in ordered_text:
    new_list.insert(x, ordered_text[x])
print ("#new_list", new_list)
print ("#list_to_bin", list_to_bin(new_list), "\n")
print(mix_up(new_list))
