from sys import argv

script, test_file = argv

run_test_file = open(test_file)

print (f"Here is your file, \'{test_file}\', my dude")
print (run_test_file.read())

run_test_file.close()