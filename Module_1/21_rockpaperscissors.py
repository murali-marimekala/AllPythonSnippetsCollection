#Program :Rock Paper Scissors

import random
def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    
    user_choice = input("Enter your hoice rock/paper/scissors :  ")
    computer_choice = random.choice(choices)

    if user_choice in choices:
        print(f"Your choice is {user_choice}")
        print(f"Computer choice is {computer_choice}")
        
        if user_choice == computer_choice:
            print("Its a tie !")    
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
            print("Congratualtions you Win !!")
        else:
            print("Sorry ! The computer wins")
    else:
        print("Invalid choice. Try again")
        
rock_paper_scissors()