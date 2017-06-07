import serial
import matplotlib.pyplot as plt
from drawnow import *
import atexit
import numpy as np
import random
##falta que mande las alertas, q muestre 2 graficos mas (temperatura y presion, humedad(?) )
##hacer interfaz y recibir el tiempo de las muestras
values = []
values_save=np.array([0,0])

plt.ion()
cnt=0

serialArduino = serial.Serial("COM4", 9600) # el puerto cambia segun la conexion

def plotValues():
    plt.title('Serial desde Arduino')
    plt.grid(True)
    plt.ylabel('Valores * 1/1000')
    plt.plot(values, 'ro-', label='values')
    plt.legend(loc='upper right')

def doAtExit():
    af=random.randint(0,100000)
    serialArduino.close()
    print("Close serial ({})".format(af))
    print(values_save)
    np.save('data{}'.format(af),values_save)
    print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

atexit.register(doAtExit)

print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))


for i in range(0,11):#tamaño del grafico a mostrar
    values.append(0)

    
while True:
    while (serialArduino.inWaiting()==0):
        pass
    valueRead = serialArduino.readline(500)
    scale=1/1000
    valueInInt = int(valueRead)*(scale)
    if (valueInInt>=5 or valueInInt==0): 
        print("readline()")
    try:
        print(valueInInt)
        values.append(valueInInt)
        values_save=np.insert(values_save,values_save.size,valueInInt)       
        values.pop(0)
        drawnow(plotValues)
    except ValueError:
        print("Valor Invalido")
