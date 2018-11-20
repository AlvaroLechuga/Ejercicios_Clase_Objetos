#Triangulo isoceles(2 iguales y 1 distinto). Variables: longitud iguales, longitud diferente, altura triangulo
#Metodos necesarios: consultar longitudes, constructor. Otros metodos: calcular area y perimetro
#P = L+L+l; A = (l*a)/2 
class Triangulo(object):
    
    def __init__(self, lIgual, lDiferente, altura):
        self.lIgual = lIgual
        self.lDiferente = lDiferente
        self.altura = altura

    def calcularArea(self):
        area = self.lIgual + self.lIgual + self.lDiferente
        print ("El area del triangulo es: ", area)
    
    def calcularPerimetro(self):
        perimetro = (self.lDiferente * self.altura)/2
        print("El perimetro del triangulo es: ", perimetro)

    def mostrarAltura(self):
        print("La altura del triangulo es: ", self.altura)

    def mostrarLigual(self):
        print("Los lados iguales miden: ", self.lIgual)
    
    def mostrarLdiferente(self):
        print("El lado diferente mide: ", self.lDiferente)

print("Bienvenido al Triangulos isosceles")
lIgual = int(input("Longitud de los lados iguales: "))
lDiferende = int(input("Longitud del lado diferente: "))
altura = int(input("Altura del triangulo: "))

triangulo = Triangulo(lIgual, lDiferende, altura)

triangulo.calcularArea()
triangulo.calcularPerimetro()
triangulo.mostrarAltura()
triangulo.mostrarLigual()
triangulo.mostrarLdiferente()

