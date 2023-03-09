from sys import argv # ?start? system module, import argument variable function

script, filename = argv # gives two arguments for argv.

print(f"We're going to erase {filename}.") # prints formatted string. this returns name of 'filename' as a string 
print("If you don't want that, hit CTRL-C (^C).") # this prints a string. CTRL + C is 'keyboard interrupt'.
print("If you do want that, hit RETURN.") # prints a string.

input("Press RETURN") # Wants a RETURN button press and proceeds if satisfied. human can press other keys and then press ENTER.

print("opening the file...") # prints a string and gives info. to human.
target = open(filename, 'a') # creates variable 'target', gives it function of taking 'filename', calls it with 'w' argument. ('w' truncates, 'empties)).

print("Truncating the file. Goodbye!") # prints a string. gives info to human.
#target.truncate() # calls truncate on 'target' variable. 'target' is 'filename', opened and truncated. do line 12 + 15 both truncate?

print("Now I'm going to ask you for the three lines.") # prints a string.

line1 = input("line 1: ") #
line2 = input("line 2: ") #
line3 = input("line 3: ") # creates three variables, each assigned a string from human input.

print("I'm going to write these to the file.") # prints a string and gives info to human.

target.write(f"{line1}\n{line2}\n{line3}\n")
#target.write(line1) 
#target.write("\n") 
#target.write(line2) 
#target.write("\n") 
#target.write(line3)     # calls 'write' function to 'target' variable with argument variable 'line 1/2/3'.  
#target.write("\n")   # calls 'write' function to 'target' variable with argument string.

print("And finally, we close it.") # prints a string.
target.close() # 