''' Gestión de Ventas y Reportes diarios versión 0.20. Gonzalo Bauzá - 2018 '''

# Establezco la variable caja para comenzar el día

print ("¡Buenos días!")
caja_inicial= int(input("Ingrese el valor inicial de su caja: "))

if caja_inicial > 0:
    print ("La caja tiene un valor de:", int (caja_inicial), "pesos")
elif caja_inicial < 0:
    print ("La caja no puede ser menor que 0")

print ("Valor inicial adquirido. ¡Comencemos a trabajar!")

# Luego de que la caja ya fue iniciada procedemos a las operatorias

caja = 0
x = 0
numeropr = 0
saldoCaja = 0
comprar= int (2)

def compra(): # Funcion de compra
    precio=0
    numeropr = int (input ("Cuantos productos son: "))
    while numeropr > 0:
        numeropr = numeropr - 1
        x = int (input ("Precio del producto: "))
        precio = precio + x
    print ("Debe: ", precio)
    efectivo = int (input ("Efectivo: "))
    cambio = efectivo - precio
    global saldoCaja
    saldoCaja = saldoCaja + precio
    while efectivo < precio: # Condicion obvia de pago
        print("No alcanza para pagar la compra, abone lo necesario")
        efectivo = int (input ("Efectivo: "))
        cambio = efectivo - precio

# Reporte después de la compra
    else:
        print ("_____________________________")
        print ("Total: ", precio)
        print ("Efectivo: ", efectivo)
        print ("Cambio: ", cambio)
        print ("Gracias por su preferencia")
        print ("_____________________________")
        
# Bucle para realizar la función tantas veces como queramos

while(comprar==2):
  compra()
  comprar = int (input ("Quiere cerrar la caja? \n 1-SI \n 2-NO \n Opcion: "))

# Final del día, reportes de saldo y últimos detalles

saldoTotal = caja_inicial + saldoCaja
if comprar == 1:
    print ("Hemos finalizado el día. Hoy la caja ha culminado con", saldoTotal)

