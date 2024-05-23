from interpreter import draw
from chessPictures import *

bishop = Picture(BISHOP)
blackBishop = bishop.negative()
king = Picture(KING)
blackKing = king.negative()
knight = Picture(KNIGHT)
blackKnight = knight.negative()
pawn = Picture(PAWN)
blackPawn = pawn.negative()
queen = Picture(QUEEN)
blackQueen = queen.negative()
rock = Picture(ROCK)
blackRock = rock.negative()
square = Picture(SQUARE)
blackSquare = square.negative()

bloque = square.join(blackSquare)
fila = bloque.horizontalRepeat(4)
filaNegativa = fila.negative()

filaPiezasBlancas = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
filaPeones = pawn.horizontalRepeat(8)
filaPeonesNegros = filaPeones.negative()
filaPiezasNegras = filaPiezasBlancas.negative()

primeraFila = fila.under(filaPiezasNegras)
segundaFila = filaNegativa.under(filaPeonesNegros)
tableroNegras = primeraFila.up(segundaFila)

tableroSinFichas = fila.up(filaNegativa).verticalRepeat(2)

penultimaFila = fila.under(filaPeones)
ultimaFila = filaNegativa.under(filaPiezasBlancas)
tableroBlancas = penultimaFila.up(ultimaFila)

tablero = tableroNegras.up(tableroSinFichas.up(tableroBlancas))

draw(tablero)