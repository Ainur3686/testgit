import tic_tac_toe_1d

def test_move_to_empty_space():
    board = tic_tac_toe_1d.move('--------------------', 'x', 2)
    assert len(board) == 20
    assert board.count('x') == 1
    assert board.count('-') == 19
    assert board[2] == 'x'

print('This file')
