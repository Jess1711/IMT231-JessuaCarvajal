import operaciones.opcion1 as opcion1
import operaciones.opcion2 as opcion2
import operaciones.opcion3 as opcion3
import operaciones.opcion4 as opcion4
import operaciones.opcion5 as opcion5

def mostrar_menu():
    print("----- MENÚ DE OPCIONES -----")
    print("1. Contar cuántos números entre 1 y N son divisibles por 3 o terminan en 3.")
    print("2. Imprimir una pirámide de asteriscos de altura N.")
    print("3. Mostrar la secuencia de los primeros N términos de la serie: 1, -2, 3, -4, 5, -6, ...")
    print("4. Mostrar la cantidad de números primos entre 1 y N.")
    print("5. Verificar si un número es palíndromo.")
    print("6. Salir del programa.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            N = int(input("Ingrese un número N: "))
            opcion1.contar_divisibles_o_terminan_en_tres(N)
        elif opcion == '2':
            N = int(input("Ingrese la altura de la pirámide N: "))
            opcion2.imprimir_piramide(N)
        elif opcion == '3':
            N = int(input("Ingrese un número N: "))
            opcion3.mostrar_serie(N)
        elif opcion == '4':
            N = int(input("Ingrese un número N: "))
            opcion4.contar_primos(N)
        elif opcion == '5':
            numero = int(input("Ingrese un número entero positivo: "))
            opcion5.verificar_palindromo(numero)
        elif opcion == '6':
            print("¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
