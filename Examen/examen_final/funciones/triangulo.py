def triangulo_letras(N):
    for i in range (1, N+1):
        print(''.join(chr(65 + j) for j in range(i)))
