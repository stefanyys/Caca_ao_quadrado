import pygame
import random

class Quadrado:
    def __init__(self, largura, altura, cor):
        self.tamanho = 60
        self.largura_tela = largura
        self.altura_tela = altura
        self.cor = cor
        self.x = random.randint(0, self.largura_tela - self.tamanho)
        self.y = random.randint(0, self.altura_tela - self.tamanho)
        self.rect = pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)

    def mover(self):
        self.x = random.randint(0, self.largura_tela - self.tamanho)
        self.y = random.randint(0, self.altura_tela - self.tamanho)
        self.rect.topleft = (self.x, self.y)

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)

    def foi_clicado(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)