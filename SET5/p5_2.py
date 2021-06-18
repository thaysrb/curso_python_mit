# Thays Rodrigues 
# SET 5- Problema 5.2
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def size(self):
        numero_linhas = 0
        for linha in self.matrix:
            numero_linhas += 1
        return((numero_linhas, len(linha)))
    
    def get(self, r, c):
        return self.matrix[r][c]

    def set(self, r, c, val):
        self.matrix[r][c] = val

    def row(self, n):
        return self.matrix[n]

    def col(self, n):
        auxiliar = []
        for linhas in self.matrix:
            for indice, elemento in enumerate(linhas):
                if indice == n:
                    auxiliar.append(elemento)
        return auxiliar

    def transpose(self):
        return Matrix([list(linha) for linha in [*zip(*self.matrix)]])
    
    def __add__(self, other):
        somada = []
        
        if isinstance(other, Matrix) and self.size()[0] == other.size()[0] and self.size()[1] == other.size()[1]:
            for i in range(self.size()[0]):
                linha = []
                for j in range(self.size()[1]):
                    elemento = self.matrix[i][j] + other.matrix[i][j]
                    linha.append(elemento)
                somada.append(linha)
            return Matrix(somada)
        
        elif isinstance(other, int) or isinstance(other, float):
            for i in range(self.size()[0]):
                linha = []
                for j in range(self.size()[1]):
                    elemento = self.matrix[i][j] + other
                    linha.append(elemento)
                somada.append(linha)
            return Matrix(somada)

    def __sub__(self, other):
        subtraida = []
        
        if isinstance(other, Matrix) and self.size()[0] == other.size()[0] and self.size()[1] == other.size()[1]:
            for i in range(self.size()[0]):
                linha = []
                for j in range(self.size()[1]):
                    elemento = self.matrix[i][j] - other.matrix[i][j]
                    linha.append(elemento)
                subtraida.append(linha)
            return Matrix(subtraida)
        
        elif isinstance(other, int) or isinstance(other, float):
            for i in range(self.size()[0]):
                linha = []
                for j in range(self.size()[1]):
                    elemento = self.matrix[i][j] - other
                    linha.append(elemento)
                subtraida.append(linha)
            return Matrix(subtraida)

    def __mul__(self, other):
        multiplicada = []
        if isinstance(other, Matrix) and self.size()[1] == other.size()[0]:
            
            for i in range(self.size()[0]):
                multiplicada.append([])
                for j in range(other.size()[1]):
                    soma_multiplicacoes = [matriz_1 * matriz_2 for matriz_1, matriz_2 in zip(self.row(i), other.col(j))]
                    multiplicada[i].append(sum(soma_multiplicacoes))
            return Matrix(multiplicada)

        if isinstance(other, int) or isinstance(other, float):
            for i in range(self.size()[0]):
                linha = []
                for j in range(self.size()[1]):
                    elemento = self.matrix[i][j] * other
                    linha.append(elemento)
                multiplicada.append(linha)
            return Matrix(multiplicada)
