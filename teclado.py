#Section 18: Polimorfismo.
#Leccion 03: Mundo PC (Clase Teclado).

'''
Nota:
'''

from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
	"""docstring for Teclado"""
	contador_teclados = 0

	def __init__(self, marca, tipo_entrada):
		Teclado.contador_teclados += 1 
		super().__init__(marca, tipo_entrada)
		self._id_tecaldo = Teclado.contador_teclados

	def __str__(self):
		return f'ID: {self._id_tecaldo}, Marca: {self._marca}, Teclado: {self._tipo_entrada}'
		

if __name__ == '__main__':
	teclado1 = Teclado('HP', 'USB')
	print(teclado1)
	teclado2 = Teclado('Asus', 'Bluetooth')
	print(teclado2)