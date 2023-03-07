from sys import argv # imports argv from sys module
from os.path import exists # imports os.path.exists function from os.path module

script, from_file, to_file = argv # sets parameters for argv, to be given arguments in command line

print(f"Copying from {from_file} to {to_file}") # prints a string, gives information to human

# we could do the below in one line. how?
in_file = open(from_file) #
indata = in_file.read() # reads the opened from file

print(f"The input file is {len(indata)} bytes long") #prints formatted string, telling human the len(gth) of indata(from_file)

print(f"Does the output file exist? {exists(to_file)}") # prints a formatted string, runs exists check and returns boolean re:to_file.
print("Ready, hit RETURN to continue, CTRL_C to abort.") # prints a string, gives info to human
input() # any input satisfies this 

out_file = open(to_file, 'w')
out_file.write(indata)


out_file.close()
in_file.close()