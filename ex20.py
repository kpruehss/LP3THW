from sys import argv


def print_all(f):
    print(">>> print_all f=", f)
    print(f.read())
    print("<<< print_all f=", f)


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(argv[1])

print("First, lets print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of liek a tape.")

rewind(current_file)

print("Now let's print 3 lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
