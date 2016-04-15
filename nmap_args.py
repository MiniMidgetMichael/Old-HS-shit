#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
with open("P:/Python/Nmap_Args.txt", "r") as f:
    nmap_args = f.read()
    nmap_args = nmap_args.split()
    ##print (nmap_args)
    nmap_args.append("--help")
