from sys import argv

input_file = argv[1]

content = ""

with open(input_file) as f:
    content = f.read()

print(content)
