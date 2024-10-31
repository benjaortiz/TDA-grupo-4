import funciones as pd
import dataset_manager as sets
import timeit

print("Para ejecutar el programa con datos generados aleatoreamente presione 1")
print("Para ejecutar un set de datos especifico presione 2")

eleccion = int(input())

if eleccion == 1:
    n   = int(input("Ingrese la cantidad de semanas (n): "))
    print("el set de datos se va a generar automaticamente\n")
    pd.ejecutar_una_vez(n)

elif eleccion == 2:
    n = int(input("ingese el valor de 'n' correspondiente al archivo 'datos_n_' que desea ejecutar\n"))
    (tranquilas,estresantes) = sets.cargar_set_datos(n)

    print("se va a correr el agloritmo con n =", n,"\n")
    print("tareas tranquilas:", tranquilas,"\n")
    print("tareas estresantes:", estresantes,"\n")

    (beneficios, solucion) = pd.ejecutar_algoritmo(n,tranquilas,estresantes)

    print("Lista de Beneficios: ", beneficios, "\n")
    print("Tareas seleccionadas cada semana: ", solucion, "\n")

    tiempo = timeit.timeit(lambda: pd.ejecutar_algoritmo(n,tranquilas,estresantes), number = 1)
    sets.guardar_resultado(n,solucion,tiempo)

else:
    print("comando no reconocido")