# To play Tic-Tac-Toe, type `python3 ttt.py` in the command line (without the backquotes) and hit Enter.

import sys

# Tic-Tac-Toe 
class ttt:
    def __init__(self):                                           # Constructor
        self.board = list();                                      # Initialize board array
        for i in range (0,9):
            self.board.append('e')                                # Fill board array with 'e' to signify empty
        self.character_map = {'e': ' ', '0': '0', 'X': 'X'}       # Print blank wherever 'e'
        self.num_turns = 0                                        # Initialize number of turns
        self.players = ('0', 'X')                                 # Fixed array for 'Os and Xs representing players'
        self.player = self.players[0]                             # Initialize Player to be O
        
    def play(self):                                               # Method to play the game: Function inside a class
        welcome_message = ("Hello! This is tic-tac-toe, a two player game "
                            "played between player 0 and player X. "
                            "The game is played in a 3 x 3 matrix. Each cell of the matrix has an index from 1-9. "
                            "Row one has cells 1, 2 and 3. "
                            "Row one has cells 4, 5 and 6. "
                            "Row one has cells 7, 8 and 9. "
                            "The game starts with player 0 selecting an index followed by player X, followed by player 0 and so on. "
                            "The game stops when one of the two players win or when the game is a draw.")
        print(welcome_message)
        self.print_board()
        while True:            
            self.user_choice = self.get_input()                 
            self.fill_array(self.user_choice, self.player)
            self.print_board()
            if self.check_winner(self.player):
                print(f'{self.player} won the game!')
                sys.exit()
                pass
            elif self.board.count('e') == 0:
                print(f"It's a draw!")
                sys.exit()
                pass
            
            if self.num_turns % 2 == 0:
                self.player = self.players[1]
            else:
                self.player = self.players[0]
            self.num_turns += 1
            pass
        pass
    
    # Method 1: User Choice that makes use of valid choice
    # returns true if user_choice is an integer in range [0,8] and 
    # if user_choice hasn't been selected before.
    def valid_choice(self, user_choice):              
        if  user_choice >= 1 and \
            user_choice <= 9 and \
            self.board[user_choice-1] == 'e':
            return True
        return False
    
    def get_input(self):   #Get User Input
        is_valid_choice = False
        while not is_valid_choice:
            try:
                user_choice = int(input(f"Player {self.player}'s turn. Enter a number between 1 and 9 (inclusive) that has not been entered before:"))
                is_valid_choice = self.valid_choice(user_choice)
            except ValueError:
                print("Error! Input should be an integer.")
                is_valid_choice = False
        return user_choice - 1
    
    # Method 2: Fill_array 
    def fill_array(self, user_choice, player):
        self.board[user_choice] = player
        pass
     
    # Method 3: Print_Board
    # returns printed board
    def print_board(self):
        print("\n")
        print(self.character_map[self.board[0]], '|', self.character_map[self.board[1]], '|', self.character_map[self.board[2]])
        print('-'* 10)
        print(self.character_map[self.board[3]], '|', self.character_map[self.board[4]], '|', self.character_map[self.board[5]])
        print('-'* 10)
        print(self.character_map[self.board[6]], '|', self.character_map[self.board[7]], '|', self.character_map[self.board[8]])
        print("\n")
        pass
    
    # Method 4: Check_Winner
    # returns Winner
    def check_winner(self, player):
        if  (self.board[0] == self.board[1] == self.board[2] == player) or \
            (self.board[3] == self.board[4] == self.board[5] == player) or \
            (self.board[6] == self.board[7] == self.board[8] == player) or \
            (self.board[0] == self.board[3] == self.board[6] == player) or \
            (self.board[1] == self.board[4] == self.board[7] == player) or \
            (self.board[2] == self.board[5] == self.board[8] == player) or \
            (self.board[0] == self.board[4] == self.board[8] == player) or \
            (self.board[2] == self.board[4] == self.board[6] == player):
            return True
        return False
    pass

if __name__ == "__main__":
    game = ttt()
    game.play()
    pass