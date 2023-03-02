formatter = "{} {} {} {}" # creates variable called 'formatter'. assigns four ?empty values? ?place holders?

print(formatter.format(1, 2, 3, 4)) # prints the variable 'formatter' with the four (int) arguments
print(formatter.format("one", "two", "three", "four")) #prints the variable with four strings
print(formatter.format(True, False, False, True)) #prints with four boolean?s? ?values?
print(formatter.format(formatter, formatter, formatter, formatter)) #prints the variable 'format' with the arguments set as the literal contents of the variable 'formatter'.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
    
))                          #prints the variable 'formatter' with four arguments, all strings. they happen to be a tuple?

