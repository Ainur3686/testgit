#Step1. Write a function 'evaluate' that accepts the string with the board as argument, returns one character 
def evaluate(board):
    #Returns the character based on the status of the game
    if "xxx" in board:
        return "x"
    elif "ooo" in board:
        return "o"
    elif "-" not in board:
        return "!"
    else:
        return "-"

#Step2. Write a 'move' function (accepts the string with the board, a position (0-19) and mark(x or o), returns a board)
def move(board, mark, position):
    #Returns the game board with the given mark in the given position
    #splicing the substring from 'start position' up to the 'position'
    #concatinating the 'mark'
    #concatinating the rest of the board, excluding the position of the 'mark'
    #updating the board
    board = board[0:position]+ mark + board[position + 1:]
    #returning the updated board
    return board

#Step3. Created a 'player_move' function (board, asks position), returns the updated board. 
def player_move(board):
    #Returns a game board with the player's move
    mark = "x"

    #Create an infinite loop
    while True:
        #asking player's position, and converting to integer
        position = int(input("Which position do you want to play?: "))

        #checking if the position in range of the board and not occupied
        if position in range(0, len(board)) and board[position] == "-":
            #using the 'move' function to put 'mark' on the selected 'position'
            #return the updated board and terminating the 'while' loop
            return move(board, mark, position)
        
#Step4. Created a 'pc_move' function(board with a selected position), returns updated board.
def pc_move(board):
   #Returns a game board with the computer's move
   mark = "o"
   
   while True:
        from random import randrange
        position=randrange(0,20) #positions: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
        #selecting random 'position' from 0 to 19
        if position in range(0, len(board)) and board[position] == "-":
            #using the 'move' function to put pc_move ('mark') on the selected random 'position'
            return move(board, mark, position)   #return the updated board  
        
#Step 5. Created OneD_tictactoe function which creates a board and alternately calls for the 'player' or 'pc' moves, returns updated board until someone wins or draw.
def OneD_tictactoe():
    board="-"*20
    print(board)
    while True:
        board=player_move(board)
        print(board)
        if evaluate(board) !="-":
           break
        board=pc_move(board)
        print(board)
        if evaluate(board) != "-":
           break


if __name__ == "__main__":
    OneD_tictactoe()