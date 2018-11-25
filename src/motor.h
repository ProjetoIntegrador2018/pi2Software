#include<stdio.h>
#include<time.h>
#include<wiringPi.h>

#define DIR_BRACO 28	// Braco Mecanico
#define STEP_BRACO 29	// Braco Mecanico

#define DIR_110 16	// LA
#define STEP_110 15	// LA

#define DIR_146 7	// RE
#define STEP_146 0	// RE

#define DIR_82 22	// MI MAIOR 
#define STEP_82 33	// MI MAIOR

#define DIR_196 12	// SOL
#define STEP_196 13	// SOL

#define DIR_246 14	// SI
#define STEP_246 21	// SI

#define DIR_329 2	// MI MENOR
#define STEP_329 3	// MI MENOR


#define CW 1		//
#define CCW 0		// Clock Config
#define SPR 200		//

void roda_motor_CW(int DIR, int STEP, int qtd){

	pinMode(DIR, OUTPUT);
	pinMode(STEP, OUTPUT);

	int step_count = SPR;
	double atraso = 1;

	int i = 0;
	digitalWrite(DIR, CCW);
	for(i = 0; i < qtd; i++){
		digitalWrite(STEP, HIGH);
		delay(atraso);
		digitalWrite(STEP, LOW);
		delay(atraso);
	}
}

void roda_motor_CCW(int DIR, int STEP, int qtd){

	pinMode(DIR, OUTPUT);
	pinMode(STEP, OUTPUT);

	int step_count = SPR;
	double atraso = 1;

	int i = 0;
	digitalWrite(DIR, CW);
	for(i = 0; i < qtd; i++){
		digitalWrite(STEP, HIGH);
		delay(atraso);
		digitalWrite(STEP, LOW);
		delay(atraso);
	}
}
