from grafoMatriz import GrafoMatrizAdjacencia

def kruskal(grafo: GrafoMatrizAdjacencia):
    A = set()
    S = [set([v]) for v in grafo.vertices]
    
    arestas = []
    for u in grafo.vertices:
        for v in grafo.vizinhos(u):
            if u < v:
                arestas.append((grafo.peso(u, v), u, v))
                # print(arestas)
    arestas.sort()
    # print(arestas)
    for aresta in arestas:
        peso, u, v = aresta
        # print(aresta)
        if S[u-1] != S[v-1]:
            A.add((u, v))
            # print(A)
            x = S[u-1].union(S[v-1])
            # print(x)
            for y in x:
                S[y-1] = x
    
    peso_total = sum(g.peso(u, v) for u, v in A)
    print(peso_total)
    print(", ".join(f"{u}-{v}" for u, v in A))


g = GrafoMatrizAdjacencia()
nome_arquivo = input("Digite o nome do arquivo .net: ")
g.ler(nome_arquivo)
kruskal(g)