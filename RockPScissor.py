#Random Python Library to allow the computer
#Rock is 1, Paper is 2, Scissor is 3
#if both players select same is draw
#
#call the random library
import random
# user to enter the choice and compare with the  computer

#initialise the counters for wins
playerWins = 0
computerWins = 0

#set maximum score to 3
scoreMax= 3

playerChoice = input("Enter a choice (rock, paper,scissors): ")
#computer selects choice
selecter = ["rock", "paper", "scissors"]
computerChoice = random.choice(selecter)
#print the choice
print(f"\nYou chose {playerChoice}, computer chose {computerChoice}.\n")


#introduce a loop

while True :


    if playerChoice == computerChoice:
        print(f"Both players selected {playerChoice}. It's a tie!")
    elif playerChoice == "rock":
     if computerChoice == "scissors":
        print("You win!")
        playerWins+=1
     else:
         print("You lose.")
         computerWins+=1
    elif playerChoice == "paper":
        if computerChoice == "rock":
          print("You win!")
          playerWins+=1
        else:
            print("You lose.")
            computerWins+=1
    elif playerChoice == "scissors":
        if computerChoice == "paper":
         print("You win!")
         playerWins+=1
        else:
            print("You lose.")
            computerWins+=1
    print("You have "+str(playerWins)+" wins")
    print("The computer has "+str(computerWins)+" wins")


    #check if user will play again
    repeat = input("\nPlay again? (yes/no): ")
    if repeat.lower() != "no":
        print("Thanks for playing!")
    break
    
#check who won
    if playerWins == scoreMax:
         print("you u won")
     

    elif computerWins == scoreMax:
        print("the computer won, better luck next time")

    break