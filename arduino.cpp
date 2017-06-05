const int pot=0;
int count=0;
//unsigned long pulso_total;

void setup(){ Serial.begin(9600); }

unsigned long timedPulsos( unsigned long pulso_total,int count) // quiero q esto se repita
{ // esto va dentro del void loop
  unsigned long startedAt = millis();
  while(millis() - startedAt < 15000) // 15 segundos
  { 
  int pulso=analogRead(pot);
  //Serial.println(pulso);
  if (pulso > 30){ pulso_total=pulso+pulso_total;}
  }
 //Serial.print ("Pulsos totales (");
 //Serial.print (count);
 //Serial.println (") :");
  return pulso_total;
}
void loop(){
  Serial.println(timedPulsos(0,count)); 
  count=count+1;
  }