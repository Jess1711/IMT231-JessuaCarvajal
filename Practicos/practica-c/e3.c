#include <stdio.h>
#include "funciones.h"

int main() {
    Semaforo estado = ROJO;
    for (int i = 0; i < 10; i++) {
        mostrarEstadoSemaforo(estado);
        estado = (estado + 1) % 3;
    }
    return 0;
}
