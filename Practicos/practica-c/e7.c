#include <stdio.h>
#include "funciones.h"

int main() {
    int numero, contador = 0;
    while (1) {
        printf("Ingresa un número (-1 para salir): ");
        scanf("%d", &numero);
        if (numero == -1) break;
        if (esMultiploDe3(numero)) contador++;
    }
    printf("Cantidad de múltiplos de 3: %d\n", contador);
    return 0;
}
