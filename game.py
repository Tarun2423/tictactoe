import random
board=['-','-','-',
       '-','-','-',
       '-','-','-',]
currentplayer='X'
winner=None
gameRunning=True
def printBoard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----------") 
    print(board[6]+" | "+board[7]+" | "+board[8])
def playerInput(board):
        n=int(input("Enter any number between 1 To 9 : "))
        if(n>=1 and n<=9 and board[n-1]=="-"):
            board[n-1]=currentplayer
        else:
            print("Choose different option")
            n=int(input("Enter any number between 1 To 9 : "))
            if(n>=1 and n<=9 and board[n-1]=="-"):
                board[n-1]=currentplayer
def checkWin(board):
    if(checkHorizontal(board) or checkDiag(board) or checkVertical(board)):
        print(f"The Winner is {winner}")
def checkHorizontal(board):
    global winner
    if(board[0]==board[1]==board[2] and board[1]!="-"):
        winner=board[0]
        return True
    elif(board[3]==board[4]==board[5] and board[4]!="-"):
        winner=board[3]
        return True
    elif(board[6]==board[7]==board[8] and board[1]!="-"):
        winner=board[6]
        return True
def checkVertical(board):
    global winner
    if(board[0]==board[3]==board[6] and board[3]!="-"):
        winner=board[0]
        return True
    elif(board[1]==board[4]==board[7] and board[7]!="-"):
        winner=board[1]
        return True
    elif(board[2]==board[5]==board[8] and board[2]!="-"):
        winner=board[2]
        return True
def checkDiag(board):
    global winner
    if(board[0]==board[4]==board[8] and board[4]!="-"):
        winner=board[0]
        return True
    elif(board[2]==board[4]==board[6] and board[4]!="-"):
        winner=board[2]
        return True
def checkTie(board):
    global gameRunning
    if "-" not in board and checkWin(board)==False:
        printBoard(board)
        print("It's a tie")
        gameRunning=False
def switchPlayer():
    global currentplayer
    if currentplayer=="X":
        currentplayer="O"
    else:
        currentplayer="X"
def computer(board):
    global currentplayer
    while(currentplayer=="O"):
        position=random.randint(0,8)
        if(board[position]=="-"):
            board[position]=currentplayer
            switchPlayer()
while(gameRunning):
    printBoard(board)
    playerInput(board)
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)
    
        

