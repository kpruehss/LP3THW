from time import sleep
# from random import random


rooms = {
    'Lounge': ['Kitchen', 'Study', 'Stairwell'],
    'Kitchen': ['Lounge', 'Pantry'],
    'Study': ['Lounge', 'Stairwell'],
    'Stairwell': ['Upstairs', 'Basement'],
    'Laundry': ['Window', 'Garage', 'Upstairs']
    }


def lounge_room():
    print("You are standing lounge room you just saw on TV")
    sleep(2)
    print("What if the killer comes after you? You need to prepare!")
    sleep(2)
    print("You scan the room, but see nothing of use.")
    sleep(3)
    print("You can see the kitchen and the study. Perhaps there?")


def kitchen_room():
    print("You're in the kitchen.")


def study_room():
    print("You're in the study.")


lounge_room()


def draw_choice(doors):
    for i, door in enumerate(doors):
        print(f"{i}: {door}")
