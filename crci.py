# Instructions
print(""" -------- Game of Cricket --------
 
Instructions to follow:
 
1. Any random number between 1 and 6 should be chosen by you.
2. Then the hacker also chooses a number. 
3.If you and the hacker chose different numbers when you hit, your number will be added to the run. 
  You lose the wicket if you and the hacker choose the same number.
4. In bowling, if you and the hacker chose different numbers, the computer's number will be added to the run. 
  If you and the hacker pick the same number, the hacker loses the wicket, similar to the previous rule.
5. You and Hacker will get 2 wickets and 2 overs with bat and bowling.
6. Here each over consists of  6 balls. This means that a player can throw a total of 12 balls in 2 overs.
7. The inning ends after the wickets have fallen or the over has ended.
8. The player with the most runs wins.""")

print("---------- Start Game ----------")

#importing random to get random input from the computer
import random
import pygame

# Initialize pygame
pygame.mixer.init()

# Load sound files
hit_sound = pygame.mixer.Sound('C:\\Users\\psvas\\OneDrive\\Desktop\\intership games\\internship\\Bat Hitting - Sound.mp3')
wicket_sound = pygame.mixer.Sound('C:\\Users\\psvas\\OneDrive\\Desktop\\intership games\\internship\\Wicket Fall - Commentary.mp3')
win_sound = pygame.mixer.Sound('C:\\Users\\psvas\\OneDrive\\Desktop\\intership games\\internship\\crowd-cheer-ii-6263.mp3')
loose_sound = pygame.mixer.Sound('C:\\Users\\psvas\\OneDrive\\Desktop\\intership games\\internship\\loose.mp3')

# Toss Time 
print("\n It's time for the Toss")
toss = (input("Choose heads or tails: ")).lower() #in lowercase

rand_toss = random.randint(1,2)            # In rand_toss (1 = Heads) and (2 = Tails) ------rand=random
rand_opt = random.randint(1,2)             # In rand_opt (1 = bat) and (2 = ball)

your_opt = 0          #your option that you chose
comp_opt = 0         #computer's option

#if-else to know if we won the toss and to choose bat or ball if we win the toss
if rand_toss == 1 and toss == "heads":
    print("\nCongratulations! You have won the toss...")
    your_opt = (input("Now choose to bat or ball: ")).lower()
elif rand_toss == 2 and toss == "tails":
    print("\nYou won the toss")
    your_opt = (input("Choose bat or ball: ")).lower()    
else:
    print("\nSorry! You have lost the toss...")
    # Computer chooses once you lost the toss
    if rand_opt == 1:
        comp_opt = "bat"
        print("Hacker chooses to bat")
        print("Now you have to ball!...All the best!")
    elif rand_opt == 2:
        comp_opt = "ball"
        print("Hacker chooses to ball")
        print("You have to bat!...All the best!")

# First Innings 
print("\n---------- First Innings Begins ----------")

runs_p1 = 0                       #Runs of the first player batting
wickets_p1 = 0                    #Wickets fallen down of the first team
balls_p1 = 0                      #balls starting from 1 to 12
 
while (wickets_p1 != 2 and balls_p1 != 12):
    your_choice = int(input("\nChoose any number from 1 to 6: "))
    comp_choice = random.randint(1,6)

    if (your_choice < 1 or your_choice > 6):
        print("\nPlease choose a value only from 1 to 6.")
    else:
        print("Your choice: ", your_choice, "\nHacker's choice: ", comp_choice)

        if (your_choice == comp_choice):
            wickets_p1 += 1
            wicket_sound.play()  # Play wicket sound effect
        else:
            if (your_opt == "bat" or comp_opt == "ball"):
                Bat_first = "You"
                Ball_first = "Hacker"
                runs_p1 += your_choice
            elif your_opt == "ball" or comp_opt == "bat":
                Bat_first = "Hacker"
                Ball_first = "You"
                runs_p1 += comp_choice
            hit_sound.play()  # Play hit sound effect

        print("\nScore =", runs_p1, "/", wickets_p1)

        balls_p1 += 1  #Incrementing the balls

        if (balls_p1 == 6):
            print("End of Over 1")
        elif (balls_p1 == 12):
            print("End of Over 2")

        print("Balls remaining:", 12 - balls_p1)

print("\n---------- End of First Innings ----------") 
print("\nFinal Score:")
print("Runs =", runs_p1)
print("Wickets =", wickets_p1)
print("Balls played =", balls_p1)

print("\n", Ball_first, "needs", runs_p1 + 1, "runs to win.")

# Second Innings (same as the first innings)
print("\n---------- Second Innings Begins ----------")

runs_p2 = 0
wickets_p2 = 0
balls_p2 = 0

while (wickets_p2 != 2 and balls_p2 != 12 and runs_p2 <= runs_p1):
    your_choice = int(input("\nChoose any number from 1 to 6: "))
    comp_choice = random.randint(1,6)

    if (your_choice < 1 or your_choice > 6):
        print("\nPlease choose a value only between 1 to 6.")
    else:
        print("Your choice: ", your_choice, "\nHacker's choice: ", comp_choice)

        if (your_choice == comp_choice):
            wickets_p2 += 1
            wicket_sound.play()  # Play wicket sound effect
        else:
            if Bat_first == "Hacker": 
                runs_p2 += your_choice
                Bat_second = "You"
            elif Bat_first == "You":
                runs_p2 += comp_choice
                Bat_second = "Hacker"
            hit_sound.play()  # Play hit sound effect

        print("\nScore =", runs_p2, "/", wickets_p2)

        balls_p2 += 1

        if (balls_p2 == 6):
            print("End of Over 1")
        elif (balls_p2 == 12):
            print("End of Over 2")

        if (runs_p2 <= runs_p1 and balls_p2 <= 11 and wickets_p2 != 2):
            print("To win:", runs_p1 - runs_p2 + 1, "runs needed from", 12 - balls_p2, "balls.")

print("\n---------- End of Second Innings ----------") 
print("\nFinal Score:")
print("Runs =", runs_p2)
print("Wickets =", wickets_p2)

# Result of Match 
print("\n------- Result -------")

if (runs_p1 > runs_p2):
    if Bat_first == "You":
        print("\nCongratulations! You won the Match by", runs_p1 - runs_p2, "runs.")
        win_sound.play()
    else:
        print("\nUh oh! The Hacker has won the Match by", runs_p1 - runs_p2, "runs.") 
        loose_sound.play()
elif runs_p2 > runs_p1:
    if Bat_second == "You":
        print("\nCongratulations! You won the Match by", wickets_p1 - wickets_p2, "wickets.")
        win_sound.play()
    else:
        print("\nUh oh! The Hacker has won the Match by", wickets_p1 - wickets_p2, "wickets.")
        loose_sound.play()
else:
    print("The Match is a Tie.","\nNo one Wins. Just Miss!")
    win_sound.play()

# Play win sound effect

