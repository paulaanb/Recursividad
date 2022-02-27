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
