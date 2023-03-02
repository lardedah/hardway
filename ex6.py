#creates variable and sets it value of 10
types_of_people = 10
#creates variable 'x'. this is a string, with f string to include types_of_people (10)
x = f"There are {types_of_people} types of people."

#sets variable with string
binary = "binary"
#sets variable with string
do_not = "don't"
#makes a funny. creates variable y, which is set a string with the two previous lines' strings.
y = f"Those who know {binary} and those who {do_not}."

#prints each of these variables (which each have one or two variables formatted within them.)
print(x)
print(y)

#each prints an f-string that pulls in the previous variables.
print(f"I said: {x}")
print(f"I also said: '{y}'")

#sets a boolean
hilarious = False
#creates variable with a string and space for formatting
joke_evaluation = "Isn't that joke so funny?! {}"
#prints the variable (happens to be a string) and sets format to the boolean, hilarious. (which is false).
print(joke_evaluation.format(hilarious))

#creates two variables each given a string.
w = "This is the left side of..."
e = "a string with a right side."

#prints both variables (this prints the two strings, side by side.)
print(w + e)
