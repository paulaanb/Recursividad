# Recursividad
El enlace de mi repositorio es el siguiente https://github.com/paulaanb/Recursividad

Esta sección plantea algunos problemas. Para resolverlos de una manera que luego sea viable para la programación, es necesario utilizar la reflexión y un poco de inventiva.

El código es el siguiente:

·Ejercicio 5:
'''#Definimos la tabla y los valores
tabla = [1,2,3,4,5,6,7,8]
n = int(input('Introduzca el valor que desea encontrar:'))
i = 0
j = len(tabla)
m = (i+j)/2

#Definimos la clase a utilizar
class tablas:
  def  __init__(self,tabla,n,i,j):
    self.i= i
    self.j= j
    self.n= n
  
  def busqueda_numero (self):
    
    if self.i > self.j:
      return'No hay ningún valor en la posición seleccionada'
      
    else:
      self.m = m
      if tabla[self.m] == n:
        return self.m
      elif tabla[self.m] > n:
        print (busqueda_numero(self))
        return busqueda_numero (self,self.m -1)
      else:
        return busqueda_numero (self, self.m + 1)
        
  #Ejecutamos el programa
  resultado = tablas(tabla,n,j,i)
  print(resultado.busqueda_numero())'''

  ·Ejercicio 6:
  '''#Instrucciones y clases
palabra = str(input('Introduzca una palabra:'))

class verificacion:
  def __init__(self,palabra):
    self.palabra = palabra
  def palabra_palindroma (self):
    if str(self.palabra) == str(self.palabra)[::-1]:
      print ('La palabra es palindroma')
    else:
      print('La palabra no es palindroma')
  
resultado = verificacion(palabra)
print(resultado.palabra_palindroma)

#Valores de los remplazadores
p= palabra
x = ''
remplazadores = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )

#Definicion de la clase convertidor
class convertidor:
  def __inti__(self,p):
    self.p = p
    self.x = x
    self.remplazadores= remplazadores
  def convertir_a_mayúcula (self):
    if p.islower(): #Esto lo usamos para comprobar si esta en minúscula
      return p.upper()
    else:
      print (p)

  def detector_caracteres_no_alfanuméricos(self):
    self.x = ''.join(ch for ch in p if ch.isalnum()) #Podemos utilizar el método isalnum() para comprobar si un carácter o cadena dada es alfanumérico o no. Podemos comparar cada carácter individualmente de una cadena, y si es alfanumérico, lo combinamos usando la función join().


    print(self.x)

  def eliminador_acentos(self):
    for a, b in remplazadores:
        p = p.replace(a, b).replace(a.upper(), b.upper())
    return p

#Instruciones para el correcto funcionamiento del programa
resultado2 = convertidor(x, remplazadores, p)
print(resultado2.convertir_a_mayuscula())
print(resultado2.detector_caracteres_no_alfanuméricos())
print(resultado2.eliminador_acentos())
'''

