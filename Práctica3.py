#1 

x= 5
y= 10
def potencie ():
    q = pow (x, y)
    print (q)
potencie ()

#2 


f = None #no significa nada
c = int(input("Digite un numero del 1 al 10: "))
def numero():
   if c <= 10:
      if c == 1:
        f = "Uno"
      if c == 2:
        f = "Dos"
      if c == 3:
        f = "Tres"  
      if c == 4:
        f = "Cuatro"
      if c == 5:
        f = "Cinco"
      if c == 6:
        f = "Seis"
      if c == 7:
        f = "Siete"
      if c == 8:
        f = "Ocho"
      if c == 9:
        f = "Nueve" 
      if c == 10:
        f = "Diez" 
      print(f)        
   else:   
    print ("Usted no digito un numero del 1 al 10 :)")

numero() 

#3

print("COMPROBADOR DE AÑOS BISIESTOS")
fecha = int(input("Escriba un año y le diré si es bisiesto: "))

if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
    print("El año", fecha, "es un año bisiesto.")
else:
    print("El año", fecha, "no es un año bisiesto.")


#4

f = 8
g = 9
def numeros():
   if f == g:
       print("son iguales")
       return True
   else:
       print("no son iguales ")

numeros()

#5

def isPalindrome(num): 
    return str(num) == str(num)[::-1] 
def largest(bot, top): 
    z = 0 
    for x in range(top, bot, -1): 
     for y in range(top,bot, -1): 
      if isPalindrome(x*y): 
       if x*y > z: 
        z = x*y 
    return z 
print largest(100,999)


#6


def validar_cedula(cedula):

	# La cédula debe tener 11 dígitos
	cedula = cedula.replace('-','')
	if len(cedula)== 11:
		if (int(cedula[0:3]) < 122 and int(cedula[0:3]) > 0 or int(cedula[0:3]) == 402):
			suma = 0
			mutliplicador = 1
			verificador = 0

			mutliplicador = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
			for i in range(10):

				digito = int(cedula[i])*mutliplicador[i]


				if(digito>9):
					digito = digito//10 + digito%10

				suma = suma + digito

			verificador = (10 - (suma % 10) ) % 10

			if(verificador == int(cedula[10]) ):
				return True
			else:
				return False
		# La serie no es válida
		else:
			return False
	# No tiene 11 dígitos
	else:
		return False


#7


x = []
def no():
   numeros = [11,10,2,15]
   x.append(numeros)
   print(x)
   return x

no() 


#8

c = int(input())
a = int(input())
def multiple(valor, multiple):
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False


multiples_6=[]

for i in range(c,a):
    if multiple(i,6):
        multiples_6.append(i)

print ("Los multiples de 6 son:", multiples_6)



