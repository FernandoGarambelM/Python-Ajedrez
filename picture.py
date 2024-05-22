from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for value in self.img[::-1]:
    	horizontal.append(value)
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []
    for value in self.img:
      negative.append([self._invColor(color) for color in value])
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    joinedImg = []
    for i in range(len(self.img)):
        joinedRow = "".join(self.img[i]) + "".join(p.img[i])
        joinedImg.append(joinedRow)
    return Picture(joinedImg)

  def up(self, p):
    uping = []
    for value in self.img:
      uping.append(value)
    for value in p.img:
      uping.append(value)
    return Picture(uping)
   
  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    undering = []
    for value in p.img:
      undering.append(value)
    for value in self.img:
      undering.append(value)
    return Picture(undering)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    horizontal = []
    for value in self.img:
      horizontal.append(value * n)
    return Picture(horizontal)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    b = []
    selfLen = len(self.img)
    for i in range(selfLen):
      a = ""
      for value in self.img:
        a += value[selfLen -1 - i]
      b.append(a)
    return Picture(b)
