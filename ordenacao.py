from grafoLista import GrafoListaAdjacencia

class Ordenacao:
    def __init__(self, G: GrafoListaAdjacencia):
        self.G = G
        self.C = [False] * (G.qtdVertices()+1)
        self.T = [float('inf')] * (G.qtdVertices()+1)
        self.F = [float('inf')] * (G.qtdVertices()+1)
        self.O = []
    
    def DFS_ordenacao_topologica(self):
        tempo = 0
        for u in self.G.vertices:
            if not self.C[u]:
                Ordenacao.DFS_visit(self, u, tempo)

        return self.O

    def DFS_visit(self, u: int, tempo: int):
        self.C[u] = True
        tempo += 1
        self.T[u] = tempo

        for v in self.G.vizinhos(u):
            if not self.C[v]:
                Ordenacao.DFS_visit(self, v, tempo)

        tempo += 1
        self.F[u] = tempo
        self.O.insert(0, u)

if __name__ == '__main__':
    g = GrafoListaAdjacencia()
    g.ler('instancias/dirigidos/manha.net')

    aux = Ordenacao(g)
    res = aux.DFS_ordenacao_topologica()
    print(res)
    print([g.rotulo(i) for i in res])

    g2 = GrafoListaAdjacencia()
    g2.ler('instancias/dirigidos/tcc_completo.net')

    aux2 = Ordenacao(g2)
    res2 = aux2.DFS_ordenacao_topologica()
    print(res2)
    print([g2.rotulo(i) for i in res2])
    
