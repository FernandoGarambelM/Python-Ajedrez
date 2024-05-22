from interpreter import draw
from chessPictures import *
square = Picture(SQUARE) 
knight = Picture(KNIGHT)
tablero = square.under(knight)
draw(tablero)