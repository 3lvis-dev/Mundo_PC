#Mundo PC (Test).

'''
Nota:
'''

from monitor import Monitor
from teclado import Teclado
from raton import Raton
from computadoras import Computadora
from orden import Orden

#Aqui podemos agregar nuestros objetos de computadoras
teclado1 = Teclado('Hp', 'USB')
raton1 = Raton('HP','USB')
monitor1 = Monitor('HP',27)
computadora1 = Computadora('HP',monitor1, teclado1, raton1)

teclado2 = Teclado('Asus', 'Bluetooth')
raton2 = Raton('Asus','Bluetooth')
monitor2 = Monitor('Asus',32)
computadora2 = Computadora('Asus',monitor2, teclado2, raton2)

computadora1 = [computadora1, computadora2]
orden1 = Orden(computadora1)
print(orden1)
		