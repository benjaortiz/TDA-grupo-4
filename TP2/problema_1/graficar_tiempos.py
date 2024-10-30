import funciones as fun
import dataset_manager as sets
import timeit
import matplotlib.pyplot as plt

sets.armar_set_datos()

cant_ejecuciones = 100
tiempos = []

for n in sets.CANTIDAD_SEMANAS:

    (tranquilas,estresantes) = sets.cargar_set_datos(n)
    
    tiempo_actual = timeit.timeit(lambda: fun.ejecutar_algoritmo(n,tranquilas,estresantes),number = cant_ejecuciones)/cant_ejecuciones
    tiempos.append(tiempo_actual)


tiempos_promedios   = tiempos
valores_n = sets.CANTIDAD_SEMANAS

plt.plot(valores_n, tiempos_promedios, marker='o')
plt.title('Tiempos de ejecución para diferentes valores de n')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo promedio de ejecución (segundos)')
plt.grid(True)

# for a,b in zip(valores_n,tiempos_promedios): 
#     plt.text(a, b, str(round(b,5)))

plt.show()