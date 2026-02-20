import pyfiglet
from enum import Enum, auto
from conecta4.match import Match
from conecta4.player import Player, HumanPlayer
from conecta4.board import Board
from beautifultable import BeautifulTable
from conecta4.settings import BOARD_COLUMNS
from conecta4.oracle import BaseOracle, SmartOracle

class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()

class DifficultyLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

class Game:

    def __init__(self, round_type = RoundType.COMPUTER_VS_COMPUTER, match = Match(Player('Chip'), Player('Chop'))):
    
        self.round_type = round_type
        self.match = match

        #tablero vacio sobre el que jugar
        self.board = Board()

    def start(self):
        # imprimo el nombre por logo del juego
        self.print_logo()
        #configuro la partida (nivel de partida etc)
        self._configure_by_user()
        # arranco el game loop
        self._start_game_loop()

    def print_logo(self):
        logo = pyfiglet.Figlet(font ='eftirobot')
        print(logo.renderText("CONNECTA"))

    def _start_game_loop(self):
        # bucle infinito
        while True:
                
            # obtengo el jugador de turno
            current_player = self.match.next_player
            #le hago jugar
            current_player.playing(self.board)
            # muestro su jugada
            self.display_move(current_player)
            # imprimo el tablero
            self.display_board()
            # si el juego ha terminado...
            if self._is_game_over():
                # muestro resultado final
                self.display_result()
                # salgo del bucle
                break
        
    def display_move(self, player: Player):
        print(f'\n {player.name} {player.char} has moved in column {player.last_move}')

    def display_board(self):
        """
        Imprimir el tablero en su estado actual
        """
        #usar tus metodos en lugar de los del profe
        matrix = self.board._display_matrix()
        bt = BeautifulTable()
        for row in matrix:
            bt.rows.append(row)
        bt.columns.header = [str(i) for i in range(BOARD_COLUMNS)]
        print(bt)
        
    def display_result(self):
        winner = self.match.get_winner(self.board)
        if winner is not None:
            print(f'\n{winner.name} ({winner.char}) wins!!!')
        else:
            print(f'\nA tie between {self.match.get_player("x").name} ("x") and {self.match.get_player("o").name} ("o")')

    def _is_game_over(self):
        """
        El juego se acaba cuando hay vencedor o empate
        """
        winner = self.match.get_winner(self.board)
        if winner != None:
            # hay un vencedor
            return True
        elif self.board.is_full():
            # empate
            return True
        else:
            return False

    def _configure_by_user(self) -> None:
        """
        Le pido al usuario, los valores que el quiere para tipo de partida
        y nivel de dificultad
        """
        #determinar el tipo de partida (preguntando al usuario)
        self.round_type = self._get_round_type()

        #preguntamos nivel de dificultad
        if self.round_type == RoundType.COMPUTER_VS_HUMAN:
            self._difficulty_level = self._get_difficulty_level()

        # crear la partida 
        self.match = self._make_match()

    def _get_difficulty_level(self):
        """
        Pregunta al usuario que tan listo quiere que sea su oponente:
        """
        print("""
        Chose your opponent, Human:
        
        1) Bender: for clowns and wimps
        2) T-800: you may regret it
        3) t-1000: Don't event think about it!
        """)
        while True:
            response = input('lease type 1, 2 or 3: ').strip()
            if response == "1":
                level = DifficultyLevel.LOW
                break
            elif response == "2":
                level = DifficultyLevel.MEDIUM
                break
            else:
                level = DifficultyLevel.HIGH
                break
        
        return level

    def _get_round_type(self) -> RoundType:
        """
        Preguntamos al usuario 
        """
        print("""
        Select Type of round:
                1) Computer vs Computer
                2) Computer vs Human
                """)
        response = ""
        while response != "1" and response != "2":
            response = input('Please type either 1 or 2: ')
        if response == '1':
            return RoundType.COMPUTER_VS_COMPUTER
        else:
            return RoundType.COMPUTER_VS_HUMAN
        
        
    def _make_match(self) -> Match:
        """
        Player 1 siempre robotico
        """
        _levels = {DifficultyLevel.LOW : BaseOracle(),
                   DifficultyLevel.MEDIUM : SmartOracle(), 
                   DifficultyLevel.HIGH: SmartOracle()}
        
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            #ambos jugadores roboticos
            player1 = Player('T-X', oracle=SmartOracle())
            player2 = Player('T-1000', oracle=SmartOracle())
        else:
            # ord vs humano
            player1 = Player('t-800', oracle=_levels[self._difficulty_level])
            player2 = HumanPlayer(name= input('Enter your name, punny human: '))
        

        return Match(player1, player2)
