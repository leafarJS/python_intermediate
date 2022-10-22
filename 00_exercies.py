import math
from re import L
import numpy as np

#TODO  1. CONVERTIR RADIANES EN GRADOS 
def radianes_grados(x):
  radian = 180
  pi= math.pi
  grados = math.ceil(((pi * radian)/(x * pi)))
  print(f"{grados}°")


radianes_grados(12)

#TODO  2. ORDENAR UNA LISTA 

arr = [350,25,145,132,489,245,354,35,4]

def order_list(arr, value):
  opcion = ["asc", "desc", "none"]
  print(value)
  if opcion[0] == value:
    arr.sort()
  elif opcion[1] == value:
    arr.sort(reverse = True)

  return arr
    
print(order_list(arr,"asc"))

#TODO  3. CONVERTIR UN NUMERO DECIAMAL A BINARIO
def decimal_a_binario(x):
  binario = 0
  multiplicador = 1
  
  if x == 1024:
    return None

  while x != 0:
    # se almacena el módulo en el orden correcto
    binario = binario + x % 2 * multiplicador
    print(f"binario es {binario}")
    x //= 2
    multiplicador *= 10
    print(f"multiplicador es {multiplicador}")

  return binario

# ejemplos de uso

#print(decimal_a_binario(36))
print(decimal_a_binario(1))
#print(decimal_a_binario(22301))

#TODO  4. CONTAR VOCALES

def contar_vacales(str):
  char = list(str)
  vocales = []
  for i in char:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
      vocales.append(i)
  
  print(len(vocales))


#contar_vacales("camino")
contar_vacales("aeiou")
#contar_vacales("xyz")

#TODO  5. OCULTAR NUMERO DE TARJETA DE CREDITO

tarjeta = "4074000131772057"
def ocular_numeros(x):
  view = list(x)
  visible = view[len(view)-4:]
  oculto = []
  for i in range(0,len(view)-4):
    i = "x"
    oculto.append(i)
  
  for i in range(0, len(visible)):
    oculto.append(visible[i])
  
  salida = "".join(oculto)
  print(salida)
    
ocular_numeros(tarjeta)

#TODO  6. contar las Xs las Os
clave = "dfadfjopcpoadifxoxoxoidfaoxoixoisdufoxoisXOOISAXOSJOXJOSIXJOSXJOAISXJOIJXOASXIOAOXIAOXISAOXIOASXIXAOSIXOAXI1654986416846514684687846464840000006" 
clave_1 = "xxxxx00000"
clave_2 = ""

def contar_x_o(x):
  str = x.lower()
  str = list(str)
  x = []
  o = []
  #print(str)
  for i in range(0, len(str)):
    #print(str[i])
    if str[i] == "x":
      x.append(str[i])
    elif str[i] == "0":
      o.append(str[i])
      
      
  if len(o) == 0 and len(x) == 0:
    return True
  elif len(x) == len(o):
    return True
  elif len(x) != len(o):
    return False
  
print(contar_x_o(clave))
print(contar_x_o(clave_1))
print(contar_x_o(clave_2))

#TODO  7. crear una función calculadora
val1 = 10
val2 = 1125

def calcular(a, calc, b):
  if calc == 1:
    return a + b
  
  if calc == 2:
    return a - b
  
  if calc == 3:
    return a * b
  
  if calc == 4:
    if b == 0:
      return "No es divisible"
    else:
      return a / b
  
  if calc > 5:
    print("Operación no contemplada")
    
#1 sumar, 2 restar, 3, multiplicar, 4 dividir  
print(calcular(val1, 1, val2))
print(calcular(val1, 2, val2))
print(calcular(val1, 3, val2))
print(calcular(val1, 4, val2))
print(calcular(val1, 0, val2))

#TODO  8. Dame un descuento 

def descuento(precio, desc):
  descuento = precio * desc
  return  precio - descuento
  
  
print(descuento(100, 0.20))

#TODO  9. solo los numeros
lista = [1,2,3,4,5, "a", "b", "c", "d", "e", "f", "g", 7,8,9,10,11,12]
print(lista)

def numeros_enteros(x):
  global lista
  num = []
  for i in x:
    if type(i) == int:
      num.append(i)
  
  lista = num
  return lista
  
print(numeros_enteros(lista))


#TODO  10. repite el contenido
cadena = "123a!"
cadena_1 = "now"
def repetir(str):
  new_str = []
  pares = []
  for i in str:
    new_str.append(i)

  new = ''.join(new_str)
  
  for i in str:
    for j in range(0,2):
      pares.append(i)
  
  pares = "".join(pares)
  return pares

print(repetir(cadena))
print(repetir(cadena_1))