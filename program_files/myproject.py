print("Welcome to Python.iQ!")
player_name=input("Name: ")
playing=input("Do you to want to participate in the game? ").lower()
if playing != "yes":
    print("pls exit from the Game :(")
    exit()
else:
    print("okay!, Let's start the Game :)")
    score=0
    answer = input("What is adith's full name? ").lower()
    if answer.lower() == "adith sagar gowda":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    answer = input("whats the  date of birth of adith(only month)? ").lower()
    if answer == "june":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    answer = input("which is color does adith like the most? ").lower()
    if answer == "blue":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    answer = input("which game does adith love's the most? ").lower()
    if answer == "badminton":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 4) * 100) + "%.")
    if score==3 or score==4:
        print("EXCELLENT!..",player_name)
    else:
        print("Better luck next time...",player_name)
    print("Thank you for participating in the Python.iQ contest!",",",player_name)


