# Thays Rodrigues 
# SET 4 - Problema 4_2

class Vector():
    def __init__(self, lista):
        self.vetor = lista 

    def as_list(self):
        return self.vetor
    
    def size(self):
        return len(self.vetor)

    def magnitude(self):
        magnitude = 0
        for valor in self.vetor: magnitude = magnitude + valor ** 2
        return magnitude ** 0.5
    
    def euclidean_distance(self, other):
        distancia = 0
        for indice in range(len(self.vetor)): distancia = distancia + (self.vetor[indice] - other.vetor[indice]) ** 2
        return distancia ** 0.5
    
    def normalized(self):
        vetor_normalizado = []
        for valor in self.vetor: vetor_normalizado.append(valor/self.magnitude())
        return Vector(vetor_normalizado)

    def cosine_similarity(self, other):
        soma = 0
        for indice in range(len(self.vetor)): soma = self.vetor[indice] * other.vetor[indice] + soma
        sub = 0
        sub = self.magnitude() * other.magnitude() + sub
        return soma/sub
    
    def __add__(self, other):
        somatoria = []
        if isinstance(other, Vector) and len(self.vetor) == len(other.vetor):
            for indice in range(self.size()): somatoria.append(self.vetor[indice] + other.vetor[indice])
            return Vector(somatoria)
        
        elif isinstance(other, int): return (self.vetor + other.vetor)
        else: return None
    
    def __sub__(self, other):
        subtracao = []
        if isinstance(other, Vector) and len(self.vetor) == len(other.vetor):
            for indice in range(self.size()): subtracao.append(self.vetor[indice] - other.vetor[indice])
            return Vector(subtracao)

        elif isinstance(other, int): return self.vetor - other.vetor
        else: return None 
    
    def __mul__(self, other):
        produto = 0
        if isinstance(other, Vector) and len(self.vetor) == len(other.vetor):
            for indice in range(self.size()): produto = self.vetor[indice] * other.vetor[indice] + produto
            return produto
        
        elif isinstance(other, int) or isinstance(other, float):
            produto = []
            for indice in range(len(self.vetor)): produto.append(self.vetor[indice] * other)
            return Vector(produto)

        else: return None
    
    def __truediv__(self, other):
        divisao = []
        if isinstance(other, float) or isinstance(other, int):
            for indice in range(len(self.vetor)): divisao.append(self.vetor[indice] / other)
            return Vector(divisao)
        else: return None