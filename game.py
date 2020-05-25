class game_begins:
    x_name = input('Enter \'X\' name:')
    O_name = input('Enter \'O\' name:')

    # just for some empty lines
    print("")
    print("")

    print('Game Begins\n')
    def game_starts(self):
        board = ['-', '-', '-', 
                '-', '-', '-', 
                '-', '-', '-']

        def display_board():
            print(board[0] + " | " + board[1] + " | " + board[2])
            print(board[3] + " | " + board[4] + " | " + board[5])
            print(board[6] + " | " + board[7] + " | " + board[8])

        display_board()

        def navigator():
            print("Choose any place in between 1-9:")
        navigator()

        def player_x():
            print('\'X\' turn...')
            limit_checker = True
            while(limit_checker):
                decision = int(input('Enter any number : '))
                if(decision <= 9 and decision > 0):
                    limit_checker = False
                else: print("Error enter correct choice")

        def player_o():
            print('\'O\' turn...')
            limit_checker = True
            while(limit_checker):
                decision = int(input('Enter any number : '))
                if(decision <= 9 and decision > 0):
                    limit_checker = False
                else: print("Error enter correct choice")
        
        player_x()
        player_o()

obj = game_begins()
obj.game_starts()