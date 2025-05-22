def contar_divisibles(N):
    count = 0
    for i in range(1, N + 1):
        if i % 3 == 0 or str(i).endswith('3'):
            count += 1