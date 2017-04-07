from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#Everything from here on should go in your for loop!
# Be sure to indent four spaces!
def guess(item):
    time=0
    guess_item=0
    while time==0:
        try:
            guess_item = int(raw_input("guess %s :" %(item)))
        except ValueError:
            print"your input is illegal,please try again"
            time=0
        else:
            time=1
            print "guess",item," input right"
            return guess_item
#main
turn=0
while turn < 4:
    #guess_row = guess_roww()#函数名定义相同 int定义了guess_row，报错
    #guess_col = guess_coll()
    guess_row=guess("row")
    guess_col=guess("col")
    print guess_row
    print guess_col
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        print "Turn", turn         
        print_board(board)
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
            turn+=1
        print "Turn", turn         
        print_board(board)
        if turn == 4:
            print "Game Over"
            print "the real location of my battleship: "
            print "ship_row:",ship_row
            print "ship_col:",ship_col