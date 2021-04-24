#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
void error( char *msg ) {
 perror(msg); exit(1);
}
int main( int argc, char *argv[] ) {
 int sockfd, portno, n;
 struct sockaddr_in serv_addr;
 struct hostent *server;
 char buffer[256];
 if( argc < 3 ) {
 fprintf( stderr, "O comando dever� ter o formato: %s host porta\n", argv[0]);
 exit(1);
 }
 portno = atoi(argv[2]);
/* Cria um socket com os seguintes par�metros: AF_INET indica que ser� criado na Internet,
 SOCK_STREAM indica que a comunica��o se dar� atrav�s de uma stream e 0 indica para 
 escolher o melhor protocolo (TCP para stream e UDP para datagramas). */
 sockfd = socket( AF_INET, SOCK_STREAM, 0 );
 if( sockfd < 0 ) {
 error("Erro ao abrir o socket");
 }
 server = gethostbyname(argv[1]);
 if( server == NULL ) {
 fprintf(stderr, "Erro ao encontrar o host\n" );
 exit(0);
 }
 /* Coloca zero na string indicada */
 bzero((char *) &serv_addr, sizeof(serv_addr));
 serv_addr.sin_family = AF_INET;
 /* void bcopy(const void *src, void *dest, size_t n);
 Copia n bytes da string src para a string dest */
 bcopy( (char *) server->h_addr, (char *) &serv_addr.sin_addr.s_addr, server->h_length );
 /* Transforma um n�mero inteiro para o formato usado em rede.
 Altera a ordem dos bytes, caso necess�rio. */
 serv_addr.sin_port = htons(portno);
 /* Tenta se conectar com o servidor */
 if( connect( sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0 ) {
 error("Erro ao conectar");
 }
 printf( "CLIENTE: Entre com a mensagem: ");
 bzero(buffer, 256);
 fgets(buffer, 255, stdin); /* Escreve na conex�o aberta pelo socket utilizando a mesma fun��o de escrita em arquivo */
 n = write( sockfd, buffer, strlen(buffer) );
 if( n < 0 ) {
 error("Erro ao escrever a mensagem no socket");
 }
 bzero( buffer, 256 );
 /* L� da conex�o aberta pelo socket da mesma forma que ler de um arquivo */
 n = read( sockfd, buffer, 255 );
 if( n < 0 ) {
 error("Erro ao ler o socket");
 }
 printf("CLIENTE: Mensagem recebida atrav�s do socket: %s", buffer );
 close(sockfd);
 return 0;
}