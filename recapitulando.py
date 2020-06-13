#Declaracion y tipos de variables
nombre = "Hugo Alberto" #String
edad = 24 #Integer
capital = 45.80 #Float
estatus_bancario = False #Boolean
estatus_bancario = True if capital > 0 else False #Operador ternario

#Interpolacion
mensaje = f"Mi nombre es {nombre}, tengo {edad} años, y tengo ${capital} pesos"
#print(mensaje)

#Operadores matematicos
a = 30
b = 5
#print(a+b) Suma
#print(a-b) Resta
#print(a*b) Multiplicacion
#print(a/b) Division
#print(a%b) Modulo/Residuo
#print(a**b) Potencia

#If - else - elif y operadores logicos
#if edad >= 18:
#   print("Eres mayor de edad")
#else:
#   print("Eres menor de edad")

#Ejercicio para evaluar operadores logicos
permiso_secreto = True
permiso_medio = True

if permiso_medio and permiso_secreto:
   print("Tienes todos los permisos")
elif permiso_medio or permiso_secreto:
   print("Tienes al menos un permiso")
else:
   print("No tienes ningun permiso")