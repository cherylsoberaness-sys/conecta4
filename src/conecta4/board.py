from conecta4.settings import BOARD_COLUMNS, BOARD_ROWS, VICTORY_STREAK
from conecta4.list_utils import find_streak, transpose_matrix, displace_lol

type MatrixColumn = list[list[str|None]]

class Board:
    """
    Representa un tablero con las dimensiones de settings
    Detecta una victoriapl 
    """
    #dunders
    def __init__(self) -> None:
        """
        Crea un tablero con las dimensiones adecuadas.
        El tablero  es una "matriz" de caracteres de jugador
        y None representa una posición vacía
        Cada lista es una columna y el fondo es el principio
        """
        #self._columns = [[None]* BOARD_ROWS] * BOARD_COLUMNS
        #self._columns = [[None for _ in range(BOARD_ROWS)] for _ in range(BOARD_COLUMNS)]
        self._columns : MatrixColumn = []
        for col_num in range(BOARD_COLUMNS):
            self._columns.append([])
            for _ in range(BOARD_ROWS):
                self._columns[col_num].append(None)
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self._columns == other._columns
    def __hash__(self):
        return hash(self._columns)

    @classmethod
    def fromList(cls, _columns):
  
        board = cls()  

        # Copiamos el contenido (sin compartir referencias)
        board._columns = [col.copy() for col in _columns]

        return board
        
    def __repr__(self) -> str:
        """
        Devuelve representacion textual del objeto: las columnas
        """
        #return repr(self._columns)
        #calcular self._columns(board) transpuesto
        
        return f"<Board: {transpose_matrix(self._columns)}" #recordar como se mejora esto cuando expliquen los oraculos
    
    
    def __str__(self):
      
        board = ''
        trans = reversed(transpose_matrix(self._columns))
        for row in trans:
            for element in row:
                if element is None:
                    board += ' - '
                else:
                    board += f' {element} '
            board += '\n'
        return board
    
    def is_full(self) -> bool: 
        """
        True si todas las columnas están llenas
        """
        full = True
        for col in self._columns:
            if col[len(col) - 1] is None:
                full = False
        return full


        
    # Juega una ficha en una columna 
    def play(self, player_char: str, col_number: int)-> None:
        """
        Método impuro, solo lleva a cabo efecto secundarios
        (cambia el tablero)
        si col_number no es válido, debe lanzar excepcion
        ValueError si la columna está llena o si el índice es de una
        columna inexistente
        """

        try:
            #selecciono la columna
            col = self._columns[col_number]

            #inserto el char del jugador en el primer None que encuentro
            found_slot = False #indica si hemos encontrado el hueco donde meter la jugada
            for i, item in enumerate(col):
                if item == None:
                    found_slot = True
                    col[i] = player_char
                    break
            if not found_slot:
                #no he encontrado ningun hueco vacio: estaba llena!
                raise ValueError(f"La columna {col_number} estaba llena!")
        
        except IndexError:
            raise ValueError(f"{col_number} no es válido")


    def is_victory(self, player_char: str) ->bool:
        """
        Determina si hay una victoria para jugador
        representado por un caracter
        """
        return (self._has_vertical_victory(player_char, self._columns) or 
                self._has_horizontal_victory(player_char, self._columns) or
                self._has_ascending_victory(player_char, self._columns) or
                self._has_descending_victory(player_char, self._columns))
    
    #interfaz privada
    def _has_vertical_victory(self, player_char:str, matrix: MatrixColumn) -> bool:
        #detectar play varias veces en el mismo sitio
        #descubrir si hay una racha de cierto numero de player_char
        result = False
        for column in matrix:
            result = find_streak(column, player_char, VICTORY_STREAK)
            if result:
                break
        return result
    
    def _has_horizontal_victory(self, player_char:str, matrix: MatrixColumn) -> bool:
        """
        transforma y venceras:
        transforma la matriz del tablero para cambiar una victoria horizontal 
        en una vertical y entonces llamas a has_vertical_victory
        """
        
        return self._has_vertical_victory(player_char, transpose_matrix(matrix))
      
        
    
    def _has_ascending_victory(self, player_char:str, matrix: MatrixColumn) -> bool:

        reversed_matrix = list(reversed(matrix))
        displaced = displace_lol(reversed_matrix, None)
        return self._has_horizontal_victory(player_char, displaced)
        
    
    def _has_descending_victory(self, player_char:str, matrix: MatrixColumn) -> bool:    
        
        reversed_matrix = list(reversed(matrix))
        return self._has_ascending_victory(player_char, reversed_matrix)
        """
        displaced = displace_lol(matrix, None, 7)
        return self._has_horizontal_victory(player_char, displaced)
        """
   