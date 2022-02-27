#Instrucciones y clases
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
