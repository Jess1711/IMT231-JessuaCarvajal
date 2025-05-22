def contar_primos(N):
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = sum(1 for i in range(1, N + 1) if es_primo(i))
    print(f"Cantidad de números primos entre 1 y {N}: {count}")
