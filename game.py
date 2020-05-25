class game_begins:
    user_x = input('Enter \'X\' name:')
    user_O = input('Enter \'O\' name:')

    # just for some empty lines
    for i in range(2):
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
            
        player_x()

        def player_o():
            print('\'O\' turn...')
        player_o()

obj = game_begins()
obj.game_starts()