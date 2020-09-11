#1
print(4<2)

#2
Nombre= "Rose"
print("Bienvenido " + Nombre)

#3
n=2
if n %2 == 0:
    print ("es par")

else:
    print("es impar")

#4
m=5 
z=4
print (m>z)
#5
dolar=300
tasa=58.44
peso_dominicano=dolar*tasa
print(peso_dominicano)

#6
celcius=37
fahrenheit=(celcius*9/5 + 32 )
print (fahrenheit)
#7
n1=90
n2=95
n3=77
n4=92
promedio=((n1+ n2+ n3+ n4)/4)
if promedio <=49:
    print("f")
elif promedio <=59:
    print ("e")
elif promedio <=69:
    print ("d")
elif promedio <=79:
    print("c")
elif promedio <=89:
    print ("b")
else:
    print ("a")

#8
monto= 10000
cantidad_cuotas=12
interés=monto* 0.003
cuota_mensual= (monto+ interés)/cantidad_cuotas
print(cuota_mensual)
