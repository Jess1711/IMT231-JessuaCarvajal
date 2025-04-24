#include <stdio.h>
#include "funciones.h"

//opcion1

int esPrimo(int numero) {
    if (numero <= 1) return 0;
    for (int i = 2; i * i <= numero; i++) {
        if (numero % i == 0) return 0;
    }
    return 1;
}

//opcion2

unsigned long long factorial(int numero) {
    unsigned long long resultado = 1;
    for (int i = 1; i <= numero; i++) {
        resultado *= i;
    }
    return resultado;
}

//opcion3

void contarDigitos(int numero, int *pares, int *impares) {
    *pares = 0;
    *impares = 0;
    for (int i = 1; i <= numero; i++) {
        if (i % 2 == 0)
            (*pares)++;
        else
            (*impares)++;
    }
}

//opcion4

void mostrarMultiplosDe3(int numero) {
    for (int i = 1; i <= numero; i++) {
        if (i % 3 == 0)
            printf("%d ", i);
    }
    printf("\n");
}
