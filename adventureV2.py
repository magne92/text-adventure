def room1():
    print("Du står i et rom, der er det en boks. Det er også en dør å videre i.")
    print("Åpner du boksen? eller gå videre? A/B")
    valg = input("-> ")

    if (valg == "A"):
        print("Du åpnet boksen, det var pandoras boks, verden gikk under.")
        input("GAME OVER")

    elif (valg == "B"):
        print("Du gikk gjennom døren.")
        room2()

def room2():
    print("Du møter en mann i dette rommet.")
    print("Hva gjør du? A/B?")
    input("-> ")

def room3():
    print()
    

room1()


