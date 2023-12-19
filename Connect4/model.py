from constants import LINHAS, COLUNAS

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [[0] * COLUNAS for _ in range(LINHAS)]

    def verificar_vencedor(self):
        for linha in range(LINHAS):
            for coluna in range(COLUNAS - 3):
                if (
                    self.tabuleiro[linha][coluna] == self.tabuleiro[linha][coluna + 1] ==
                    self.tabuleiro[linha][coluna + 2] == self.tabuleiro[linha][coluna + 3] != 0
                ):
                    return True

        for coluna in range(COLUNAS):
            for linha in range(LINHAS - 3):
                if (
                    self.tabuleiro[linha][coluna] == self.tabuleiro[linha + 1][coluna] ==
                    self.tabuleiro[linha + 2][coluna] == self.tabuleiro[linha + 3][coluna] != 0
                ):
                    return True

        for linha in range(3, LINHAS):
            for coluna in range(COLUNAS - 3):
                if (
                    self.tabuleiro[linha][coluna] == self.tabuleiro[linha - 1][coluna + 1] ==
                    self.tabuleiro[linha - 2][coluna + 2] == self.tabuleiro[linha - 3][coluna + 3] != 0
                ):
                    return True

        for linha in range(LINHAS - 3):
            for coluna in range(COLUNAS - 3):
                if (
                    self.tabuleiro[linha][coluna] == self.tabuleiro[linha + 1][coluna + 1] ==
                    self.tabuleiro[linha + 2][coluna + 2] == self.tabuleiro[linha + 3][coluna + 3] != 0
                ):
                    return True

        return False

    def fazer_movimento(self, coluna, jogador):
        for linha in range(LINHAS):
            if self.tabuleiro[linha][coluna] == 0:
                self.tabuleiro[linha][coluna] = jogador
                return True
        return False
