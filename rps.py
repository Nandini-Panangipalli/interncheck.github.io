import random

choices=["rock","paper","scissors"]
scores={"player": 0 , "hacker": 0}

def round(player_choice, hacker_choice):
    print("Your choice:", player_choice)
    print("Hacker's choice:", hacker_choice)

    if player_choice == hacker_choice:
        print("Both chose the same --> It's a TIE --> Try again")    

    elif (
        (player_choice == "rock" and hacker_choice == "scissors") or
        (player_choice == "paper" and hacker_choice == "rock") or
        (player_choice == "scissors" and hacker_choice == "paper")
    ):
        print("You Win a point :)... Keep it up")
        scores["player"] +=1

    else:
        print("The hacker has got the point :( .. Be careful")
        scores["hacker"] += 1


def game():
	print("""Hello Player! Welcome to Rock Paper and Scissors!
Beware of the Hacker!
The Hacker is too smart and can outplay you!""")

	while scores["player"]<5 and scores["hacker"]<5:
		print("The current scores are:")
		print("Your Score:",scores["player"] ,"and","Hacker's Score:",scores["hacker"])
		player_choice=input("Enter your choice--[rock/paper/scissors]: ").lower()
		if player_choice not in choices:
			print("This is an invalid choice---Please give a valid choice")
			continue

		hacker_choice=random.choice(choices)
		round(player_choice,hacker_choice)
		print()

	print("The Final Scores are:")
	print("Your Score:",scores["player"] ,"and","Hacker's Score:",scores["hacker"])
	if(scores["player"] > scores["hacker"]):
		print("Congratulations you've passed the second round!")
		print("Keep going on until you are the chief of general")

	else:
		print("Oh no! You have been attacked by the hacker!--Check your data!:(")

game()







