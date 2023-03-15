# In this project I will be building the popular Tic Tac Toe game using the Classes Concepts in Python

#Imports
import random

# Creating the game class
class game:

    # the game board
    def __init__(self):
        self.board = []

    #define the dimentions of the board
    def create_board(self):
        for i in range(3):
            row = []

            for j in range(3):
                row.append('-')
            self.board.append(row)

    # Prompt player
    def get_first_player(self):
        return random.randint(0, 1)

    # fix the player in the game
    def fix_game(self, row, col, player):
        self.board[row][col] = player

    # check the win
    def get_winner(self, player):

        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True

            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
                if win:
                    return win
                
        # checking colums
        for i in range(n):
            win = True

            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
                if win:
                    return win
                
        # Checking Diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
            if win:
                return win
            
        win = True
        for i in range(n):
            if self.board[i][n-1-i] != player:
                win = False
                break
            if win:
                return win
        return False
        
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True
    
    # check if board is full
    def is_board_full(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True
    
    # Swap Players
    def swap_player(self, player):
        return 'X' if player == 0 else 0
    
    # check if board is full
    def show_board (self):
        for row in self.board:
            for item in row:
                print(item, end="")
            print()

    # the start of the game
    def start(self):
        self.create_board()

        player = 'X' if self.get_first_player() == 1 else '0'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # getting user iput
            row, col = list(map(int, input("Enter Number to Fix Spot: ").split()))
            print()

            # fixing the input spot
            self.fix_game(row - 1, col - 1, player)

            # checking for the winner
            if self.get_winner(player):
                print(f"The winner is {player}")
                break

            #checking for a draw
            if self.is_board_full():
                print("Match is a draw")
                break
            # swap players
            player = self.swap_player()

        #show final board view
        print()
        self.show_board()

#start game
tic_tac_toe = game()
tic_tac_toe.start()




        