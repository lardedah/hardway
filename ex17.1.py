from sys import argv # imports argv from sys module
from os.path import exists # imports os.path.exists function from os.path module
script, from_file, to_file = argv # sets parameters for argv, to be given arguments in command line
indata = open(from_file).read() # creates 'indata', a function to take 'from_file' and open it as read.
out_file = open(to_file, 'w') # 
out_file.write(indata)
out_file.close()