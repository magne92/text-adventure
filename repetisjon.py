#inventory
knives = 0
rope = 1
bombs = 0
stones = 0

def start_room():
    print("You are in a dark room, with two doors. There is two big letters on the doors. A and B")
    choice = input("Door A or B? -> ")

    if (choice == "A"):
        room1()

    elif (choice == "B"):
        room2()

def room1():
    global stones
    print("You are in room 1")
    print("You found a stone on the ground. You took it.")

    stones += 1

    choice = input("What will you do in this room? A: Jump or B: Dig")
    if (choice == "A"):
        room3()

    elif (choice == "B"):
        room4()


def room2():
    print("You are in room 2")

def room3():
    print()

def room4():
    print()

start_room()


