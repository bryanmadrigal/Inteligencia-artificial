from collections import deque

def bfs(grafico, inicio, objetivo):
   cola = deque ([(inicio, [inicio ])])

   while cola:
      nodo, camino = cola.popleft()

      if nodo == objetivo:
         return camino
      
      for vecino in grafico [nodo]:
         if vecino not in camino:
            cola.append ((vecino, camino + [vecino]))

   return None
         
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}        

#inicio 
inicio = 'A'
#objetivo
objetivo = 'E'

resultado = bfs (grafo, inicio, objetivo)

if resultado:
   print (f"camino de {inicio}: a  {objetivo}")

else:
   print (f"no se encontro un camino de {inicio} a {objetivo}")