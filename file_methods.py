#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
from fnmatch import *
from turtledemo import *
def strip_space(op_file):
    with open(op_file, "r") as file:
        ##print (file.read())
        file_text = str(file.read())
        ##print (file_text)
        file_filter = filter(lambda x: x != " ", file_text)
        file_filtered = [i for i in file_filter]
        ##print (file_filtered)
        file_nospace = ""
        for i in file_filtered:
            file_nospace += i
        ##print(file_nospace)
        return file_nospace


##print (strip_space("P:/Python/alphabet_dict.py"))
##TESTING
