import operaciones

def mostrar_menu():
    while True:
        print("----- MENÚ DE OPCIONES -----")
        print("1. Contar números divisibles por 3 o que terminan en 3")
        print("2. Imprimir pirámide de asteriscos de altura N")
        print("3. Mostrar la secuencia de los primeros N términos")
        print("4. Mostrar la cantidad de números primos entre 1 y N")
        print("5. Verificar si un número es palíndromo")
        print("6. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            N = int(input("Ingrese un número N: "))
            operaciones.opcion1.contar_divisibles(N)
        elif opcion == '2':
            N = int(input("Ingrese la altura de la pirámide N: "))
            operaciones.opcion2.imprimir_piramide(N)
        elif opcion == '3':
            N = int(input("Ingrese un número N: "))
            operaciones.opcion3.mostrar_serie(N)
        elif opcion == '4':
            N = int(input("Ingrese un número N: "))
            operaciones.opcion4.contar_primos(N)
        elif opcion == '5':
            numero = int(input("Ingrese un número entero positivo: "))
            operaciones.opcion5.verificar_palindromo(numero)
        elif opcion == '6':
            print("¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
