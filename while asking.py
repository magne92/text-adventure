def room1():
    print("Du står i et rom, der er det en boks. Det er også en dør å videre i.")
    print("Åpner du boksen? eller gå videre? A/B")
    asking = True
    while asking == True:
        print("Choose A or B")
        choice = input("-> ")

        if (choice == "A"):
            asking = False
            room2()

        elif (choice == "B"):
            asking = False
            room3()

        else:
            print("Your input was not an alternative, try again")


def asking_function():
    global asking
    
    

