#include <stdio.h>
#include "funciones.h"

int main() {
    int numero;
    while (1) {
        printf("Ingresa un número entero positivo (0 para salir): ");
        scanf("%d", &numero);
        if (numero == 0) break;

        printf("El número tiene %d dígitos\n", contarDigitos(numero));
    }
    return 0;
}