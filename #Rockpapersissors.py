while True :
    person1 = input("enter you choice (rock,paper,scissor) : ")
    person2 = input("enter you choice (rock,paper,scissor) : ")
    if person1 == person2:
        print("tie")
    elif person1 == "rock":
        if person2 == "scissor":
            print("congratulations person1 ! you won")
        else:
            print("congratulations person2 ! you won")
    elif person1 == "paper":
        if person2 == "rock":
            print("congratulations person1 ! you won")
        else:
            print("congratulations person2 ! you won")
    elif person1 == "scissor":
        if person2 == "paper":
            print("congratulations person1 ! you won")
        else:
            print("congratulations person2 ! you won")
    response = input("do you want play again? (yes or no) : ")
    if response == "yes" :
        continue