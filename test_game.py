import tic_tac_toe_1d           

def test_move_board_length(): #testing the length of the board, it should be 20 '-'
    board = tic_tac_toe_1d.move('--------------------', 'x', 2) #board, mark, position of the mark
    assert len(board) == 20
    

def test_move_dash_count(): #testing that after n move, the remaining empty positions are correct
    board = tic_tac_toe_1d.move('--------------------', 'x', 7)
    assert board.count('-') == 19


def test_move_mark_count(): #testing the number of specific marks on the board
    board = tic_tac_toe_1d.move('--------------------', 'x', 3)
    assert board.count('x') == 1


def test_move_mark_position(): #testing the position of the mark
    board = tic_tac_toe_1d.move ('--------------------', 'x', 1)
    assert board[1] == 'x'


