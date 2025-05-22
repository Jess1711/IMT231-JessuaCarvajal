def suma_divisores(N):
    suma = 0
    for i in range(1, N):
        if N % i == 0:
            suma += i
    return suma