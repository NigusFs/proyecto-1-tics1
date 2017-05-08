const int pot = 0;
float factor_convencion = 7.5; // convencion del sesor del caudal

void setup(){
	Serial.begin(9600); 
}

void loop(){
	float frecuencia = analogRead(pot); // recibir frecuencia del sensor casero
	float caudal_m = frecuencia/factor_convencion; // Caudal por minuto
	Serial.print("FrecuenciaPulsos: ");
	Serial.print(frecuencia, 0);
	Serial.print("\t Caudal: "); 
	Serial.print(caudal_m);
	delay(400); // 400 milisegundo
}