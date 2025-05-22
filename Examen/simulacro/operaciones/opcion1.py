# operaciones/opcion1.py

def contar_divisibles_o_terminan_en_tres(N):
    contador = 0
    for i in range(1, N + 1):
        if i % 3 == 0 or str(i).endswith('3'):
            contador += 1
    print(f"Cantidad de números entre 1 y {N} que son divisibles por 3 o terminan en 3: {contador}")
