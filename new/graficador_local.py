import numpy as np
import matplotlib.pyplot as plt

def main(): #graficar 4 graficos, es facil
	a = np.load('dataF4017.npy')## hay que colocarle el numero de la prueba
	b = np.load('dataT15615.npy')## hay que colocarle el numero de la prueba
	c = np.load('dataH41051.npy')## hay que colocarle el numero de la prueba
	d = np.load('dataP19405.npy')## hay que colocarle el numero de la prueba
	
	a=np.delete(a, 1, axis=0)
	a=np.delete(a, 0, axis=0)
	
	b=np.delete(b, 1, axis=0)
	b=np.delete(b, 0, axis=0)
	
	c=np.delete(c, 1, axis=0)
	c=np.delete(c, 0, axis=0)
	
	d=np.delete(d, 1, axis=0)
	d=np.delete(d, 0, axis=0)
	#print(a)
	fig1=plt.figure(1)
	plt.title('Pulsos Guardados')
	plt.ylabel('Pulsos recibidos')
	plt.xlabel('Muestras')
	scale=1
	plt.plot(a/scale)
	fig1.show()
	
	fig2=plt.figure(2)
	plt.title('Temp Guardada')
	plt.ylabel('Temp recibida')
	plt.xlabel('Muestras')
	scale=1
	plt.plot(b/scale)
	fig2.show()
	
	fig3=plt.figure(3)
	plt.title('Humedad Guardada')
	plt.ylabel('Humedad recibida')
	plt.xlabel('Muestras')
	scale=1
	plt.plot(c/scale)
	fig3.show()


	fig4=plt.figure(4)
	plt.title('Presion Guardada')
	plt.ylabel('Presion recibida')
	plt.xlabel('Muestras')
	scale=1
	plt.plot(d/scale)
	fig4.show()
	plt.show()

if __name__ == "__main__":
    main()
