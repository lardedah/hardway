#this one is like your scripts with argv
def print_two(*args): # creates function 'print_two'.
    arg1, arg2 = args # gives two variables arg1 + arg2 to args as parameters.
    print(f"arg1: {arg1}, arg2: {arg2}") # prints arg1 + arg2 with some text.

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): # creates function and gives it two parameters.
    print(f"arg1: {arg1}, arg2: {arg2}") # function returns string with each given argument formatted into it.

#this just takes one argument
def print_one(arg1): # creates a function, gives it one parameter.
    print(f"arg1: {arg1}") # calls print on the argument.

# this one takes no arguments
def print_none(): # creates variable with no parameters.
    print("I got nothin'.") # ..
          
          
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()