#Section 18: Polimorfismo.
#Leccion 02: Mundo PC (Clase Ráton).

'''
Nota:
'''

from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
	"""docstring for Raton"""
	contador_ratones = 0
	def __init__(self, marca, tipo_entrada):
		super().__init__(marca, tipo_entrada)
		Raton.contador_ratones += 1
		self._id_raton = Raton.contador_ratones 
		
	def __str__(self):
		return f'ID: {self._id_raton}, Marca: {self._marca}, Entrada: {self._tipo_entrada}'


if __name__ == '__main__':
	raton1 = Raton('HP', 'USB')
	print(raton1)

	raton2 = Raton('Asus', 'Bluetooth')
	print(raton2)