#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <time.h>
#include <wiringPi.h>
#include "motor.h"

#define PORT 8291
#define BUFFER_LENGTH 4096


/* void compara_frequencia(char* frequencia){
	
	float freq = atof(frequencia);
	int corda = 329;

	const int corda_329 = 329.00;
	const int corda_246 = 246.00;
	const int corda_196 = 196.00;
	const int corda_146 = 146.00;
	const int corda_110 = 110.00;
	const int corda_82 = 82.00;
	
	const int delta = 5;

	if (corda == 329){
		
		// afr
		if (freq >= corda_329 + delta ){
			roda_motor_CCW();						
		}
		//apr
		if (freq <= corda_329 - delta ){
			roda_motor_CW();						
		}

	}

	if (corda == 246){
		// afr
		if (freq >= corda_246 + delta ){
			roda_motor_CCW();						
		}
		//apr
		if (freq <= corda_246 - delta ){
			roda_motor_CW();						
		}
	}

	if (corda == 196){
		// afr
		if (freq >= corda_196 + delta ){
			roda_motor_CCW();						
		}
		//apr
		if (freq <= corda_196 - delta ){
			roda_motor_CW();						
		}
	}

	if (corda == 146){
		// afr
		if (freq >= corda_146 + delta ){
			roda_motor_CCW();						
		}
		//apr
		if (freq <= corda_146 - delta ){
			roda_motor_CW();						
		}
	}

	if (corda == 110){
		// afr
		if (freq >= corda_110 + delta ){
			roda_motor_CCW();						
		}
		//apr
		if (freq <= corda_110 - delta ){
			roda_motor_CW();						
		}
	}
	
	if (corda == 82){
		// afr
		if (freq >= corda_82 + delta ){
			roda_motor_CCW();						
		}
		//apr
		if (freq <= corda_82 - delta ){
			roda_motor_CW();						
		}
	}
} */

int main(void) {
    wiringPiSetup();

    struct sockaddr_in client, server;

    int serverfd, clientfd;

    char buffer[BUFFER_LENGTH];

    fprintf(stdout, "Iniciando conexão!\n");

    serverfd = socket(AF_INET, SOCK_STREAM, 0);
    
    server.sin_family = AF_INET;
    server.sin_port = htons(PORT);
    memset(server.sin_zero, 0x0, 8);


    int yes = 1;
    if(setsockopt(serverfd, SOL_SOCKET, SO_REUSEADDR,
                  &yes, sizeof(int)) == -1) {
        perror("Socket options error:");
        return EXIT_FAILURE;
    }

    if(bind(serverfd, (struct sockaddr*)&server, sizeof(server)) == -1 ) {
        perror("Socket bind error:");
        return EXIT_FAILURE;
    }

    if(listen(serverfd, 1) == -1) {
        perror("Listen error:");
        return EXIT_FAILURE;
    }
    fprintf(stdout, "Porta %d\n", PORT);

    socklen_t client_len = sizeof(client);
    if ((clientfd=accept(serverfd,(struct sockaddr *) &client, &client_len )) == -1) {
        perror("Accept error:");
        return EXIT_FAILURE;
    }

// Envio e recebimento da frequencia
    char freq[20] = "240";

    strcpy(buffer, freq);

    // Envia para o cliente
    if (send(clientfd, buffer, strlen(buffer), 0)) {
        fprintf(stdout, "Conectado.\n");

        do {
            memset(buffer, 0x0, BUFFER_LENGTH);

            // Recebimento
            int message_len;
            if((message_len = recv(clientfd, buffer, BUFFER_LENGTH, 0)) > 0) {
                buffer[message_len] = '\0';
                printf("Recebido: %s\n", buffer);

            	roda_motor_CCW(DIR_246, STEP_246);
             }
		send(clientfd, freq, strlen(freq), 0);

        } while(strcmp(buffer, "fim"));
    }

    close(clientfd);

    close(serverfd);

    printf("Conexão terminada!\n\n");

    return EXIT_SUCCESS;
}
