import random
from pywebio.input import input, select
from pywebio.output import put_text, put_html, put_buttons, put_markdown
from pywebio.platform.flask import start_server

# Level 1
def level1():
    choices = ["rock", "paper", "scissors"]
    scores = {"player": 0, "hacker": 0}

    def round(player_choice, hacker_choice):
        # ... existing code ...

    def game():
        # ... existing code ...

        if scores["player"] > scores["hacker"]:
            put_text("Congratulations! You've passed Level 1!")
            level2()  # Redirect to Level 2
        else:
            put_text("Oh no! You have been defeated by the hacker! Game Over")

    start_server(game, port=8088)

# Level 2
def level2():
    # ... existing code ...

    def play_guess_game():
        # ... existing code ...

        if score > 2:
            put_text("Congratulations! You've passed Level 2!")
            level3()  # Redirect to Level 3
        else:
            put_text("Uh oh! You've lost to the hacker. Game Over")

    start_server(play_guess_game, port=9190)

# Level 3
def level3():
    # ... existing code ...

    def game():
        # ... existing code ...

        if runs_p1 > runs_p2:
            put_text("Congratulations! You've passed Level 3!")
            level4()  # Redirect to Level 4
        else:
            put_text("Uh oh! The Hacker has won the match. Game Over")

    start_server(game, port=8100)

# Level 4
def level4():
    # ... existing code ...

    def play():
        # ... existing code ...

        if score > 3:
            put_text("Congratulations! You've passed Level 4!")
            level5()  # Redirect to Level 5
        else:
            put_text("Oh no! You've lost to the hacker. Game Over")

    start_server(play, port=9250)

# Level 5
def level5():
    # ... existing code ...

    def game():
        # ... existing code ...

        if player_score > computer_score:
            put_text("Congratulations! You've passed Level 5!")
            put_text("You've completed all levels! Game Over")
        else:
            put_text("Oops! The hacker has outsmarted you. Game Over")

    start_server(game, port=8300)

# Start the game at Level 1
level1()
