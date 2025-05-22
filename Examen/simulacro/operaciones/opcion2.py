# operaciones/opcion2.py

def imprimir_piramide(N):
    for i in range(1, N + 1):
        espacios = ' ' * (N - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacios + asteriscos)
