from conecta4.oracle import BaseOracle, ColumnClassification, ColumnRecommendation
from conecta4.board import Board
import random
from conecta4.list_utils import all_same


class Player:
    """
    Representa un jugador, con un nombre y un caracter (con el que juega)
    """
    def __init__(self, name:str, char:str = None, opponent = None, oracle = BaseOracle())->None:
        self.name: str = name
        self.char = char
        self._oracle = oracle
        self.opponent = opponent
        self.last_move = None

    @property
    def opponent(self):
        return self._opponent
    @opponent.setter
    def opponent(self, other):
        if other != None:
            self._opponent = other
            other._opponent = self
    def playing(self, board: Board):

        """
        Elige la mejor columna de aquellas que recomienda el oráculo
        """
        #pregunto al oraculo 
        (best, recommendations) = self._ask_oracle(board)

        #juego en la mejor
        self._play_on(board, best._index)

    def _play_on(self, board: Board, position):
        #juega en la pos
        board.play(self.char, position)
        #Guardo mi ultima jugado
        self.last_move = position

    def _ask_oracle(self, board)-> tuple[ColumnRecommendation, list[ColumnRecommendation]]:
        """
        pregunta al oraculo y devuelve la mejor opcion
        """
        #obtenemos las recomendaciones
        recommendations = self._oracle.get_recommendation(board, self)
        
        #seleccionamos la mejor
        best = self._choose(recommendations)

        return (best, recommendations)

    def _choose(self, recommendations: list[ColumnRecommendation]) -> ColumnRecommendation:
        #quitamos las no validas
        valid_recommendations: list[ColumnRecommendation] = []
        for r in recommendations:
            if r.classification != ColumnClassification.FULL:
                valid_recommendations.append(r)
        #ordenamos por el valor de vlasificacion
        valid_recommendations = sorted(valid_recommendations, key= lambda x: x.classification.value, reverse=True)        
        #si son todas iguales, pillo una el azar
        if all_same(valid_recommendations):
            return random.choice(valid_recommendations)
        # si no lo son, pillo la mas deseable(que sera la primera)
        else:
            #seleccionamos entre ellas la mejor (que sera la primera)
            return valid_recommendations[0]
    

        
        
    
class HumanPlayer(Player):
    
    def __init__(self, name, char=None):
        super().__init__(name, char)

    def _ask_oracle(self, board):
        """
        le pido al humano que es mi oraculo
        """
        while True:
            #pedimos columna al humano
            raw = int(input("Select a column, punny human: "))
            #verificamos que su respuesta no sea una idiotez
            if _is_int(raw) and _is_within_column_range(board, int(raw)) and _is_non_full_column(board, int(raw)):
                #si no lo es, jugamos donde ha dicho y salimos del bucle
                pos = raw
                return (ColumnRecommendation(pos, None), None)
            

# Funciones de validacion de indice de columna
def _is_within_column_range(game_board: Board, col_idx: int):

    return 0 <= col_idx < len(game_board._columns)
    
def _is_non_full_column(game_board: Board, col_idx: int):

    column = game_board._columns[col_idx]
    return column[len(column) - 1] is None
    
def _is_int(col: str):
    
    try:
        int(col)
        return True
    except ValueError:
        return False
            



           


