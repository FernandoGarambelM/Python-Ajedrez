from interpreter import draw
from chessPictures import *
knight = Picture(KNIGHT)
knightN= knight.negative()
parKnight = knight.join(knightN)
knightH = knight.horizontalMirror()
knight90 = knight.rotate()
knightUp = knight.up(knightN)
knightUnder = knight.under(parKnight)
variosKnightsH = knight.horizontalRepeat(3)
variosKnightsV = knight.verticalRepeat(3)
draw(variosKnightsV)