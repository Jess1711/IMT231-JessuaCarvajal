#include <stdio.h>
#include "funciones.h"

int main() {
    int opcion, a, b;
    while (1) {
        printf("\n1. Sumar dos números\n2. Restar dos números\n3. Multiplicar dos números\n4. Salir\n");
        printf("Elige una opción: ");
        scanf("%d", &opcion);

        if (opcion == 4) break;

        printf("Ingresa dos números: ");
        scanf("%d %d", &a, &b);

        switch (opcion) {
            case 1:
                printf("Resultado: %d\n", sumar(a, b));
                break;
            case 2:
                printf("Resultado: %d\n", restar(a, b));
                break;
            case 3:
                printf("Resultado: %d\n", multiplicar(a, b));
                break;
            default:
                printf("Opción inválida\n");
        }
    }
    return 0;
}
