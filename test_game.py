import tic_tac_toe_1d           

def test_move_board_length(): #testing the length of the board, it should be 20 '-'
    board = tic_tac_toe_1d.move('--------------------', 'x', 2) #board, mark, position of the mark
    assert len(board) == 20
    

def test_move_dash_count(): #testing that after n move, the remaining empty positions are correct
    board = tic_tac_toe_1d.move('--------------------', 'x', 7)
    assert board.count('-') == 19 #assert, which means if it is true, then pass it


def test_move_mark_count(): #testing the number of specific marks on the board
    board = tic_tac_toe_1d.move('--------------------', 'x', 3)
    assert board.count('x') == 1


def test_move_mark_position(): #testing the position of the mark
    board = tic_tac_toe_1d.move ('--------------------', 'x', 1)
    assert board[1] == 'x'

def test_evaluate_space():   #testing the empty space
   result = tic_tac_toe_1d.evaluate ('--------------------')
   assert result == '-' #assert, which means if it is true, if it is equal to the expected result, then pass it


def test_evaluate_winner_pc(): #testing if the pc is winner
    result = tic_tac_toe_1d.evaluate('-o-x-xx--o---ooo---x')
    assert result == 'o' #if we have 'ooo', the game returns 'o'


def test_evaluate_winner_player(): #testing if the player won
    result = tic_tac_toe_1d.evaluate('-x--xxx-oo-o---x--oo')
    assert result == 'x' #if we have 'xxx', the game returns 'x'

def test_evaluate_full(): #testing if the board is full, no empty space
   result = tic_tac_toe_1d.evaluate ('xooxooxoxoxoxxoxooxo')
   assert result == '!' #if we the board is full, but there are no 'ooo' or 'xxx', the game returns '!'

#a)	Python module
#It is a ready to use stored code, which you can import and use it immediately. There are built-in, third party or your own modules. 
#Python package: Package is a collection of specific type of modules. One big module might have submodules, which is called a package.

#b)	Exceptions are error messages detected when we run a code/program. If we encounter an unknown error, it is better to terminate the program.

#c)	By using following keywords, you are going to:\

#d)	By using keyword ‘raise’ followed by name of the exception and keyword Error. For example , ‘raise NameError’, ‘raise ValueError’ and etc.

#e)	Benefits of testing: Saving time when we work with long program/code. Checking thoroughly the program, cause manually we some errors can be missed 


