#include <stdio.h>
#include "funciones.h"

int main() {
    int total = 0, numero;
    while (1) {
        printf("Ingresa un número positivo (negativo para salir): ");
        scanf("%d", &numero);
        if (numero < 0) break;
        total = acumular(total, numero);
    }
    printf("Total acumulado: %d\n", total);
    return 0;
}
