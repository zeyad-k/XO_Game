import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    """
    A class representing the Tic Tac Toe game.

    Attributes:
    - root: The root window of the game.
    - score: A dictionary to keep track of the score for each player.
    - current_player: A string representing the current player ('Player' or 'Computer').
    - board: A list representing the game board.
    - buttons: A 2D list of buttons representing the game board GUI.
    - restart_button: A button to restart the game.
    - score_label: A label to display the current score.

    Methods:
    - on_click: Handles the button click event.
    - computer_turn: Performs the computer's turn.
    - check_winner: Checks if there is a winner.
    - highlight_winner: Highlights the winning combination on the GUI.
    - show_winner: Displays the winner or a draw message.
    - update_score: Updates the score for the given player.
    - restart_game: Restarts the game.
    - run: Runs the game loop.
    """

    def __init__(self, root):
        """
        Initializes the TicTacToe object.

        Parameters:
        - root: The root window of the game.
        """
        self.root = root
        self.root.title("Tic Tac Toe")

        self.score = {'Player': 0, 'Computer': 0}
        self.current_player = 'Player'
        self.board = [' ' for _ in range(9)]

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text=' ', font=('Arial', 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=3, column=1, pady=10)

        self.score_label = tk.Label(self.root, text="Score - Player: 0 | Computer: 0")
        self.score_label.grid(row=4, column=0, columnspan=3)

    def on_click(self, row, col):
        """
        Handles the button click event.

        Parameters:
        - row: The row index of the clicked button.
        - col: The column index of the clicked button.
        """
        index = 3 * row + col
        if self.board[index] == ' ':
            self.board[index] = 'X' if self.current_player == 'Player' else 'O'
            self.buttons[row][col].config(text=self.board[index], state='disabled')
            if self.check_winner('X'):
                self.update_score('Player')
                winning_combo = self.check_winner('X')
                self.highlight_winner(winning_combo)
                self.show_winner('Player')
                self.restart_game()
            else:
                if ' ' not in self.board:  # Check for a tie
                    self.show_winner('Draw')
                    self.restart_game()
                else:
                    self.current_player = 'Computer'
                    self.computer_turn()

    def computer_turn(self):
        """
        Performs the computer's turn.
        """
        empty_cells = [i for i, val in enumerate(self.board) if val == ' ']
        index = random.choice(empty_cells)
        self.board[index] = 'O'
        row, col = divmod(index, 3)
        self.buttons[row][col].config(text='O', state='disabled')
        if self.check_winner('O'):
            self.update_score('Computer')
            winning_combo = self.check_winner('O')
            self.highlight_winner(winning_combo)
            self.show_winner('Computer')
            self.restart_game()
        else:
            if ' ' not in self.board:  # Check for a tie
                self.show_winner('Draw')
                self.restart_game()
            else:
                self.current_player = 'Player'

    def check_winner(self, symbol):
        """
        Checks if there is a winner.

        Parameters:
        - symbol: The symbol to check for a win ('X' or 'O').

        Returns:
        - The winning combination if there is a winner, None otherwise.
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if all(self.board[i] == symbol for i in combo):
                return combo  # Return the winning combination
        return None

    def highlight_winner(self, combo):
        """
        Highlights the winning combination on the GUI.

        Parameters:
        - combo: The winning combination.
        """
        for index in combo:
            row, col = divmod(index, 3)
            self.buttons[row][col].config(bg='red')  # Change background color of winning buttons

    def show_winner(self, winner):
        """
        Displays the winner or a draw message.

        Parameters:
        - winner: The winner or 'Draw' if it's a draw.
        """
        if winner == 'Draw':
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            messagebox.showinfo("Game Over", f"{winner} wins!")

    def update_score(self, player):
        """
        Updates the score for the given player.

        Parameters:
        - player: The player to update the score for ('Player' or 'Computer').
        """
        self.score[player] += 1
        self.score_label.config(text=f"Score - Player: {self.score['Player']} | Computer: {self.score['Computer']}")

    def restart_game(self):
        """
        Restarts the game.
        """
        self.current_player = 'Player'
        self.board = [' ' for _ in range(9)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', state='normal', bg='SystemButtonFace')  # Reset button style

    def run(self):
        """
        Runs the game loop.
        """
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    game.run()
