from interpreter import draw
from chessPictures import *
square = Picture(SQUARE) 
blackSquare = square.negative()
bloque = square.join(blackSquare)
fila = bloque.horizontalRepeat(4)
filaNegativa = fila.negative()
tablero = fila.up(filaNegativa).verticalRepeat(2)
draw(tablero)