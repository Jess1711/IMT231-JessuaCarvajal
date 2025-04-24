#include <stdio.h>
#include "funciones.h"

int main() {
    int numero;
    while (1) {
        printf("Ingresa un número entero (-1 para salir): ");
        scanf("%d", &numero);
        if (numero == -1) break;

        if (esPar(numero))
            printf("Es par\n");
        else
            printf("Es impar\n");
    }
    return 0;
}
