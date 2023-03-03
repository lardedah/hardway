from sys import argv
script_name, t, o, m, m, y = argv

print("The script is called:", script_name)
print("Your first variable is:", t)
print("Your second variable is:", o)
print("Your third variable is:", m)
print("This extra thing is:", m)
print("This other extra thing is:", y)

explanation = input("Can you explain where those arguments came from please? \n\n")

print("\n\nOh!", "\"" + explanation + "\"", "\n\n \t\t ... well. alright then.")