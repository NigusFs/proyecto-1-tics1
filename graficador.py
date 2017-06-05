import serial
import matplotlib.pyplot as plt
from drawnow import *
import atexit
import numpy as np
import random

values = []
values_save=np.array([0,0])

plt.ion()
cnt=0

serialArduino = serial.Serial("COM4", 9600)

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

#pre-load dummy data
for i in range(0,26):
    values.append(0)

#values_save.append(-1)
#values_save.append(1)
    
while True:
    while (serialArduino.inWaiting()==0):
        pass
    valueRead = serialArduino.readline(500) 
    valueInInt = int(valueRead) 
    if (valueInInt>=5 or valueInInt==0): 
        print("readline()")
    #valueRead = serialArduino.readline(500)

    #check if valid value can be casted
    try:
        #valueInInt = int(valueRead)
        print(valueInInt)
        if True:
            if valueInInt >= 5 or valueInInt==0 :
                values.append(valueInInt)
                #values_save.append(valueInInt)
                values_save=np.insert(values_save,values_save.size,valueInInt)
                
                values.pop(0)
                drawnow(plotValues)
            else:
                print("Invalid! negative number")
        else:
            print("Invalid! too large")
    except ValueError:
        print("Invalid! cannot cast")