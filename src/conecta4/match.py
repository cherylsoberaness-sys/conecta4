from conecta4.player import Player, HumanPlayer
from conecta4.board import Board

class Match:
    def __init__(self, player1: Player, player2: Player):
        player1.char = "x"
        player2.char = "o"
        player1.opponent = player2

        #guardar los jugadores en alguna estructura de datos que nos permita recuperar 
        #a los jugadores mediante su ficha, o sea, recuperar por clave y no por posicion,
        # o sea un dicionario.

        #meterlo en una estructura de datos que nos permita tomarlo dato por dato
        self._players = {"x" : player1, "o" : player2}
        self._round_robbin = [player1, player2]
            
    @property
    def next_player(self):
        next = self._round_robbin[0]
        self._round_robbin.reverse()
        return next
        
    def get_player(self, char):

        return self._players[char]

    def get_winner(self, board: Board) -> Player | None:
        """
        Devuelve el jugador ganador y si no lo hay, devuelve none
        """

        if board.is_victory('x'):
            return self.get_player('x')
        elif board.is_victory('o'):
            return self.get_player('o')
        else:
            return None
        