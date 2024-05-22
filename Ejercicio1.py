from interpreter import draw
from chessPictures import *
knight = Picture(KNIGHT)
knightN= knight.negative()
parKnight = knight.join(knightN)
knightH = knight.horizontalMirror()
knight90 = knight.rotate()
knightUp = knight.up(knightN)
draw(knightUp)