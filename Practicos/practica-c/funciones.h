#ifndef FUNCIONES_H
#define FUNCIONES_H

int esPar(int numero);

int contarDigitos(int numero);

typedef enum { ROJO, VERDE, AMARILLO } Semaforo;
void mostrarEstadoSemaforo(Semaforo estado);

int acumular(int actual, int nuevo);

int sumar(int a, int b);
int restar(int a, int b);
int multiplicar(int a, int b);