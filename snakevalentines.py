import pygame, random
from pygame.locals import *
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption('Snake')
pygame.font.init()
font_text = pygame.font.SysFont('arial', 40)
font_pontos = pygame.font.SysFont('arial', 20)
text_inicial = font_text.render("Para começar pressione espaço", 1, (0, 200, 255))
text_perdeu = font_text.render("Você perdeu", 1, (0, 200, 255))
apple = pygame.Surface((10,10))
apple.fill((255,0,0))
rodando = True
tela_inicial = True
gamming = False
tela_restart = False
pontuação = 0
melhor_pontuação = 0
ultima_pontuação = 0
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
PARADO = 4
barra_topo = pygame.Surface((1000,30))
barra_topo.fill((0, 0, 0))
snake_skin = pygame.Surface((10,10))
snake_skin.fill((100,255,100))
barreira = []
bloco = pygame.Surface((10,10))
bloco.fill((72,185,219))

def on_grid_random():
    x = random.randint(10,280) // 10 * 10
    y = random.randint(40,280) // 10 * 10
    for barr in barreira:
        if (x,y) == (barr):
            on_grid_random()
    return (x,y)

apple_pos = on_grid_random()

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def desenhar_pontuação(pontos):
    text_pontuação = font_pontos.render(f"Pontuação Atual: {pontos}", 1, (0, 200, 255))
    screen.blit(text_pontuação, (10, 5))
    
def desenhar_ultima_pontuação(ultima_pontuação):
    text_sua_pontuacao = font_text.render(f"Você fez {ultima_pontuação} pontos",1 ,(0, 200, 255))
    screen.blit(text_sua_pontuacao, (195,230))

def desenhar_melhor_pontuação(melhor_pontuação):
    if tela_restart:
        text_melhor_pontuacao = font_text.render(f"Sua melhor pontuação foi {melhor_pontuação}",1 ,(0, 200, 255))
        screen.blit(text_melhor_pontuacao, (150,270))
        text_reiniciar = font_text.render("Para reiniciar pressione espaço",1,(0,200,255))
        screen.blit(text_reiniciar,(130,310))
    if gamming:
        text_melhor_pontuacao = font_pontos.render(f"Melhor Pontuação: {melhor_pontuação}",1 ,(0, 200, 255))
        screen.blit(text_melhor_pontuacao, (840,5))

# obstáculo do meio parte de cima

for t in range(90,140,10):
    barreira.append((460,t))

for b in range(90,140,10):
    barreira.append((130,b))

for h in range(140,470,10):
    barreira.append((h,90))

# obstaculo do meio parte de baixo

for u in range(180,220,10):
    barreira.append((130,u))

for p in range(180,220,10):
    barreira.append((460,p))

for c in range(130,470,10):
    barreira.append((c,220))

# obstaculo de cima

for i in range(0,480,10):
    barreira.append((i,30))

for a in range(520,1000,10):
    barreira.append((a,30))

# obstaculo lado esquerdo

for x in range(30,140,10):
    barreira.append((0,x))

for z in range(180,300,10):
    barreira.append((0,z))

# obstaculo de baixo

for t in range(0,480,10):
    barreira.append((t,290))

for j in range(520,1000,10):
    barreira.append((j,290))

# obstaculo lado direito

for o in range(30,140,10):
    barreira.append((990,o))

for h in range(180,300,10):
    barreira.append((990,h))

# Textos para minha namorada






clock = pygame.time.Clock()
while rodando:
    clock.tick(15)

    if tela_inicial:
        my_direction = LEFT
        snake = [[300,160], [310,160],[320,160]]
        screen.fill((0,0,0))
        screen.blit(text_inicial,(280,320))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    gamming = True
                    tela_inicial = False

    if gamming:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_UP and not my_direction == DOWN:
                    my_direction = UP
                if event.key == K_DOWN and not my_direction == UP:
                    my_direction = DOWN
                if event.key == K_LEFT and not my_direction == RIGHT:
                    my_direction = LEFT
                if event.key == K_RIGHT and not my_direction == LEFT:
                    my_direction = RIGHT

        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append([0,0])
            pontuação += 1

        for c in snake:
            if collision(snake[0], c) and c is not snake[0]:
                ultima_pontuação = pontuação
                if pontuação > melhor_pontuação:
                    melhor_pontuação = pontuação
                my_direction = PARADO
                gamming = False
                tela_restart = True
                
        if my_direction != PARADO:
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = (snake[i-1][0], snake[i-1][1])

        for c in barreira:
            if collision(snake[0], c):
                ultima_pontuação = pontuação
                if pontuação > melhor_pontuação:
                    melhor_pontuação = pontuação
                my_direction = PARADO
                gamming = False
                tela_restart = True

        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
        
        if snake[0][0] > 600:
            my_direction = PARADO
            snake[0] = (snake[0][0] - 610, snake[0][1])
            my_direction = RIGHT
        if snake[0][0] < 0:
            my_direction = PARADO
            snake[0] = (snake[0][0] + 600, snake[0][1])
            my_direction = LEFT
        if snake[0][1] > 300:
            my_direction = PARADO
            snake[0] = (snake[0][0], snake[0][1] - 280)
            my_direction = DOWN
        if snake[0][1] < 30:
            my_direction = PARADO
            snake[0] = (snake[0][0], snake[0][1] + 270)
            my_direction = UP
            
        screen.fill((3,6,82))
        screen.blit(apple, apple_pos)
        for pos in snake:
            screen.blit(snake_skin,pos)
        for c in barreira:
            screen.blit(bloco, c)
        screen.blit(barra_topo,(0,0))
        desenhar_pontuação(pontuação)
        desenhar_melhor_pontuação(melhor_pontuação)
        pygame.display.update()

    if tela_restart:
        my_direction = LEFT
        snake = [[300,160], [310,160],[320,160]]
        apple_pos = on_grid_random()
        screen.fill((0,0,0))
        screen.blit(text_perdeu,(220,190))
        desenhar_ultima_pontuação(ultima_pontuação)
        desenhar_melhor_pontuação(melhor_pontuação)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    gamming = True
                    tela_restart = False
                    pontuação = 0