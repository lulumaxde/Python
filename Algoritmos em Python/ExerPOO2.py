class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c





    #def perimetro(self):
     #   A = self.a
      #  B = self.b
       # C = self.c

        #return A+B+C

    def tipo_lado(self):
        if (self.a == self.b and self.a == self.c):
            string = "equilátero"
        elif (self.a == self.b or self.a == self.c or self.b == self.c):
            string = "isósceles"
        else:
            string = "escaleno"

        return string
