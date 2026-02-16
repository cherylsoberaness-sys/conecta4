from conecta4.board import Board
"""
if __name__ == "__main__":

   #victoria vertical
   b = Board()

   b.play("x", 0)
   b.play("x", 0)
   b.play("x", 0)

   
   #print("player_char 'o':", b.is_victory("o"))
   #print("Columnas:")
   #for i, col in enumerate(b._columns):
   #  print(i, col)
   
   print("Tablero interno (_columns):")
   for i, col in enumerate(b._columns):
      print(i, col)

   print("is_victory('x'):", b._has_vertical_victory("x", b._columns))
   print("is_victory('o'):", b._has_vertical_victory("o", b._columns))
   
   assert b.is_victory("o") == False
   print(b.is_victory("x"))

   print(b)

   #victoria horizontal
   b1 = Board()
   
   b1.play("x", 0)
   b1.play("x", 1)
   b1.play("x", 2)
   print(b1.is_victory("x"))
   print("is_victory('x'):", b1._has_horizontal_victory("x", b1._columns))

   print(b1)

   #victoria diagonal

   b2 = Board()

   b2.play("x", 0)
   b2.play("o", 1)
   b2.play("x", 1)
   b2.play("o", 2)
   b2.play("x", 3)
   b2.play("o", 2)
   b2.play("x", 2)


   print("Tablero interno (_columns):")
   for i, col in enumerate(b2._columns):
      print(i, col)
   print(b2.is_victory("x"))
   print("is_victory('x'):", b2._has_ascending_victory("x", b2._columns))
   print(b2)



   b3 = Board()

   # Columna 0
   b3.play("o", 0)
   b3.play("o", 0)
   b3.play("x", 0)  # fila 2, parte de la diagonal descendente

   # Columna 1
   b3.play("o", 1)
   b3.play("x", 1)  # fila 1
   b3.play("o", 1)

   # Columna 2
   b3.play("x", 2)  # fila 0
   b3.play("o", 2)
   b3.play("o", 2)

   # Columna 3
   # No necesitamos nada aquí

   
   print("Tablero interno (_columns):")
   for i, col in enumerate(b3._columns):
      print(i, col)
   print(b3.is_victory("x"))
   print("is_victory('x'):", b3._has_descending_victory("x", b3._columns))
   print(b3)

"""