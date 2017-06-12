const int pot_f=0;// pin sensor flujo
//const int pot_h=2;//  pin sensor humedad
int count=0;
//unsigned long pulso_total;
#include <SFE_BMP180.h>
#include <Wire.h>
#define ALTITUDE 1655.0 

#include <dht.h>
dht DHT;
#define DHT11_PIN 7



SFE_BMP180 pressure;
void setup(){ 

  Serial.begin(9600); 
  pressure.begin();

}


void loop(){
  //variables generales
  int secs=3;// de aqui se regula el tiempo, cambiarlo para q sea ingresado por consola
  unsigned long startedAt = millis(); // optimizar esto ?- si
  //--

  //variables para pulsos
  unsigned long pulso_total=0;
  //--

  //Variables para Temperatura
  int count_T=0;
  float temp_total;
  double T;
  char statusT=pressure.startTemperature();
  //---
  
  //Variables para Presion
  int count_P=0;
  float presion_total;
  double P;
  char statusP= pressure.startPressure(3);;
  //--
  //Variables para Humedad
  int chk = DHT.read11(DHT11_PIN);
  int count_H=0;
  float humedad_total=0;
  //---
  
  while(millis() - startedAt < secs *1000) // milisegundos
  { 
    //pulsos
    int pulso=analogRead(pot_f);
    if (pulso > 30)
      { 
        pulso_total=pulso+pulso_total;
      }
    
    //temp
    if (statusT != 0)
    {
      delay(statusT); // Wait for the measurement to complete:
      statusT = pressure.getTemperature(T);
      if (statusT != 0)
      {
        float temp=float(T);
        temp_total=temp+temp_total;
        count_T+=1;
      }
    } 
    //Presion
    if (statusP != 0)
    {
      delay(statusP); // Wait for the measurement to complete:
      statusP = pressure.getPressure(P,T);
      if (statusP != 0)
      {
        float presion=float(P);
        presion_total=presion+presion_total;
        count_P+=1;
      }
    }

    //---
    
    // Humedad
    float humedad=DHT.humidity;
    humedad_total=humedad+humedad_total;
    count_H+=1;
    
  }
  float tempPr=temp_total/count_T;
  float humPr=humedad_total/count_H;
  float presPr=presion_total/count_P;
  Serial.print(pulso_total);
  Serial.write(",");
  Serial.print(tempPr,2);// 2 decimales
  Serial.write(",");
  Serial.print(humPr,2);// 2 decimales
  Serial.write(",");
  Serial.print(presPr,2);// 2 decimales
  Serial.print("\n");
}
