# Mad Libs Generator - Mahir Berke Durmaz (13th May 2021)

loop = 1

while loop :
    
    # Questions that program asks to user.
    pir = input("Person in room: ")
    num = input("Number: ")
    adj = input("Adjective: ")
    clr = input("Color: ")
    noun = input("Noun: ")
    tof = input("Type of food (plural): ")
    noun2 = input("Noun: ")
    vrb = input("""Verb ending in "ing": """) # I used triple quotation marks because of the "ing" word.
    aoc = input("Article of clothing: ")
    adj2 = input("Adjective: ")
    clbr = input("Celebrity: ")
    clbr += "." # I added period beacuse the celebrity word is going to be last word of 4th article. 
    num2 = input("Number: ")
    pir2 = input("Person in room: ")
    noun3 = input("Noun: ")
    noun3 += "," 
    pir3 = input("Person in room:")
    occ = input("Occupation: ")
    occ += "!" 

    # Displays the story based on users words.
    
    print()
    print("------------------------------------------------------------------------")
    print()
    
    print("My name is", pir, "and I am", num, "years old. If i were president, I'd do a whole bunch of", adj, "things:")
    print()
    print("1. I would drive the biggest", clr, "car in the country. And that car would go faster than any other", noun, "in the world!")
    print("2. Everyone would eat pepperoni", tof, "for dinner")
    print("3. I would live in the Statue of", noun2, "and build a", vrb, "pool at her feet.")
    print("4. I would wear a/an", aoc, "on my head, and everyone would say I look", adj2, "like", clbr)
    print("5. School would be open only", num2, "days a year.")
    print("6. I would give my friends the best jobs. I would nominate", pir2, "to be secretary of (the)", 
         noun3, "and", pir3, "could be vice", occ)
    
    print()
    print("------------------------------------------------------------------------")
    print()
    
    # Asking to user if he/she wants to play again or not.
    desicion = input("Would you like to play again? Type Yes or No: ")
    
    if desicion == "Yes" or "yes" or "YES" or "yEs" or "yeS" : #yo go easy on it just use lowercase() bro 
      loop = 1
    else :
        print("Ok, thanks for playing Mad Libs. Goodbye!")
        loop = 0
