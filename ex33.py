from sys import argv
numbers = []
script, limit, step = argv


def while_loop(limit, step=1):
    i = 0
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += step
        print("Numbers now: ", numbers)
        print(f"At the bottom, i is {i}")


while_loop(int(limit), int(step))
print("The Numbers: ")

for num in numbers:
    print(num)
