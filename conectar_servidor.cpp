/*
#include <Ethernet.h>
#include <SPI.h>

byte mac[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};
byte ip[] = {}; IP del arduino
byte server[] = {}: IP del servidor
EthernetClient client;
*/

const int pot = 0;
float factor_convencion = 7.5; // convencion del sesor del caudal

void setup(){
	//Ethernet.begin(mac, ip); Inicializar Ethernet Shield
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
	/*
	if (client.connect(server, 80) > 0) {
		client.print("GET servidor en php"); enviar los datos en GET
		client.print(caudal_m);
		client.println(" HTTP/1.0"):
		client.println("User-Agent: Arduino 1.0")
		client.println();
		Serial.println("Conectado");
	}else{
		Serial.println("Fallo de conexion");
	}
	if (!client.connected()){
		Serial.println("Desconectado!");
	}
	client.stop();
	client.flush();
	delay(); esperar * para tomar otra muestra
	*/
}