const int pot_f=0;// pin sensor flujo
//const int pot_h=2;//  pin sensor humedad
int count=0;
//unsigned long pulso_total;
#include <SFE_BMP180.h>
#include <Wire.h>
#define ALTITUDE 1655.0 



SFE_BMP180 pressure;
void setup(){ 

  Serial.begin(9600); 
  pressure.begin();

}


/*
unsigned long timedPresion( float presion_total, int seconds)// presion promedio en n seconds
{  
  unsigned long startedAt = millis();
  int count_P=0;

  while(millis() - startedAt < seconds *1000) // milisegundos
  { 

  float temp=analogRead(pot_p);
  temp_total=temp+temp_total;
  count_P+=1;
  
  }
  return presion_total/count_P; // promedio de la presion
}


*/

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
    //Serial.println(timedPresion(0,secs));
  }
  Serial.print(pulso_total);
  float tempPr=temp_total/count_T;
  Serial.write(",");
  Serial.print(tempPr,2);// 2 decimales
  Serial.print("\n");
}
