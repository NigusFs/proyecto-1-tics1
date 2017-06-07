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
    plt.title('Serial value from Arduino')
    plt.grid(True)
    plt.ylabel('Values')
    plt.plot(values, 'rx-', label='values')
    plt.legend(loc='upper right')

def doAtExit():
    af=random.randint(0,100000)
    serialArduino.close()
    print("Close serial ({})".format(af))
    print(values_save)
    #f = open ('{}.txt'.format("hola"),'a')
    #f.write('%s \n' % values_save)
    #f.close() 
    np.save('data{}'.format(af),values_save)
    print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

atexit.register(doAtExit)

print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

for i in range(0,11): # tamaño del grafico mostrado
    values.append(0)    
while True:
    while (serialArduino.inWaiting()==0):
        pass
    valueRead = serialArduino.readline(500) 
    valueInInt = int(valueRead) 
    if (valueInInt>=5 or valueInInt==0): 
        print("readline()")

    try:
        print(valueInInt)
        if valueInInt >= 5 or valueInInt==0 :
        values.append(valueInInt)
        values_save=np.insert(values_save,values_save.size,valueInInt)
        values.pop(0)
        drawnow(plotValues)
