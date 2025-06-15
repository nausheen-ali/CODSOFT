import random

def user_choice():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("Enter your choice:"))

    if choice in [1,2,3]:
        if (choice == 1):
            return "Rock"
        elif (choice == 2):
            return "Paper"
        else:
            return "Scissors"
    else :
        print("Invalid choice. Try again.")
        return user_choice()
    
def comp_choice():
    return random.choice(["Rock","Paper","Scissors"])

def winner(user,comp):
    if user==comp:
        return "Tie"
    elif (
        (user == "Rock" and comp == "Scissors") or
        (user == "Scissors" and comp == "Paper") or
        (user == "Paper" and comp == "Rock")
    ):
        return "User"
    else:
        return "Computer"
    
def play_again():
    while True :
        print ("1. Play again")
        print ("2. Quit game")
        choice = int(input("Enter choice:"))

        if (choice == 1):
            return True
        elif choice == 2:
            return False
        else:
            print("Invalid choice. Try again.")
            return play_again()
    
def play_game():
    user_score=0
    comp_score=0
    round_number=1

    while True:
        print("Round number : ", round_number)
        user=user_choice()
        comp=comp_choice()

        print("You choose: ", user)
        print("Computer choose: ",comp)

        result=winner(user,comp)
        if result=="Tie":
            print("It's a Tie!")
        elif result=="User":
            user_score+=1
            print("You Win!!!")
        else:
            comp_score+=1
            print("Computer Wins!")

        print(f"Score after round {round_number}: You: {user_score} | Computer: {comp_score}")
        round_number+=1

        if not play_again():
            break
    
    print("Game over!")
    print(f"Final Scores after {round_number-1} rounds:\n You: {user_score} | Computer: {comp_score}")

    if user_score>comp_score:
        print("You win this game!!!")
    elif comp_score>user_score:
        print("Computer wins this game!")
    else:
        print("It's a Tie!")

    
print("ROCK PAPER SCISSOR GAME")
play_game()