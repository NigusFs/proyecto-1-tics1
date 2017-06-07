import numpy as np
import matplotlib.pyplot as plt

a = np.load('data61870.npy')## hay que colocarle el numero de la prueba
plt.title('Pulsos Guardados')
plt.ylabel('Pulsos recibidos')
plt.xlabel('Muestras')
scale=1000
plt.plot(a/scale)
plt.show()
