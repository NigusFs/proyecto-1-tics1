const int pot = 0;
float factor_convencion = 113.76; // convencion del sesor del caudal
int pulso_total;
int caudal_p=20; // valor aleatorio para el prototipo.
void setup(){
	Serial.begin(9600); 
	
}
//hacer una funcion que calcule el caudal promedio segun los datos analoados
void loop(){
	starttime = millis(); //  verificar si esto funciona
	endtime = starttime; // La idea es que analice los datos en 1 minuto 
						//y retorne el pulso total que se obtuve dentro de ese tiempo
	pulso_total=0;// es 0 para que no se sume con los datos anteriores
	while ((endtime - startime) <= 60000){// pulso total en 1 min


	int pulso = analogRead(pot); // recibir frecuencia del sensor casero
	pulso_total=pulso+pulso_total;
	}

	float caudal_m = pulso_total/factor_convencion; // Caudal por minuto
	Serial.print("Pulsos Totales: ");
	Serial.print(pulso_total, 0);
	Serial.print("\t Caudal: "); 
	Serial.print(caudal_m);
	if (caudal_m > caudal_p) {
		Serial.print(" Alerta !! ");
	}
	delay(200); // 200 milisegundo
}
