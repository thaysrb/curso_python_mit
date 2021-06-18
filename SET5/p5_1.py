# Thays Rodrigues 
# SET 5- Problema 5.1

class Grid:
    
    def __init__(self, regras, tamanho):

        # Definições gerais
        self.regras = regras
        self.associacao_regras_cores = dict(zip(range(len(self.regras)), regras))

        # Definições grid
        self.tamanho = tamanho
        self.grid = []
        for elemento in range(tamanho):
            self.grid.append([0 for i in range(tamanho)])

         # Definições formiga
        self.posicao_formiga = [int((self.tamanho - 1) / 2), int((self.tamanho - 1) / 2)]
        self.sentido_formiga = 90 # Definido em graus

    def andar(self):
        if self.sentido_formiga == 0: 
            self.posicao_formiga[1] += 1
        elif self.sentido_formiga == 90:
            self.posicao_formiga[0] -= 1
        elif self.sentido_formiga == 180: 
            self.posicao_formiga[1] -= 1
        elif self.sentido_formiga == 270:
            self.posicao_formiga[0] += 1

    def rotacionar(self, rotacao):
        if rotacao == 'L':
            self.sentido_formiga += 90
            if self.sentido_formiga >= 360:
                self.sentido_formiga = 360 - self.sentido_formiga
        
        else:
            self.sentido_formiga -= 90
            if self.sentido_formiga < 0 and self.sentido_formiga >= -360:
                self.sentido_formiga = 360 + self.sentido_formiga
        
    def alterar_cor(self, x, y):
        self.grid[x][y] = (self.grid[x][y] + 1) % len(self.regras)

def run_langton(regras, tamanho):

    grid = Grid(regras, tamanho)
    passos = 0
    while True:
        grid.alterar_cor(grid.posicao_formiga[0], grid.posicao_formiga[1])
        grid.andar()
        passos += 1
        if grid.posicao_formiga[0] >= grid.tamanho or grid.posicao_formiga[0] < 0 or grid.posicao_formiga[1] >= grid.tamanho or grid.posicao_formiga[1] < 0:
            break
        rotacao = grid.associacao_regras_cores[grid.grid[grid.posicao_formiga[0]][grid.posicao_formiga[1]]]
        grid.rotacionar(rotacao)

    return passos, grid.grid