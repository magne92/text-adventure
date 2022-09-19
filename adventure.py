print("It was a nice day")
print("You see two doors, wich one do you enter?")
print("Left door: A  Right door: B")
answer = input("-> ")

if (answer == "A"):
    print("something")
    print("you explode, but you continue on in the afterlife")
    print("Do you want to enter heaven or hell? ")
    answer = input("Heaven: A  Hell: B")

    if (answer == "A"):
        print("you went to heaven and it was nice.")
    elif (answer == "B"):
        print("You went to hell and did not have a good time.")

elif (answer == "B"):
    print("something else")


if (answer == "B"):
    print("")
    