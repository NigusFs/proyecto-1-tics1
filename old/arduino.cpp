const int pot_f=0;// pin sensor flujo
const int pot_t=1;// pin sensor temeperatura
const int pot_p=2;//  pin sensor presion
int count=0;
//unsigned long pulso_total;

void setup(){ Serial.begin(9600); }

unsigned long timedPulsos( unsigned long pulso_total, int seconds)
{ 
  unsigned long startedAt = millis(); // optimizar esto ?
  while(millis() - startedAt < seconds *1000) // milisegundos
  { 
  int pulso=analogRead(pot_p);

  if (pulso > 30){ pulso_total=pulso+pulso_total;}
  }
 
  return pulso_total;
}

unsigned long timedTemperatura( float temp_total, int seconds)// temperatura promedio en n seconds
{  
  unsigned long startedAt = millis();
  int count_T=0;

  while(millis() - startedAt < seconds *1000) // milisegundos
  { 

  float temp=analogRead(pot_t);
  temp_total=temp+temp_total;
  count_T+=1;
  
  }
  return temp_total/count_T; // promedio de la temperatura
}

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




void loop(){
  int secs=15;// de aqui se regula el tiempo, cambiarlo para q sea ingresado por consola

  Serial.println(timedPulsos(0,secs));   // 15 segundos
  Serial.println(timedTemperatura(0,secs));
  Serial.println(timedPresion(0,secs));
  }
