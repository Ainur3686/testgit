import tic_tac_toe_1d

def test_move_board_length():
    board = tic_tac_toe_1d.move('--------------------', 'x', 2)
    assert len(board) == 20
    

def test_move_dash_count():
    board = tic_tac_toe_1d.move('--------------------', 'x', 7)
    assert board.count('-') == 19


def test_move_mark_count():
    board = tic_tac_toe_1d.move('--------------------', 'x', 3)
    assert board.count('x') == 1


def test_move_mark_position():
    board = tic_tac_toe_1d.move ('--------------------', 'x', 1)
    assert board[1] == 'x'


