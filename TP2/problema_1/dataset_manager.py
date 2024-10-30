import random

CANTIDAD_SEMANAS = [50, 20, 50, 100, 150, 200, 300, 400, 500, 700, 800, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 4000, 5000]
CANTIDAD_CORRIDAS = 100

def armar_set_datos():
    tranquila = 0
    estresante = 0
    for n in CANTIDAD_SEMANAS:
        with open("set_datos/datos_n_" + str(n),"w") as archivo:
            for _ in range(0,n):
                valores = (random.randint(1,100), random.randint(1,100))
                tranquila = valores[0]
                estresante = valores[1]
                archivo.write(str(tranquila)+";"+str(estresante)+"\n")
                #print("semana numero ",i+1,"tarea tranquila:", tranquila, "tarea estresante:",estresante,"\n")


def cargar_set_datos(cant_semanas):
    dataset = "set_datos/datos_n_" + str(cant_semanas)
    tranquilas =[]
    estresantes= []
    
    #abro archivo con las tareas
    with open(dataset,"r") as archivo:
        for linea in archivo:        
            valores = linea.rstrip("\n").split(";")
            
            #cargo las tareas de la linea (casteo a int porque son strings)
            tranquilas.append(int(valores[0]))
            estresantes.append(int(valores[1]))

    return (tranquilas, estresantes)

  
def guardar_resultado(cant_semanas, solucion, tiempo_ejecucion):
    nombre_archivo = "set_datos/resultado_n_" + str(cant_semanas)

    with open(nombre_archivo,"w") as archivo:
        archivo.write("Resultado obtenido para n = " + str(cant_semanas) + " semanas\n")
        archivo.write("Tiempo de ejecucion promedio: "+ str(tiempo_ejecucion) +"\n")
        archivo.write("Tareas ejecutadas cada semana: " + str(solucion) + "\n")