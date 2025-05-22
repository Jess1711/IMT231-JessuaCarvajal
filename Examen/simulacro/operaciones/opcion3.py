# operaciones/opcion3.py

def mostrar_serie(N):
    serie = []
    for i in range(1, N + 1):
        if i % 2 == 0:
            serie.append(-i)
        else:
            serie.append(i)
    print("Secuencia:", ', '.join(map(str, serie)))
