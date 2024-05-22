from interpreter import draw
from chessPictures import *
knight = Picture(KNIGHT)
knightN = knight.negative()
knightPar = knight.join(knightN)
knightImpar = knightPar.negative()
knightImparV = knightImpar.verticalMirror()
tablero = knightPar.up(knightImparV)
draw(tablero)