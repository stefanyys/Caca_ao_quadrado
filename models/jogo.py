import sys
import pygame
from models.quadrado import Quadrado

class Jogo:
    def __init__(self):
        pygame.init()
        self.largura = 800
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Caça ao Quadrado")
        self.relogio = pygame.time.Clock()
        self.fonte = pygame.font.SysFont(None, 36)

        self.tempo_limite = 30_000  # 30 segundos em milissegundos
        self.inicio = pygame.time.get_ticks()
        self.pontuacao = 0
        self.rodando = True

        self.quadrado = Quadrado(self.largura, self.altura, (255, 0, 0))

    def mostrar_texto(self, texto, x, y):
        img = self.fonte.render(texto, True, (0, 0, 0))
        self.tela.blit(img, (x, y))

    def executar(self):
        while self.rodando:
            self.tela.fill((255, 255, 255))
            tempo_atual = pygame.time.get_ticks()
            tempo_restante = max(0, (self.tempo_limite - (tempo_atual - self.inicio)) // 1000)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if self.quadrado.foi_clicado(evento.pos):
                        self.pontuacao += 1
                        self.quadrado.mover()

            self.quadrado.desenhar(self.tela)
            self.mostrar_texto(f"Pontos: {self.pontuacao}", 10, 10)
            self.mostrar_texto(f"Tempo: {tempo_restante}", 10, 50)

            if tempo_restante <= 0:
                fim = self.fonte.render("FIM DE JOGO!", True, (0, 0, 0))
                self.tela.blit(fim, (300, 250))
                pygame.display.update()
                pygame.time.wait(3000)
                self.rodando = False

            pygame.display.update()
            self.relogio.tick(60)

        pygame.quit()
        sys.exit()