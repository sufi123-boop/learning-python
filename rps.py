def user_choice(): # function to get user input
    while True:
        choice = input("Please enter your move (rock, paper, scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def computer_choice(): # function to get computer's random choice
    import random
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):   # function to determine the winner
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!" 

user = user_choice() #determining the winner
computer = computer_choice()
result = determine_winner(user, computer)

print(f"You chose: {user}")   #printing user and computer choices and the result
print(f"Computer chose: {computer}")
print(result)        