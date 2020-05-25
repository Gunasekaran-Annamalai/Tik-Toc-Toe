class game_begins:
    x_name = input('Enter \'X\' name:')
    O_name = input('Enter \'O\' name:')

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
            limit_checker_1 = True
            while(limit_checker_1):
                x_decision = int(input('Enter any number : '))
                if(x_decision <= 9):
                    print("Something")
        player_x()

        def player_o():
            print('\'O\' turn...')
            x_decision = int(input('Enter any number : '))
        player_o()

obj = game_begins()
obj.game_starts()