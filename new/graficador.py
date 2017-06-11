import serial
import matplotlib.pyplot as plt
from drawnow import *
import atexit
import numpy as np
import random
##falta que mande las alertas, q muestre 2 graficos mas (temperatura y presion, humedad(?) )
##hacer interfaz y recibir el tiempo de las muestras

Flujo_values = []
Temp_values=[]
Presion_values=[]   # para graficar
Humedad_values=[] 

values_save_F=np.array([0,0]) ## se hace float por la temperatura
values_save_T=np.array([float(0),float(0)]) ## se hace float por la temperatura
#values_save_P=np.array([0,0]) # es necesario colocarle info antes ?
#values_save_H=np.array([0,0])

##Para guardar los datos

plt.ion()
cnt=0
cnt_input=0;

serialArduino = serial.Serial("COM4", 9600) # el puerto cambia segun la conexion
def doAtExit():
    af=random.randint(0,100000) #guardar todos los arreglos generados
    serialArduino.close()
    print("Close serial ({})".format(af))
    #print(values_save)
    np.save('dataT{}'.format(af),values_save_T)
    np.save('dataF{}'.format(af),values_save_F)
    print("save succesfully")
    print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

def plotValuesT():
    
    plt.title('Temperatura captada por Arduino')
    plt.grid(True)
    plt.ylabel('Valores')
    plt.plot(Temp_values, 'ro-', label='values')
    plt.legend(loc='upper right')
def plotValuesF():
    
    plt.title('Flujo captado por Arduino')
    plt.grid(True)
    plt.ylabel('Valores')
    plt.plot(Flujo_values, 'bo-', label='values')
    plt.legend(loc='upper right')
def plotValuesP():
    plt.title('Presion captada por Arduino')
    plt.grid(True)
    plt.ylabel('Valores')
    plt.plot(Presion_values, 'go-', label='values')
    plt.legend(loc='upper right')
def plotValuesH():
    plt.title('Humedad captada por Arduino')
    plt.grid(True)
    plt.ylabel('Valores')
    plt.plot(Humedad_values, 'go-', label='values')
    plt.legend(loc='upper right')        


def captdata():
    print("entro")
    while (serialArduino.inWaiting()==0):
        pass
    ard_serial=serialArduino.readline().strip().decode("utf-8")
    print(ard_serial)
    allsensor= str(ard_serial).split(",")
    print(allsensor)
    allsensor[0]=int(allsensor[0])
    allsensor[1]=float(allsensor[1])
    print(allsensor)
    #ardStr=
    #print(ardStr)
    
    print(allsensor)
    return allsensor
    #la wea recibe un string de largo 4 
    # y lo guarda en un arreglo, cada posicion es un sensor

def Flujo(allsensor,values_save_F,Flujo_values): #primer dato entregado
    scale=1/1000
    valuefloatF= float(allsensor[0])*(scale)
    Flujo_values.append(valuefloatF)
    values_save_F=np.insert(values_save_F,values_save_F.size,float(valuefloatF))       
    Flujo_values.pop(0)
    #values.pop(0) verificar si esto sirve
    drawnow(plotValuesF)# funcion solo para graficar los datos de flujo h
    plt.pause(1)
    return values_save_F
def Temperatura(allsensor,values_save_T,Temp_values): #segundo dato en ser entregado
    #values_save_T=np.array([float(0),float(0)])
    scale=1
    valuefloatT= float(allsensor[1])*(scale)
    Temp_values.append(valuefloatT)
    values_save_T=np.insert(values_save_T,values_save_T.size,float(valuefloatT))       
    Temp_values.pop(0)
    #values.pop(0) verificar si esto sirve
    drawnow(plotValuesT)# funcion solo para graficar los datos de temperatura h
    plt.pause(1)
    return values_save_T
'''
def Presion(allsensor): #tercer dato entregado
    scale=1
    valuefloatP= float(allsensor[2])*(scale)
    Presion_values.append(valuefloatP)
    values_save_P=np.insert(values_save_P,values_save.size,float(valuefloatP))       
    Presion_values.pop(0)
    #values.pop(0) verificar si esto sirve
    drawnow(plotValuesP)# funcion solo para graficar los datos de temperatura h
'''
'''    
def Humedad(allsensor): #cuarto dato entregado
    scale=1
    valuefloatH= float(allsensor[3])*(scale)
    Humedad_values.append(valuefloatH)
    values_save_H=np.insert(values_save_H,values_save.size,float(valuefloatH))       
    Humedad_values.pop(0)
    #values.pop(0) verificar si esto sirve
    drawnow(plotValuesH)# funcion solo para graficar los datos de temperatura h    
'''

atexit.register(doAtExit)# no sense
print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))
for i in range(0,11):#tamaño del grafico a mostrar
    Flujo_values.append(0)
    Temp_values.append(0)
    ######        
while True:
    while (serialArduino.inWaiting()==0):
        pass
    #valueRead = serialArduino.readline()

    
    ##para temperatura
    
    
    print("readline()")
    try:
        #print(valueInInt)
        allsensor=captdata()
        print("paso")
        values_save_T=Temperatura(allsensor,values_save_T,Temp_values)
        print(values_save_T)
        values_save_F=Flujo(allsensor,values_save_F,Flujo_values)
        #Humedad(allsensor)
        #Presion(allsensor)

        
    except ValueError:
        print("Valor Invalido")
