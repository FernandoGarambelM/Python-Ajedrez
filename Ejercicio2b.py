from interpreter import draw
from chessPictures import *
knight = Picture(KNIGHT)
knightN = knight.negative()
knightPar = knight.join(knightN)
knightImpar = knightPar.negative()
knightParV = knightPar.verticalMirror()
tablero = knightPar.up(knightParV)
draw(tablero) 