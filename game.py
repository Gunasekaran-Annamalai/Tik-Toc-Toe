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
        print(1, "|", 2, "|", 3)
        print(4, "|", 5, "|", 6)
        print(7, "|", 8, "|", 9)

        print('------------Game Begins-------------\n')

    def display_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def player_X(self, place):
        if self.board[place] == '-':
            self.board[place] = 'x'
        game.display_board()
    
    def player_O(self, place):
        self.board[place] = 'o'
        game.display_board()

x = input('Enter \'X\' name:')
o = input('Enter \'O\' name:')

game = game_begins(x, o)
game.display_board()

for i in range(1, 10):
    print(i)
    choice_1 = int(input("Enter the place to change into \'X\'"))
    game.player_X(choice_1)
    choice_2 = int(input("Enter the place to change into \'O\'"))
    game.player_O(choice_2)
    


    # def navigator(self):
    #     self.board[3] = 'x'
        
    # def player_x(self):
    #     print('\'X\' turn...')
    #     limit_checker = True
    #     while(limit_checker):
    #         decision = int(input('Enter any number : '))
    #         if(decision <= 9 and decision > 0):
    #             limit_checker = False
    #             self.board[2] = 'x'
    #             print(self.board[2])
    #         else: print("Error enter correct choice")

    # def player_o(self):
    #     print('\'O\' turn...')
    #     limit_checker = True
    #     while(limit_checker):
    #         decision = int(input('Enter any number : '))
    #         if(decision <= 9 and decision > 0):
    #             limit_checker = False
    #         else: print("Error enter correct choice")

    # def check_diagonals(self):
    #     self.board[0] == 'x'
    #     print(self.board[0])
    #     if(self.board[0] == self.board[1] == self.board[2]):
    #         if(self.board[0] == 'x'): print(self.x_name+" won the game")
    #         else: print("o won the game")


