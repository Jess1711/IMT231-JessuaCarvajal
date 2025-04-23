#include "funciones.h"
#include <stdio.h>

#e1

int esPar(int numero) {
    return numero % 2 == 0;
}

#e2

int contarDigitos(int numero) {
    int contador = 0;
    do {
        numero /= 10;
        contador++;
    } while (numero > 0);
    return contador;
}

#e3

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

#e4

int acumular(int actual, int nuevo) {
    return actual + nuevo;
}

#e5

int sumar(int a, int b) {
    return a + b;
}
int restar(int a, int b) {
    return a - b;
}
int multiplicar(int a, int b) {
    return a * b;
}
