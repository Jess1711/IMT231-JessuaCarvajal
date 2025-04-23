#include <stdio.h>
#include "funciones.h"

int main() {
    int numero;
    while (1) {
        printf("Ingresa un número positivo (0 o negativo para salir): ");
        scanf("%d", &numero);
        if (numero <= 0) break;
        printf("El factorial de %d es %d\n", numero, factorial(numero));
    }
    return 0;
}
