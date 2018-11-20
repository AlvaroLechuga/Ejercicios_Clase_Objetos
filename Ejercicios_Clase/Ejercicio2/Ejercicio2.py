#número de cuenta (un entero), el DNI del cliente (string ya que contiene la letra), el saldo actual y el 
#interés anual que se aplica a la cuenta (porcentaje).
import random
class Cuenta(object):

    def __init__(self, nCuenta, dni, saldoActual, interesAnual):
        self.nCuenta = nCuenta
        self.dni = dni
        self.saldoActual = saldoActual
        self.interesAnual = interesAnual

    def ActualizarSaldo(self):
        #actualizará el saldo de la cuenta aplicándole el interés diario,(anual / 365 aplicado al saldo actual).
        self.saldoActual = self.saldoActual * (self.interesAnual / 360)

    def Ingresar(self, ingreso):
        #permitirá ingresar una cantidad en la cuenta
        self.saldoActual += ingreso
        print("Se ha ingresado el dinero")

    def Retirar(self, retirar):
        #permitirá sacar una cantidad de la cuenta (si hay saldo)
        if(retirar > self.saldoActual):
            print("No puedes retirar esa cantidad de dinero.")
        else:
            self.saldoActual -= retirar
            print("Se ha retirado el dinero correctamente")

    def MostrarInfo(self):
        print("El numero de cuenta es: ", self.nCuenta)
        print ("El DNI es: ", self.dni)
        print("El saldo actual es: ", self.saldoActual)
        print("El interes actual es: ", self.interesAnual)

dni = input("Bienvenido a su cajero de confianza, Introduzca su DNI: ")
numeroCuenta = random.randrange(99999999999999999999)
interesAnual = random.randrange(20)

cliente = Cuenta(numeroCuenta, dni, 0, interesAnual)
opcion = 0
while opcion != 5:
    print("Elije una opcion: ")
    print("1. Actualizar")
    print("2. Ingresar")
    print("3. Retirar")
    print("4. Mostrar informacion")
    print("5. Salir")

    opcion = int(input())

    if(opcion == 1):
        cliente.ActualizarSaldo()
    elif(opcion == 2):
        cantidad = int(input("Dime la cantidad de dinero a ingresar: "))
        cliente.Ingresar(cantidad)
    elif(opcion == 3):
        cantidad = int(input("Dime la cantidad de dinero a retirar: "))
        cliente.Retirar(cantidad)
    elif(opcion == 4):
        cliente.MostrarInfo()
    elif(opcion == 5):
        break;
    else:
        print("Opcion no valida")

cliente.MostrarInfo()



