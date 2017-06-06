const int pot_f=0;// pin sensor flujo
const int pot_t=1;// pin sensor temeperatura
const int pot_p=2;//  pin sensor presion
int count=0;
//unsigned long pulso_total;

void setup(){ Serial.begin(9600); }

unsigned long timedPulsos( unsigned long pulso_total,int count, int seconds)
{ 
  unsigned long startedAt = millis(); // optimizar esto ?
  while(millis() - startedAt < seconds *1000) // milisegundos
  { 
  int pulso=analogRead(pot_p);
  //Serial.println(pulso);
  if (pulso > 30){ pulso_total=pulso+pulso_total;}
  }
 //Serial.print ("Pulsos totales (");
 //Serial.print (count);
 //Serial.println (") :");
  return pulso_total;
}

unsigned long timedTemperatura( float temp_total,int count, int seconds)// temperatura promedio en n seconds
{ 
  unsigned long startedAt = millis();
  while(millis() - startedAt < seconds *1000) // milisegundos
  { 
  int temp=analogRead(pot_t);
  //Serial.println(pulso);
  temp_total=temp+temp_total;
  
 //Serial.print ("Pulsos totales (");
 //Serial.print (count);
 //Serial.println (") :");
  return pulso_total;
}




void loop(){
  int secs=15;
  Serial.println(timedPulsos(0,count,secs));   // 15 segundos
  
  count=count+1;
  }
