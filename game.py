board = ['-', '-', '-', 
        '-', '-', '-', 
        '-', '-', '-']

navigator = [1, 2, 3, 
            4, 5, 6, 
            7, 8, 9]


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def display_navigator():
    print(navigator[0] , " | " , navigator[1] , " | " , navigator[2])
    print(navigator[3] , " | " , navigator[4] , " | " , navigator[5])
    print(navigator[6] , " | " , navigator[7] , " | " , navigator[8])

display_board()
display_navigator()