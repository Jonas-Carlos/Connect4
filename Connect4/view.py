import pygame
class CaixaTexto:
    def __init__(self, x, y, largura, altura, cor_fundo, cor_borda, fonte, cor_texto):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor_fundo = cor_fundo
        self.cor_borda = cor_borda
        self.fonte = fonte
        self.cor_texto = cor_texto
        self.texto = ""

    def renderizar(self, screen):
        pygame.draw.rect(screen, self.cor_fundo, (self.x, self.y, self.largura, self.altura))
        pygame.draw.rect(screen, self.cor_borda, (self.x, self.y, self.largura, self.altura), 2)
        
        texto_surface = self.fonte.render(self.texto, True, self.cor_texto)
        screen.blit(texto_surface, (self.x + 5, self.y + 5))
