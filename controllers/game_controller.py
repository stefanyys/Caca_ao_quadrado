import pygame

# Defina as dimensões da tela
LARGURA, ALTURA = 800, 600

def desenhar_tela_inicio(screen, fonte):
    screen.fill((30, 30, 30))
    texto = fonte.render("Tela Inicial - Pressione ESC para sair", True, (255, 255, 255))
    rect = texto.get_rect(center=(LARGURA // 2, ALTURA // 2))
    screen.blit(texto, rect)

def iniciar_jogo():
    pygame.init()
    screen = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Caça ao Quadrado")
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 48)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        desenhar_tela_inicio(screen, fonte)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()