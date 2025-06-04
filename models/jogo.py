class Jogo:
    def __init__(self):
        self.largura = 800
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Caça ao Quadrado")
        self.relogio = pygame.time.Clock()
        self.fonte = pygame.font.SysFont(None, 36)

        self.tempo_limite = 30_000  # 30 segundos
        self.inicio = pygame.time.get_ticks()
        self.pontuacao = 0
        self.rodando = True

        self.quadrado = Quadrado(self.largura, self.altura, (255, 0, 0))


    def mostrar_texto(self, texto, x, y):
         #implemente
         pass

    def executar(self):
        while self.rodando:
            self.tela.fill((255, 255, 255))
            tempo_atual = pygame.time.get_ticks()
            tempo_restante = 0 #arrumar codigo  


            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if self.quadrado.foi_clicado(evento.pos):
                        #implemente
                        pass 

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
