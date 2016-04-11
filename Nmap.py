#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
#! C:\Users\MichaelLFarwell\AppData\Local\Programs\Python\Python35-32\python.exe

import subprocess as sp
import webbrowser, os, methods
from number_funct import *

##proc = sp.Popen('cmd.exe', stdin = sp.PIPE, stdout = sp.PIPE)

sp.check_output("dir C:\Windows\winsxs\wow64_microsoft-windows-commandprompt_31bf3856ad364e35_6.1.7601.17514_none_f387767e655cd5ab", shell=True).decode()

print ("TEST")
##print (sp.check_output(['nmap', '--help'], shell=True).rstrip().decode())
##import os;
##os.system("C:\\Temp\\a b c\\Notepad.exe");
##raw_input();

##print ("TEST")

def filter_for_int(s):
    if is_number(s):
        return s


def ask_for_input():
    option = input('What would you like to do? \n [R]un Zenmap \n [N]map scan \n [I]P config \n [D]efault Gateway \n [S]how available options \n [H]elp \n [C]lear \n [E]nd \n').casefold()
    option_list = ("s", "h", "e", "r", "i", "d", "c", "n",)
    while not(option in option_list):
        print (option + " is not a valid answer \n")
        option = input('What would you like to do? \n [R]un Zenmap \n [N]map scan \n [I]P config \n [D]efault Gateway \n [S]how available options \n [H]elp \n [C]lear \n [E]nd \n').casefold()
    if option == 's':
            ##print ("debug")
            print (sp.check_output(['nmap', '--help'], shell=True).rstrip().decode())
            ask_for_input()
    elif option == 'h':
            help_type = input('Which page? \n [W]iki page \n [N]map website \n [E]xit \n').casefold()
            while not(help_type == "w") and not(help_type == "n") and not(help_type == "e"):
                print("%s is not an answer \n" % help_type)
                help_type = input('Which page? \n [W]iki page \n [N]map website \n [E]xit \n').casefold()
            if help_type == "n":
                webbrowser.open("https://nmap.org/book/man-briefoptions.html")
                ask_for_input()
            elif help_type == "w":
                webbrowser.open("https://en.wikipedia.org/wiki/Nmap")
                ask_for_input()
            else:
                ask_for_input()
    elif option == 'r':
        sp.call("P:\\Nmap\\zenmap.exe")
        ask_for_input()
    elif option == 'i':
        print (sp.check_output(['ipconfig', '/allcompartments', '/all'], shell=True).rstrip().decode(), " \n")
        ask_for_input()
    elif option == 'd':
        ipconfig = str(sp.check_output(['ipconfig', '/all'], shell=True).rstrip().decode())
        #   Default Gateway . . . . . . . . . : x.x.x.x
        dg_string = "Default Gateway . . . . . . . . . :"
        for index, i in enumerate(ipconfig):
            if ipconfig[index:index+35] == dg_string:
                default_gateway = ipconfig[index+35:index+50].strip()
        print ("Default Gateway: \n", default_gateway + "\n")
        ask_for_input()
        ##print ("#LEN", len(dg_string)) >>> 35
    elif option == 'c':
        methods.clearscreen()
        ask_for_input()
    elif option == "n":
        is_args = input("Any arguments? \n [Y] or [N] \n")
        while not(is_args == 'y' or is_args == 'n'):
            print (is_args + " is not an answer, please answer with 'y' or 'n' \n")
            is_args = input("Any arguments? \n [Y] or [N] \n")
        args = input("Arguments (seperated by comma): \n")
        valid_chars = (" ", "-", ",", "?",)
        for index, i in enumerate(args):
            if not(i in valid_chars or methods.is_alphanumeric(i)):
                print (i + " is not a valid character")
                args = input("Arguments (separated by comma): \n")
        arg_list = []
        args = ''.join(args)
        args = args.split(sep=',')
        for index, i in enumerate(args):
            if (i == " ") and (args[index+1] == " "):
                print (i)
        #while ('' in args):
            #args.remove('')
        print ("#ARGS", args)
        for index, i in enumerate(args):
            if not(i[0] == "-"):
                args[index] = "-" + i
        try:
            sp.check_output(['nmap', [i for i in args]], shell=True).rstrip().decode()
            good_args = True
        except:
            ValueError
            good_args = False
        if good_args:
            ip = input("Please give an ip: \n")
            print (sp.check_output(['nmap', [i for i in args], ip], shell=True).rstrip().decode())
            ask_for_input()
        else:
            print ("Invalid Arguments \n")
            ask_for_input()
    elif option == 'e':
            confirm = input("Are you sure? \n [Y]es or [N]o \n").casefold()
            while not(confirm == 'y' or confirm == 'n'):
                print (confirm + " is not an option, please answer with 'y' or 'n'")
                confirm = input("Are you sure? \n [Y]es or [N]o \n").casefold()
            else:
                if confirm == 'y':
                    exit
                else:
                    ask_for_input()


ask_for_input()

