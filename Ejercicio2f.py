from interpreter import draw
from chessPictures import *
square = Picture(SQUARE) 
blackSquare = square.negative()
bloque = square.join(blackSquare)
fila = bloque.horizontalRepeat(4)
draw(fila.negative())