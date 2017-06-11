import numpy as np
import matplotlib.pyplot as plt

def main(): #graficar 4 graficos, es facil
	a = np.load('dataF64951.npy')## hay que colocarle el numero de la prueba
	a=np.delete(a, 1, axis=0)
	a=np.delete(a, 0, axis=0)
	print(a)
	plt.title('Pulsos Guardados')
	plt.ylabel('Pulsos recibidos')
	plt.xlabel('Muestras')
	scale=1
	plt.plot(a/scale)
	plt.show()
if __name__ == "__main__":
    main()
