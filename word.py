import random
import time
import threading
import sys

# List of words for the puzzle
words = ["cyber", "ddos-attack", "phishing", "social engineering", "malware", "hacker", "cryptography", "man-in-the-middle", "vulnerability", "rootkit"]

def choose_word(words):
    # Randomly select a word from the list
    return random.choice(words)

def jumble_word(word):
    # Randomly shuffle the characters in the word
    jumbled = list(word)
    random.shuffle(jumbled)
    return ''.join(jumbled)

def play_game():
    print("Welcome to the Word Puzzle Game!")

    score = 0  # Player's score
    remaining_words = words.copy()  # Copy of the words list

    for round_num in range(1, 11):  # Ten rounds
        if not remaining_words:
            print("No more words to guess!")
            break

        chosen_word = choose_word(remaining_words)
        remaining_words.remove(chosen_word)  # Remove the chosen word
        jumbled_word = jumble_word(chosen_word)

        print("\nRound {}: Unscramble the letters to form a word.".format(round_num))
        print("Jumbled word:", jumbled_word)

        start_time = time.time()  # Start the timer
        attempts = 3  # Number of attempts for each round

        def timer():
            remaining_time = 20
            while remaining_time > 0:
                sys.stdout.write("\rRemaining time: {:.1f} seconds".format(remaining_time))
                sys.stdout.flush()
                time.sleep(1)
                elapsed_time = time.time() - start_time
                remaining_time = max(20 - elapsed_time, 0)
            sys.stdout.write("\r")  # Clear the remaining time display
            sys.stdout.flush()

        timer_thread = threading.Thread(target=timer)
        timer_thread.start()

        while True:
            guess = input("\nEnter your guess:\n ")

            elapsed_time = time.time() - start_time  # Calculate the elapsed time
            remaining_time = 20 - elapsed_time  # Calculate the remaining time

            if remaining_time <= 0:
                print("Time's up!")
                break

            if guess == chosen_word:
                print("\nCorrect!")
                score += 1
                break
            else:
                print("Incorrect guess. Try again.")
                attempts -= 1
                print("Remaining attempts:", attempts)

            if attempts <= 0:
                print("Out of attempts!")
                break

        print("\nYour score:", score)

    # Wait for the last timer thread to complete
    if timer_thread is not None:
        timer_thread.join()

    print("\nThank you for playing!")

    if score >= 6:
        print("Congratulations! You can go to the next level.")
    else:
        print("Sorry! Your journey ends here.")

# Start the game
play_game()
