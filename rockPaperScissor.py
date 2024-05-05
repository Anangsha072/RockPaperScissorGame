import tkinter as tk
import random

def play_game(user_choice):
    if user_choice >= 3 or user_choice < 0:
        result_label.config(text="You entered an invalid choice. You lose.")
        return

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.randint(0, 2)
    computer_choice_label.config(text="Computer's choice: " + choices[computer_choice])

    if computer_choice == user_choice:
        result_label.config(text="It's a draw!")
    elif (computer_choice == 0 and user_choice == 2) or \
         (computer_choice == 1 and user_choice == 0) or \
         (computer_choice == 2 and user_choice == 1):
        result_label.config(text="You lose!")
    else:
        result_label.config(text="You win!")

# Create the GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Label for result
result_label = tk.Label(root, text="")
result_label.pack()

# Label for computer's choice
computer_choice_label = tk.Label(root, text="")
computer_choice_label.pack()

# Buttons for player choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_game(0))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game(1))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game(2))
scissors_button.pack(side=tk.LEFT, padx=10)

root.mainloop()


