import pygame

pygame.init()
screen = pygame.display.set_mode([640,480])
fps =30
clock = pygame.time.Clock()
fundo_ambiente_virtual = pygame.image.load('animacoes/fundo.jpg').convert()

parado = []
levantar_ambos_os_bracos = []
levantar_braco_direito = []
levantar_braco_esquerdo = []
caminhar_direita = []
caminhar_esquerda = []

for i in range(0,29):
    parado.append(pygame.image.load("animacoes/standing/"+str(i) +".png").convert_alpha())
    levantar_ambos_os_bracos.append(pygame.image.load("animacoes/both_arms/"+str(i) +".png").convert_alpha())
    levantar_braco_direito.append(pygame.image.load("animacoes/right_arm/"+str(i) +".png").convert_alpha())
    levantar_braco_esquerdo.append(pygame.image.load("animacoes/left_arm/"+str(i) +".png").convert_alpha())
    caminhar_direita.append(pygame.image.load("animacoes/walk_right/"+str(i) +".png").convert_alpha())
    caminhar_esquerda.append(pygame.image.load("animacoes/walk_left/"+str(i) +".png").convert_alpha())

frame_da_animacao=0
estado_avatar = parado
posicao_X_do_avatar = 100
posicao_Y_do_avatar = 160
sequencia_de_animacoes = []

