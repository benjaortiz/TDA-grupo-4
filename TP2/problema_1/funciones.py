import random

def B(n, t, e): 
    #donde 't' y 'e' denotan la lista de beneficios de cada semana

    # Crear una lista de tamanio n para almacenar los beneficios acumulados
    beneficios = [0] * n  # Inicializamos la lista con ceros
    
    # Caso base B(1)
    beneficios[0] = max(t[0], e[0])  # Asignar el beneficio de la semana 1
    
    # Caso base B(2)
    if n > 1:
        beneficios[1] = max(beneficios[0] + t[1], e[1])  # Asignar el beneficio de la semana 2
    
    # Recurrencia para i >= 3
    for i in range(2, n):
        # Para cada semana i, calculamos el maximo entre:
        # - Tomar la tarea t[i] y sumar el beneficio hasta la semana i-1
        # - Tomar la tarea e[i] y sumar el beneficio hasta la semana i-2
        beneficios[i] = max(t[i] + beneficios[i-1], e[i] + beneficios[i-2])

    
    # Devolver la lista completa de beneficios hasta la semana 'n', el ultimo elemento de la lista es el beneficio total optimo.
    return beneficios
 

def reconstruir_tareas(n, t, e, beneficios):  
#donde 't' y 'e' denotan la lista de beneficios de cada semana y 'beneficios' es la lista obtenida en la funcion 'B'

    tareas_elegidas = [0] * n  # Inicializamos una lista para las tareas elegidas (0 significa ninguna tarea)
    
    # El indice inicial debe ser el ultimo indice de la lista de beneficios
    i = n-1
    
    # Bucle para reconstruir las tareas elegidas para i >= 2
    while i >= 2:
        # Comparamos si el beneficio proviene de t_i + B(i-1) o e_i + B(i-2)
        if beneficios[i] == t[i] + beneficios[i-1]:
            tareas_elegidas[i] = 't'  # Se eligio la tarea t_i
            i -= 1  # Retrocedo a la semana anterior
            
        elif beneficios[i] == e[i] + beneficios[i-2]:
            tareas_elegidas[i] = 'e'  # Se eligio la tarea e_i
            i -= 2  # Retrocedo dos semanas
    
    # Casos base fuera del while
    if i == 1:  # Si estamos en la segunda semana
        if beneficios[1] == beneficios[0] + t[1]:
            tareas_elegidas[1] = 't'
            i -= 1 # hice una tranquila en la segunda semana, asique la primera puede ser T o E
        elif beneficios[1] == e[1]:
            tareas_elegidas[1] = 'e' #hice un E en la segunda, asique la primera no hice nada (salteo i==0)

    if i == 0:  # Si solo hay una semana
        if beneficios[0] == t[0]:
            tareas_elegidas[0] = 't'
        elif beneficios[0] == e[0]:
            tareas_elegidas[0] = 'e'

    return tareas_elegidas

def armar_set_datos_aleatorio(n,t,e):
    print("Armando set de datos aleatorio\n")
    for i in range(0,n):
        valores = (random.randint(1,90), random.randint(1,90))
        t[i] = valores[0]
        e[i] = valores[1]



def ejecutar_algoritmo(n: int,tranquilas,estresantes):

    beneficios = B(n,tranquilas,estresantes)
    solucion = reconstruir_tareas(n,tranquilas,estresantes,beneficios)

    return (beneficios,solucion)



def ejecutar_una_vez(cant_semanas: int):
    n = cant_semanas
    tranquilas = [0] * n
    estresantes = [0] * n

    armar_set_datos_aleatorio(n,tranquilas,estresantes)
    print("Tranquilas:", tranquilas,"\n")
    print("Estresantes:", estresantes,"\n")

    print("Armando lista de beneficios acumulados\n")
    
    beneficios = B(n,tranquilas,estresantes)
    print("beneficios: ", beneficios, "\n")
    
    solucion = reconstruir_tareas(n,tranquilas,estresantes,beneficios)
    print("tareas elegidas en cada semana:",solucion,"\n")
