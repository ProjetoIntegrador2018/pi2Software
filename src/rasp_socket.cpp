#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include "motor.h"
#include <stdio.h>
#include <time.h>
#include <wiringPi.h>

#define PORT 8291
#define BUFFER_LENGTH 4096
#define DIR 28
#define STEP 29
#define CW 1
#define CCW 0
#define SPR 200


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
            	roda_motor();
             }
		send(clientfd, freq, strlen(freq), 0);

        } while(strcmp(buffer, "fim"));
    }

    close(clientfd);

    close(serverfd);

    printf("Conexão terminada!\n\n");

    return EXIT_SUCCESS;
}
