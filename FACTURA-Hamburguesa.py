#Datos Empresa
nombre_empresa=input("Ingrese el nombre de la empresa: ")
nit_empresa=int(input("Nit de la empresa: "))
num_factura=int(input("Numero de empresa: "))
num_autorizacion=int(input("Numero de autorizacion: "))
#Datos Cliente
lugar=input("Ingrese la direccion: ")
gestion=int(input("Ingrese el año de ingreso. "))
mes=int(input("Ingrese el mes de ingreso: "))
dia=int(input("Ingrese el dia de ingreso: "))
nombre_apellido=input("Ingrese su nombre y apellido: ")
nit_ci=int(input("Ingrese el nit o su CI: "))
cantidadTotal=int(input("cuantos items ingresara a su factura"))
cantidadInicial=0
total=0
while cantidadInicial<cantidadTotal:
    producto=input("ingrese el nombre del producto")
    print("precio de",producto)
    precio=int(input())
    print("cantida de",producto)
    cantidadProducto=int(input())
    subtotal=precio*cantidadProducto
    total=total+subtotal
    catidadInicial=cantidadInicial+1
print("el total de su compra es",total)    


