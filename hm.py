import time
import random

# Welcoming the user
name = input("What is your name? ")

print("Hello, " + name + ". Time to play Guess Game!")
print("Remember that each round you have 5 chances with a 1-minute time limit, and only if you score more than 2, you can move to the next level")

# Wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

words_and_clues = {
    "malware": "A malicious software that damages or gets unauthorized access to your network",
    "worm": "Malware that can reproduce itself for the purposes of spreading itself to other computers in the network. ",
    "firewall": "Any technology, be it software or hardware, used to keep intruders out.",
    "encryption": "Cypher code used to protect your information from hackers.",
    "hacking": "Gaining unauthorized access to your computer and later take your information"
}

score = 0
total_turns = 7
round_time = 60  # in seconds
rounds = 5

# Create a for loop for the rounds
for round in range(1, rounds + 1):
    print(f"\n--- Round {round} ---")

    # Select a random word and clue from the dictionary
    word, clue = random.choice(list(words_and_clues.items()))
    words_and_clues.pop(word)

    # Variables for the current round
    guesses = ""
    turns = total_turns
    start_time = time.time()
    timer_expired = False

    # Generate dashes based on word length
    dashes = "_" * len(word)

    # Display the number of letters in the word and the clue
    print("The word has", len(word), "letters.")
    print("Clue:", clue)
    
    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("\nCongratulations! You won the round!")
            score += 1
            break

        guess = input("\nGuess a character: ")
        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", turns, "more guesses")

        elapsed_time = time.time() - start_time
        remaining_time = round_time - int(elapsed_time)
        if remaining_time <= 0:
            print("\nTime's up!")
            break
        else:
            print("Time remaining:", remaining_time, "seconds")

        if remaining_time <= 10 and not timer_expired:
            timer_expired = True
            print("Hurry up! Only 10 seconds left!")

    if round < rounds and remaining_time > 0:
        print("\nNext round:")
    elif round == rounds:
        print("\nGame Over")

    if remaining_time > 0:
        time.sleep(1)  # Delay for 1 second before moving to the next question

# Check the final result based on score
if score > 2:
    print("Congratulations! You've passed this game. See you in the next level")
else:
    print("UH OOH!, You've lost to the hacker.. Sorry, you are out of the game")
