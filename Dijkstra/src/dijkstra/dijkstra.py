import math
from importlib.resources import path


# Indica donde empieza y donde acabas
start="A"
end="E"
# Creamos variables globales
grafo={}
cantidad={}
grafpadre={}
inf=math.inf


def leer_archivo():
    global cantidad
    global grafpadre
    global grafo
    #Se lee el fichero el nodo esta representado en el fichero de la siguiente manera
    #    -Primer caracter de la linea nombre del nodo
    #    -Se separa de los nodos relacionados con /
    #    -Se pone el coste con =
    with open("../graph.txt","r") as fichero:
        for linea in fichero:
            event=linea.rstrip('\n')        
            des_nodo = event.split('/')
            #introducimos en el diccionario el nodo
            grafo[des_nodo[0]]={}
            for event in des_nodo[1:]:
                #introducimos la relacion con el nodo
                auxgraph=event.split('=')
                grafo[des_nodo[0]][auxgraph[0]]=int(auxgraph[1])
                
    #Se presupone que el movimiento es infinito inicialmente        
    for node in grafo:
        cantidad[node] = inf
        grafpadre[node]={}
    #el movimiento de salida hacia si mismo es 0
    cantidad[start]=0
    
    return None
def encontrar_nodo_optimo(cantidad,not_checked):
    #al principio se indica que no hay movimiento y que cualquier valor nos valdria
    cheapest_node=None
    lowest_node=inf
    #buscamos el nodo menos costoso
    for node in cantidad:
        if node in not_checked and cantidad[node]<=lowest_node:
            lowest_node = cantidad[node]
            #avanzamos
            cheapest_node = node
    return cheapest_node
def calculate_movements():
    #comprobamos los nodos no visitados
    sinvisit=[nodo for nodo in cantidad]
    nodo = encontrar_nodo_optimo(cantidad,sinvisit)
    while sinvisit:
        #samos el coste del nodo
        auxcantidad= cantidad[nodo]
        child_cost = grafo[nodo]
 
        for c in child_cost:
            #itineramos si el coste es menor reemplaza
            print(cantidad) 
            if cantidad[c]>auxcantidad+child_cost[c]:
                cantidad[c] = auxcantidad+child_cost[c]
                grafpadre[c]=nodo
        sinvisit.pop(sinvisit.index(nodo))
        nodo= encontrar_nodo_optimo(cantidad, sinvisit)
    print(f"Costs : {cantidad} coste de ir de {start} a {end}")
    
    
    #a la hora de imprimir el camino comprobamos que se ha llegado a un final
    if cantidad[end]<inf:
        path=[end]        
        i=0
        
        while start not in path:
            path.append(grafpadre[path[i]])
            i+=1
            
        print(f"El camino es {path[::-1]}")
    return None

#ejecutamos los metodos    
leer_archivo()
calculate_movements()


        