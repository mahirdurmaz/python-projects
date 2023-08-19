# Mad Libs Generator - Mahir Berke Durmaz (13th May 2021)
# contribute - Edinbo
def new_game():

    # Questions that program asks to user.
    pir = input("Name: ")
    num = input("Age: ")
    adj = input("Adjective: ")
    clr = input("Color: ")
    noun = input("Noun: ")
    tof = input("Meal for everyone: ")
    noun2 = input("Noun: ")
    vrb = input("Verb ending in (ing): ")
    aoc = input("Article of clothing: ")
    adj2 = input("Adjective: ")
    clbr = input("Celebrity: ")
    clbr += "." 
    num2 = input("Number: ")
    pir2 = input("Person in room: ")
    noun3 = input("Noun: ")
    noun3 += ","
    pir3 = input("Person in room:")
    occ = input("Occupation: ")
    occ += "!"

    # Displays the story based on users words.
    print("\n------------------------------------------------------------------------\n")
    print(f"My name is {pir} and I am {num} years old. If i were president, I'd do a whole bunch of {adj} things:\n")
    print(f"1. I would drive the biggest {clr} car in the country. And a car would go faster than any other {noun} in the world!")
    print(f"2. Everyone would eat {tof} for dinner")
    print(f"3. I would live in the Statue of {noun2} and build a {vrb} pool at her feet.")
    print(f"4. I would wear a/an {aoc} on my head, and everyone would say I look {adj2} like {clbr}")
    print(f"5. School would be open only {num2} days a year.")
    print(f"6. I would give my friends the best jobs. I would nominate {pir2} to be secretary of (the) {noun3} and {pir3} could be vice {occ}")
    print("\n------------------------------------------------------------------------\n")

    decision = input("Would you like to play again? Type Yes or No: ").lower()

    if decision != "yes":
        print("Ok, thanks for playing Mad Libs. Goodbye!")
        exit()
    else:
        new_game()

new_game()
