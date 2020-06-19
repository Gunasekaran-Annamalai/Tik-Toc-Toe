class game_begins:
    def __init__(self, x, o):
        self.x_name = x
        self.o_name = o
        # just for some empty lines
        print("")
        print("")
        self.board = ['-', '-', '-', 
                    '-', '-', '-', 
                    '-', '-', '-']
        
        print("--------------Game Navigator-------------")
        print("Choose any place in between 1-9:")
        print()

        print('------------Game Begins-------------\n')

    def display_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2] + "   " + "1 | 2 | 3")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5] + "   " + "4 | 5 | 6")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8] + "   " + "7 | 8 | 9")

    def X_turn(self):
        choice_1 = int(input("Enter the place to change into \'X\'"))
        game.player_X(choice_1)

    def O_turn(self):
        choice_2 = int(input("Enter the place to change into \'O\'"))
        game.player_O(choice_2)

    def player_X(self, place):
        if self.board[place-1] == '-':
            self.board[place-1] = 'x'
            game.display_board()
        elif self.board[place-1] == 'x':
            game.X_turn()
        else:
            game.display_board()
        game.X_checker()
    
    def player_O(self, place):
        if self.board[place-1] == '-':
            self.board[place-1] = 'o'
            game.display_board()
        elif self.board[place-1] == 'o':
            game.O_turn()
        else:
            game.display_board()
        game.O_checker()

    def X_checker(self):
        if ((self.board[0] == 'x' and self.board[1] == 'x' and self.board[2] == 'x') or 
            (self.board[3] == 'x' and self.board[4] == 'x' and self.board[5] == 'x') or 
            (self.board[6] == 'x' and self.board[7] == 'x' and self.board[8] == 'x')):
            print(self.x_name + " won the game")
            exit()
        elif ((self.board[0] == 'x' and self.board[4] == 'x' and self.board[8] == 'x') or 
            (self.board[2] == 'x' and self.board[4] == 'x' and self.board[6] == 'x')):
            print(self.x_name + " won the game")
            exit()
        elif ((self.board[0] == 'x' and self.board[3] == 'x' and self.board[6] == 'x') or 
            (self.board[1] == 'x' and self.board[4] == 'x' and self.board[7] == 'x') or 
            (self.board[2] == 'x' and self.board[5] == 'x' and self.board[8] == 'x')):
            print(self.x_name + " won the game")
            exit()
        elif (self.board[0] != '-' and self.board[1] != '-' and self.board[2] != '-' and
            self.board[3] != '-' and self.board[4] != '-' and self.board[5] != '-' and
            self.board[6] != '-' and self.board[7] != '-' and self.board[8] != '-'):
            print("Game draw")
            exit()

    def O_checker(self):
        if ((self.board[0] == 'o' and self.board[1] == 'o' and self.board[2] == 'o') or 
            (self.board[3] == 'o' and self.board[4] == 'o' and self.board[5] == 'o') or 
            (self.board[6] == 'o' and self.board[7] == 'o' and self.board[8] == 'o')):
            print(self.o_name + " won the game")
            exit()
        elif ((self.board[0] == 'o' and self.board[4] == 'o' and self.board[8] == 'o') or 
            (self.board[2] == 'o' and self.board[4] == 'o' and self.board[6] == 'o')):
            print(self.o_name + " won the game")
            exit()
        elif ((self.board[0] == 'o' and self.board[3] == 'o' and self.board[6] == 'o') or 
            (self.board[1] == 'o' and self.board[4] == 'o' and self.board[7] == 'o') or 
            (self.board[2] == 'o' and self.board[5] == 'o' and self.board[8] == 'o')):
            print(self.o_name + " won the game")
            exit()
        elif (self.board[0] != '-' and self.board[1] != '-' and self.board[2] != '-' and
            self.board[3] != '-' and self.board[4] != '-' and self.board[5] != '-' and
            self.board[6] != '-' and self.board[7] != '-' and self.board[8] != '-'):
            print("Game draw")
            exit()

    def draw(self):
            if (self.board[0] != '-' and self.board[1] != '-' and self.board[2] != '-' and
            self.board[3] != '-' and self.board[4] != '-' and self.board[5] != '-' and
            self.board[6] != '-' and self.board[7] != '-' and self.board[8] != '-'):
                print("game draw")
                exit()

x = input('Enter \'X\' name:')
o = input('Enter \'O\' name:')

game = game_begins(x, o)
game.display_board()

while True:
    game.X_turn()
    game.O_turn()
