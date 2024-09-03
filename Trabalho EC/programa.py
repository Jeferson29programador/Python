#from arquivo import classe
from Aresta import Aresta
from Vertice import Vertice
from Grafo import Grafo

#origem = Vertice('Ituiutaba')
#destino = Vertice('Capinopólis')

#a = Aresta(origem, destino, 30)
#print (a)

#Ituiutaba = Vertice('Ituiutaba')
#Capinopolis = Vertice('Capinopólis')
#Trevao = Vertice('Trevao')
#MonteAlegre = Vertice('Monte Alegre')
#Prata = Vertice('Prata')
#Uberlandia = Vertice('Uberlândia')
#Araguari = Vertice('Araguari')

#Ituiutaba.Add_Adjacencia(Capinopolis, 30)
#Ituiutaba.Add_Adjacencia(Trevao, 20)
#Ituiutaba.Show_Adjacencias()

#Capinopolis.Add_Adjacencia(Ituiutaba, 30)
#Capinopolis.Show_Adjacencias()

grafo = Grafo()
grafo.Add_Vertice('Ituiutaba')
grafo.Add_Vertice('Capinópolis')
grafo.Add_Vertice('Trevão')
grafo.Add_Vertice('Prata')
grafo.Add_Vertice('Monte Alegre')
grafo.Add_Vertice('Araguari')
grafo.Add_Vertice('Uberlândia')

grafo.Add_Aresta('Ituiutaba', 'Capinópolis', 30)
grafo.Add_Aresta('Ituiutaba', 'Trevão', 40)
grafo.Add_Aresta('Trevão', 'Prata', 70)
grafo.Add_Aresta('Trevão', 'Monte Alegre', 20)
grafo.Add_Aresta('Uberlândia', 'Prata', 70)
grafo.Add_Aresta('Uberlândia', 'Monte Alegre', 60)
grafo.Add_Aresta('Uberlândia', 'Araguari', 30)
grafo.Show_Vertices()
#print(grafo)

    
 # Função para executar Dijkstra e exibir distâncias a partir de um vértice
def mostrar_distancias(grafo, origem):
    distancias = grafo.Dijkstra(origem)
    print(f"Distâncias a partir de {origem}:")
    for vertice, distancia in distancias.items():
        print(f"Distância até {vertice}: {distancia}")
        

# Executa o algoritmo de Dijkstra a partir de cada cidade
for cidade in ['Ituiutaba', 'Capinópolis', 'Trevão', 'Prata', 'Monte Alegre', 'Araguari', 'Uberlândia']:
    mostrar_distancias(grafo, cidade)
    print('-' * 30)   