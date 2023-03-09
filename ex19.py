def cheese_and_crackers(cheese_count, boxes_of_crackers): # defines function, assigns two parameters.
    print(f"You have {cheese_count} cheeses!") # prints a string with the argument passed to cheese_count variable.
    print(f"You have {boxes_of_crackers} boxes of crackers!") # ...
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # calls the function, passing 20 and 30 to the variable.


print("OR, we can use variables from our script:")
amount_of_cheese = 10 #
amount_of_crackers = 50 # assigns values to two variables...

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # calls the function using these two variables.


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) # calls the function with sums as arguments.


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # calls the function with sums, made of an integer and a variable, as arguments.