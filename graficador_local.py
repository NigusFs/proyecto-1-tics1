import numpy as np
import matplotlib.pyplot as plt

a = np.load('data61870.npy')## hay que colocarle el numero de la prueba
plt.plot(a)
plt.ylabel('some numbers')
plt.show()