#include<stdio.h>
#include<time.h>
#include<wiringPi.h>

#define DIR 28
#define STEP 29
#define CW 1
#define CCW 0
#define SPR 200

void roda_motor_CW(void){
	

	pinMode(DIR, OUTPUT);
	pinMode(STEP, OUTPUT);

	int step_count = SPR;
	double atraso = 1;

	int i = 0;
	digitalWrite(DIR, CW);
	for(i = 0; i < 50; i++){
		digitalWrite(STEP, HIGH);
		delay(atraso);
		digitalWrite(STEP, LOW);
		delay(atraso);
	}

void roda_motor_CCW(void){
	

	pinMode(DIR, OUTPUT);
	pinMode(STEP, OUTPUT);

	int step_count = SPR;
	double atraso = 1;

	int i = 0;
	digitalWrite(DIR, CCW);
	for(i = 0; i < 50; i++){
		digitalWrite(STEP, HIGH);
		delay(atraso);
		digitalWrite(STEP, LOW);
		delay(atraso);
	}

//void compara_frequencia(char frequencia, int corda){
	
	//if (corda == 329){
		
	//}

	//if (corda == 246){
		
	//}

	//if (corda == 196){
		
	//}

	//if (corda == 146){
		
	//}

	//if (corda == 110){
		
	//}
	
	//if (corda == 82){
		
	//}
//}
