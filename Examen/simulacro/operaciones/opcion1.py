def contar_divisibles(N):
    count = 0
    for i in range(1, N + 1):
        if i % 3 == 0 or str(i).endswith('3'):
            count += 1
    print(f"Cantidad de números entre 1 y {N} que son divisibles por 3 o terminan en 3: {count}")
