def verificar_palindromo(numero):
    if numero <= 0:
        print("El número debe ser mayor a 0.")
        return
    es_palindromo = str(numero) == str(numero)[::-1]
    if es_palindromo:
        print(f"{numero} es un palíndromo.")
    else:
        print(f"{numero} no es un palíndromo.")
