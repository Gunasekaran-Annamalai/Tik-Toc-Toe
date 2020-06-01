class game_begins:
    x_name = input('Enter \'X\' name:')
    o_name = input('Enter \'O\' name:')

    # just for some empty lines
    print("")
    print("")


    def game_starts(self):
        self.board = ['-', '-', '-', 
                    '-', '-', '-', 
                    '-', '-', '-']
        print('------------Game Begins-------------\n')

    def display_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def navigator(self):
        print("--------------Game Navigator-------------")
        print("Choose any place in between 1-9:")
        print()
        print(1, "|", 2, "|", 3)
        print(4, "|", 5, "|", 6)
        print(7, "|", 8, "|", 9)
class game_play(game_begins):

    def player_x(self):
        print('\'X\' turn...')
        limit_checker = True
        while(limit_checker):
            decision = int(input('Enter any number : '))
            if(decision <= 9 and decision > 0):
                limit_checker = False
                self.board[2] = 'x'
                print(self.board[2])
            else: print("Error enter correct choice")

    def player_o(self):
        print('\'O\' turn...')
        limit_checker = True
        while(limit_checker):
            decision = int(input('Enter any number : '))
            if(decision <= 9 and decision > 0):
                limit_checker = False
            else: print("Error enter correct choice")

class game_winner(game_play, game_begins):
    def check_diagonals(self):
        self.board[0] == 'x'
        print(self.board[0])
        if(self.board[0] == self.board[1] == self.board[2]):
            if(self.board[0] == 'x'): print(self.x_name+" won the game")
            else: print("o won the game")

gameobj = game_winner()
gameobj.navigator()
gameobj.game_starts()
gameobj.display_board()
gameobj.player_x()
gameobj.player_o()
gameobj.check_diagonals()