import funciones as fun
import dataset_manager as sets
import timeit

def correr_prueba(n, cant_corridas):
    (tranquilas,estresantes) = sets.cargar_set_datos(n)
    
    print("se va a correr el agloritmo con n =", n,"\n")
    print("tareas tranquilas:", tranquilas,"\n")
    print("tareas estresantes:", estresantes,"\n")
    
    (_, solucion) = fun.ejecutar_algoritmo(n,tranquilas,estresantes)
    tiempo_promedio = timeit.timeit(lambda: fun.ejecutar_algoritmo(n,tranquilas,estresantes), number= cant_corridas)
    
    print("Tareas ejecutadas cada semana: ", solucion, "\n")
    print("tiempo promedio para ", cant_corridas, "corridas del algoritmo: ", tiempo_promedio, "\n")
    
    sets.guardar_resultado(n,solucion,tiempo_promedio)


sets.armar_set_datos()

for n in sets.CANTIDAD_SEMANAS:
    correr_prueba(n, sets.CANTIDAD_CORRIDAS)