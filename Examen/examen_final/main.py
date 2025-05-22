import funciones.suma_divisores as opcion1
import funciones.triangulo_letras as opcion2
import funciones.primeros_primos as opcion3
import funciones.fibonacci as opcion4

def main():
    while True:
        print("----- MENÚ DE FUNCIONES -----")
        print("1. Calcular la suma de todos los divisores de un número N")
        print("2. Generar un triángulo de caracteres con letras del alfabeto hasta una altura N")
        print("3. Mostrar los primeros N números primos")
        print("4. Generar la secuencia de los primeros N términos de la serie de Fibonacci inversa")
        print("5. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            N = int(input("Ingrese un número entero positivo: "))
            print(opcion1.suma_divisores(N))
        elif opcion == '2':
            N = int(input("Ingrese la altura del triángulo: "))
            print(opcion2.triangulo_letras(N))
        elif opcion == '3':
            N = int(input("Ingrese cuántos números primos mostrar: "))
            print(opcion3.primeros_primos(N))
        elif opcion == '4':
            N = int(input("Ingrese cuántos términos de Fibonacci inversa mostrar: "))
            print(opcion4.fibonacci_inverso(N))
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
