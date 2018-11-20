#NIF, sueldo base, pago por hora extra, horas extra realizadas en el mes, 
#tipo (porcentaje) de IRPF, casado o no y número de hijos

class Empleado(object):
    def __init__(self, nif, sbase, pagohextra, horasExtras, irpf, casado, hijos):
        self.nif = nif
        self.sbase = sbase
        self.pagohextra = pagohextra
        self.horasExtras = horasExtras
        self.irpf = irpf
        self.casado = casado
        self.hijos = hijos

    #Cálculo y devolución del complemento correspondiente a las horas extra realizadas.
    
    def calcularDevolucionHExtras(self):
         
        devolucion = self.horasExtras * self.pagohextra
        print("El sueldo extra del empleado es: ", devolucion)
        return devolucion

    #Cálculo y devolución del sueldo bruto (Sueldo base más las horas extras realizadas).

    def calcularDevolucionBruto(self, extra):

        bruto = self.sbase + extra
        print("El sueldo bruto del empleado es: ", bruto)

    #Visualización de la información básica del empleado.

    def InformacionEmpleado(self):
        print("NIF del empleado: ", self.nif)
        print("Sueldo base del empleado: ", self.sbase)
        print("Pago por hora extra: ", self.pagohextra)
        print("Horas extras: ", self.horasExtras)
        print("IRPF: ", self.irpf)
        print("Casado: ", self.casado)
        print("Hijos: ", self.hijos)

nif = input("Introduzca el NIF del empleado: ")
sueldoBase = int(input("Dime el sueldo base del empleado: "))
pagoxHoraExtra = int(input("Dime el pago al empleado por hora extra: "))
horasExtras = int(input("Dime la cantidad de horas extras del empleado: "))
irpf = int(input("Dime el IRPF del empleado: "))
casado = input("¿El empleado se encuentra casado? [s/N]")
hijos = int(input("Numero de hijos del empleado: "))

empleado = Empleado(nif, sueldoBase, pagoxHoraExtra, horasExtras, irpf, casado, hijos)

extras = empleado.calcularDevolucionHExtras()
empleado.calcularDevolucionBruto(extras)
empleado.InformacionEmpleado()
