#include "funciones.h"
#include <stdio.h>

int esPar(int numero) {
    return numero % 2 == 0;
}

int contarDigitos(int numero) {
    int contador = 0;
    do {
        numero /= 10;
        contador++;
    } while (numero > 0);
    return contador;
}

void mostrarEstadoSemaforo(Semaforo estado) {
    switch (estado) {
        case ROJO:
            printf("Semáforo ROJO - Detenerse\n");
            break;
        case VERDE:
            printf("Semáforo VERDE - Avanzar\n");
            break;
        case AMARILLO:
            printf("Semáforo AMARILLO - Precaución\n");
            break;
    }
}
