correct = True
while correct:
    print("Are you a potato?y/n")
    answer = input()
    if answer == 'y':
        print("Congrats, so am I!!!!!!!!!!!!!!!!!")
        quit()
    if answer == 'n':
        print("You have failed the spud test!!!!!")
        print("Would you like to attempt the spud test again?y/n")
        answer2 = input()
        if answer2 == 'y':
            correct = True
        if answer2 == 'n':
            print("Too bad. See ya soon. Hopefully.")
            quit()
