from grafoLista import GrafoListaAdjacencia

class Q1:
    def __init__(self):
        self.grafo = GrafoListaAdjacencia()
        arquivo = input("Digite o nome do arquivo .net: ")
        self.grafo.ler(arquivo)

    def kosajaru(self):
        self.C, self.T, self.A_, self.F = self.DFS(self.grafo)
        self.Gt = self.transpor()
        self.Ct, self.Tt, self.A_t, self.Ft = self.DFS(self.Gt)
        self.imprimir()

    def DFS(self, grafo):
        self.grafo_DFS = grafo
        self.C = {}
        self.T = {}
        self.A_ = {}
        self.F = {}
        for v in self.grafo_DFS.vertices:
            self.C[v] = False
            self.T[v] = float('inf')
            self.F[v] = float('inf')
            self.A_[v] = None

        self.tempo = 0
        for u in self.grafo_DFS.vertices:
            if self.C[u] == False:
                self.DFS_Visit(u)
        
        return (self.C, self.T, self.A_, self.F)
    
    def DFS_Visit(self, u):
        self.C[u] = True
        self.tempo += 1
        self.T[u] = self.tempo
        for n in self.grafo.vizinhos(u):
            if self.C[n] == False:
                self.A_[n] = u
                self.DFS_Visit(n)
        self.tempo += 1
        self.F[u] = self.tempo

    def transpor(self):
        self.Gt = GrafoListaAdjacencia()
        for u in self.grafo.vertices:
            self.Gt.adicionarVertice(u)
        for u in self.grafo.vertices:
            for v in self.grafo.vizinhos(u):
                self.Gt.adicionarAresta(v, u)
        return self.Gt
    
    def imprimir(self):
        self.componentes = {}
        for u, lider in self.A_t.items():
            if lider not in self.componentes:
                self.componentes[lider] = [u]
            else:
                self.componentes[lider].append(u)
    
        for lider, vertices in self.componentes.items():
            print("{" + ", ".join(map(str, vertices)) + "}")

    
q1 = Q1()
q1.kosajaru()