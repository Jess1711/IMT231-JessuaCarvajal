#include <stdio.h>
#include "funciones.h"

int main() {
    int numero;
    while (1) {
        printf("Ingresa un número mayor a 9 (termina si es de un solo dígito): ");
        scanf("%d", &numero);
        if (numero < 10) break;
        printf("Número invertido: %d\n", invertirNumero(numero));
    }
    return 0;
}
