from conecta4.board import Board
from conecta4.oracle import ColumnRecommendation, BaseOracle, ColumnClassification
from conecta4.player import Player
from conecta4.oracle import SmartOracle
from conecta4.settings import BOARD_COLUMNS

def test_base_oracle():
    board = Board.fromList([[None, None, None, None],
                            ["x", "o", "x", "o"],
                            ["o", "o", "x", "x"],
                            ["o", None, None, None]])
    
    expected = [ColumnRecommendation(0, ColumnClassification.MAYBE),
                ColumnRecommendation(1, ColumnClassification.FULL),
                ColumnRecommendation(2, ColumnClassification.FULL),
                ColumnRecommendation(3, ColumnClassification.MAYBE)]
    
    rappel = BaseOracle()

    assert len(rappel.get_recommendation(board, None)) == len(expected)
    assert rappel.get_recommendation(board, None) == expected


def test_equality():
    cr = ColumnRecommendation(2, ColumnClassification.MAYBE)

    assert cr == cr #son identicos
    assert cr == ColumnRecommendation(2, ColumnClassification.MAYBE) #equivalentes

    #no equivalentes (puesto que no tienen la misma clasificacion)
    assert cr != ColumnRecommendation(2, ColumnClassification.FULL)
    assert cr != ColumnRecommendation(3, ColumnClassification.FULL)

def test_is_winning_move():
    winner = Player("Cucu", "x")
    loser = Player("otto", "o")

    empty = Board()
    almost = Board.fromList([["o", "x", "o", None],
                            ["o", "x", "o", None],
                            ["x",  None, None, None],
                            [None, None, None, None]])
    
    oracle = SmartOracle()
    
    #sobre tablero vacio    
    for i in range(0, BOARD_COLUMNS):
        assert oracle._is_winning_move(empty, i, winner) == False
        assert oracle._is_winning_move(empty, i, loser) == False

    for i in range(0, BOARD_COLUMNS):
        assert oracle._is_winning_move(almost, i, loser) == False
    
    assert oracle._is_winning_move(almost, 2, winner)


