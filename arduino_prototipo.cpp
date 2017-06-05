void setup(){
Serial.begin(9600);
  
}

void timedPulsos(unsigned long howLong) // quiero q esto se repita
{ // esto va dentro del void loop
  unsigned long startedAt = millis();
  while(millis() - startedAt < 30000) // 30 segundos
  { pulso_total=0;
  int pulso=analogRead(pot);

  if (pulso > 30){
  pulso_total=pulso+pulso_total;
  }

  }
  return pulso_total;
}
void loop(){
  Serial.println(timedPulsos);
   
}


-----------------
----------------

const int pot=0;
unsigned long pulso_total;
void setup(){
  Serial.begin(9600);
  pulso_total=0;
}
void loop(){
  
  int pulso=analogRead(pot);
  
  Serial.println(pulso);
  if (pulso > 30){
  pulso_total=pulso+pulso_total;
  }
 
  
  
}
