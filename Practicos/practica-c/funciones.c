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