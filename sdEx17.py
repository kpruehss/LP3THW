from sys import argv

with open(argv[2], 'w') as f:
    f.write(open(argv[1]).read())
