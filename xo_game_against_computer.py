import tkinter as tk
import random

 
player =  "X"
player_score = 0
computer_score = 0
game_buttons =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
 

def next_turn(row, col):
    """
    Function to handle the next turn in the game.
    It updates the game board with the player's move and checks for a winner.

    Parameters:
    - row (int): The row index of the button clicked.
    - col (int): The column index of the button clicked.
    """
    global player, player_score

    if game_buttons[row][col]['text'] == "" and check_winner() == False:
        game_buttons[row][col]['text'] = player
        if check_winner() == True:
            label_result.config(text=(player + ' : Player Wins! '))
            player_score += 1
            label_player_score.config(text=(player_score))
        elif check_winner() == 'tie':
            label_result.config(text=(' It`s a Tie, No Winner ! '))
        else:
            player = "O"
            computer_move()

def computer_move():
    """
    Function to handle the computer's move in the game.
    It uses a simple AI algorithm to make a move:
    - If there's a winning move, take it.
    - If the player has a winning move, block it.
    - Otherwise, move randomly.
    """
    global player, computer_score

    for row in range(3):
        for col in range(3):
            if game_buttons[row][col]['text'] == "":
                game_buttons[row][col]['text'] = player
                if check_winner() == True:
                    label_result.config(text=(player + ' : Computer Wins! '))
                    computer_score += 1
                    label_computer_score.config(text=(computer_score))
                    return
                game_buttons[row][col]['text'] = ""

    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if game_buttons[row][col]['text'] == "":
            game_buttons[row][col]['text'] = player
            if check_winner() == 'tie':
                label_result.config(text=(' It`s a Tie, No Winner ! '))
            player = "X"
            break

def check_winner():
    """
    Function to check if there is a winner in the game.
    It checks all possible winning conditions: horizontal, vertical, and diagonal.

    Returns:
    - True if there is a winner.
    - 'tie' if it's a tie game.
    - False if there is no winner yet.
    """
    for row in range(3):
        if game_buttons[row][0]['text'] == game_buttons[row][1]['text'] == game_buttons[row][2]['text'] != "":
            game_buttons[row][0].config(bg="cyan")
            game_buttons[row][1].config(bg="cyan")
            game_buttons[row][2].config(bg="cyan")
            return True

    for col in range(3):
        if game_buttons[0][col]['text'] == game_buttons[1][col]['text'] == game_buttons[2][col]['text'] != "":
            game_buttons[0][col].config(bg="cyan")
            game_buttons[1][col].config(bg="cyan")
            game_buttons[2][col].config(bg="cyan")
            return True 

    if game_buttons[0][0]['text'] == game_buttons[1][1]['text'] == game_buttons[2][2]['text'] != "":
        game_buttons[0][0].config(bg="cyan")
        game_buttons[1][1].config(bg="cyan")
        game_buttons[2][2].config(bg="cyan")
        return True 
    elif game_buttons[0][2]['text'] == game_buttons[1][1]['text'] == game_buttons[2][0]['text'] != "":
        game_buttons[0][2].config(bg="cyan")
        game_buttons[1][1].config(bg="cyan")
        game_buttons[2][0].config(bg="cyan")
        return True     

    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_buttons[row][col].config(bg='red')
        return 'tie'  
    else:
        return False

def check_empty_spaces():
    """
    Function to check if there are any empty spaces left on the game board.

    Returns:
    - True if there are empty spaces.
    - False if there are no empty spaces.
    """
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_buttons[row][col]['text'] != '':
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def start_new_game():
    """
    Function to start a new game.
    It resets the game board, chooses a random player to start, and clears the result label.
    """
    global player
    player ="X"

    label_result.config(text="")

    for row in range(3):
        for col in range(3):
            game_buttons[row][col].config(text="", bg="#f0f0f0")

def on_button_click(button):
    """
    Function to handle button click event.
    Currently, it sets the text of the clicked button to "X".

    Parameters:
    - button (tkinter.Button): The button that was clicked.
    """
    button.config(text="X")

# Create a window
root = tk.Tk()
root.title("XO Game")
root.configure(bg='#f0f0f0')  # Set background color

# Label for the player score 
label_player = tk.Label(root, text="Player :", bg='#f0f0f0', font=("Arial", 12))
label_player.grid(column=0, row=0, padx=15, pady=10, sticky='w')
label_player_score = tk.Label(root, text="", bg='#f0f0f0', font=("Arial", 12))
label_player_score.grid(column=1, row=0, sticky='w')

# Label for the computer score 
label_computer = tk.Label(root, text="Computer :", bg='#f0f0f0', font=("Arial", 12))
label_computer.grid(column=2, row=0, padx=15, pady=10, sticky='w')
label_computer_score = tk.Label(root, text="", bg='#f0f0f0', font=("Arial", 12))
label_computer_score.grid(column=3, row=0, sticky='w')

# Label to announce the winner
label_result = tk.Label(root, text=" ", bg='#f0f0f0', font=("Arial", 14, 'bold'))
label_result.grid(column=0, columnspan=3, row=1, padx=15, pady=10, sticky='w')

# Button to restart the game
restart_button = tk.Button(root, text="Restart", relief=tk.RAISED, command=start_new_game, bg='#4CAF50', fg='white', font=("Arial", 10, 'bold'))
restart_button.grid(column=1, row=2, padx=10, pady=10)

# Buttons of the game 
buttons = []
for row in range(3):
    for col in range(3):
        game_buttons[row][col] = tk.Button(root, text="", relief=tk.RAISED, width=8, height=4, font=("Arial", 12, 'bold'),
                                           command=lambda row=row, col=col: next_turn(row, col))
        game_buttons[row][col].grid(column=col, row=row + 3, padx=5, pady=5)

root.mainloop()
