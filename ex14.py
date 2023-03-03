from sys import argv
script, user_name, user_age = argv
words = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(words)


print(f"Where do you live {user_name}?")
lives = input(words)

print(f"How old are you {user_name}?")
user_age = input(words)

print("What kind of computer do you have?")
computer = input(words)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
You are {user_age}.
And you have a {computer} computer. Nice.
""")
