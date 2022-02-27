#Definimos la tabla y los valores
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
  
  
