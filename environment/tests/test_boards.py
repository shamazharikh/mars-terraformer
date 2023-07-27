"""
Test Board functionality
"""
from environment.mars_boards import BaseBoard


def test_base_board():
    """
    Test base board functionality
    """
    BaseBoard(board_name="base").print_board()


if __name__ == "__main__":
    test_base_board()
