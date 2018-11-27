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
#define STEP_82 23	// MI MAIOR

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
	double atraso = 60;

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
	double atraso = 60;

	int i = 0;
	digitalWrite(DIR, CW);
	for(i = 0; i < qtd; i++){
		digitalWrite(STEP, HIGH);
		delay(atraso);
		digitalWrite(STEP, LOW);
		delay(atraso);
	}
}

void manutencao_corda(int direcao){
	int duracao = 0;
	const int limite = 30;
	const int passo = 1;

	if (direcao == 1){

		while(duracao <= limite){
			printf(" --- Tensionando Corda --- ");

			roda_motor_CW(DIR_329, STEP_329, passo);
			roda_motor_CW(DIR_246, STEP_246, passo);
			roda_motor_CW(DIR_196, STEP_196, passo);
			roda_motor_CW(DIR_146, STEP_146, passo);
			roda_motor_CW(DIR_110, STEP_110, passo);
			roda_motor_CW(DIR_82, STEP_82, passo);

			duracao++;
		}

	}
	else if (direcao == 0){

		while(duracao <= limite){
			printf(" --- Afrouxando Corda --- ");

			roda_motor_CCW(DIR_329, STEP_329, passo);
			roda_motor_CCW(DIR_246, STEP_246, passo);
			roda_motor_CCW(DIR_196, STEP_196, passo);
			roda_motor_CCW(DIR_146, STEP_146, passo);
			roda_motor_CCW(DIR_110, STEP_110, passo);
			roda_motor_CCW(DIR_82, STEP_82, passo);

			duracao++;
		}

	}
	else{
		printf("Erro, direcao invalida");
	}
}
