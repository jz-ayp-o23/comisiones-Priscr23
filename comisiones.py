"""
Diseña un programa que, dadas las ventas diarias (lunes a viernes) de un vendedor, calcule sus ventas totales de la semana y su comisión, considerando que ésta es del 5% si sus ventas fueron de hasta $20,000 y del 6% si sus ventas superaron dicha cantidad.
750722
"""
#Entradas
lunes = float(input("Ingrese la venta del lunes: "))
martes = float(input("Ingrese la venta del martes: "))
miercoles = float(input("Ingrese la venta del miércoles: "))
jueves = float(input("Ingrese la venta del jueves: "))
viernes = float(input("Ingrese la venta del viernes: "))

#Procesos
venta_semana = lunes + martes + miercoles + jueves + viernes 
comision_1 = venta_semana * 0.05
comision_2 = venta_semana *0.06

#Salidas
if venta_semana <= 20000:
    print("La venta total es: ", venta_semana, "La comisión es: ", comision_1)

elif venta_semana > 20000:
    print("La venta total es: ", venta_semana, "La comisión es: ", comision_2)
