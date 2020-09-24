# 1

# numero= 1
# cantidad = 0
# suma= 0
# while numero != 0:
#     numero= int(input("ingrese un numero: "))
#     if numero != 0:
#         suma= suma + numero
#         cantidad= cantidad + 1

#     print(f"usted ingreso {cantidad} y la suma es:{suma} ")


    #2
# def menu ():
#     print ("bienvenido al mneú: 1. convertir de celcius a Fahrenheit, 2. converit de dolar a peso, 3. convertir de metros a pies, 4. salir")


# menu ()
# n= int (input ("ingrese el numero de la opcion deseada:"))
# while n < 4:
#     if n == 1 :
#         x= input ("ingrese el grado en celcius_: ")
#         print ((int (x) * 9/5) + 32)
#         menu ()
#         n= int (input ("ingrese el numero de la opcion deseada:"))
#     elif n== 2: 
#          y= input ("ingrese la cantidad en dolar: ")
#          print ((int (y) * 58.44))
#          menu ()
#          n= int (input ("ingrese el numero de la opcion deseada:"))
#     else:
#         n== 3
#         z= int(input("ingrese la cantidad en metros: "))
#         print ((int (z) * 3.281))
#         menu ()
#         n= int (input ("ingrese el numero de la opcion deseada:"))

# print ("Gracias por utilizar mi programa")
#3
# n = int (input("ingrese el numero deseado: "))
# e= 5
# while  e <= 1000 :
#     print (n * e)
#     e += 5 


# #4
# #calculadora de isr
# top1  =  416220.00
# top2  =  624329.00
# top3  =  867123.00
# salario  =  float ( input ( "ingrese su sueldo mensual:" ))
# salario_anual  =  salario  *  12
# isr  =  0


# if  salario_anual  <=  top1 :
#     print( "Excenta" )
# elif  salario_anual  <=  top2 :
#     excedente  =  salario_anual  -  top1
#     isr  =  excedente  *  0.15
# elif  salario_anual  <=  top3 :
#     excedente  =  salario_anual  -  top2
#     isr  =  31216.00  + ( excedente  *  0.20 )
# else:
#     excedente  =  salario_anual  -  top3
#     isr  =  79776.00  +  excedente  *  0.25

# print ( isr  /  1250 )   

# ars = salario * 0.0304
# afp= salario* 0.085

# print (f"Se descuenta a su salario mensual {salario}: un isr {isr/ 12},ars {ars}, afp {afp}")


#5
carga1000 = 9000
carga500 = 9500
carga100 = 9900
 
def sacar_dinero(cantidad):
  global carga1000, carga500, carga100
  if cantidad <= 1000:
 
    de1000 = int(cantidad / 1000)
    cantidad = cantidad % 1000
    if de1000 >= carga1000: # Si hay suficientes billetes de 50
      cantidad = cantidad + (de1000 - carga1000) * 1000
      de1000 = carga1000
 
    de500 = int(cantidad / 500)
    cantidad = cantidad % 500
    if de500 >= carga500: # y hay suficientes billetes de 20
      cantidad = cantidad + (de20 - carga20) * 20
      de500 = carga500
 
    de100 = int(cantidad / 100)
    cantidad = cantidad % 100
    if de100 >= carga100: # y hay suficientes billetes de 10
      cantidad = cantidad + (de100 - carga100) * 10
      de10 = carga100
 
    # Si todo ha ido bien, la cantidad que resta por entregar es nula:
    if cantidad == 0:
      # Así que hacemos efectiva la extracción
      carga1000 = carga1000 - de1000
      carga500 = carga500- de500
      carga100 = carga100 - de100
      return [de1000, de500, de100]
    else: # Y si no, devolvemos la lista con tres ceros:
      return [0, 0, 0]
  else:
    return [-1, -1, -1]
 
try:
    c = int(input('Cantidad a extraer: '))
    resultado=sacar_dinero(c)
    if resultado==[0,0,0]:
        print ('No hay desglose de billetes para su importe')
    elif resultado==[-1,-1,-1]:
        print ('No hay suficientes billetes')
    else:
        print ('Billetes de 1000:', resultado[0])
        print ('Billetes de 500:', resultado[1])
        print ('Billetes de 100:', resultado[2])
except:
    print ('Importe incorrecto')
            

