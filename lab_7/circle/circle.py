import pygame
pygame.init()


W, H = 800, 600
screen = pygame.display.set_mode((W, H))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
screen.fill(WHITE)
x, y = W//2, H//2
circle = pygame.draw.circle(screen, RED, (x, y), 25)
speed = 10
clock = pygame.time.Clock() 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if y > 25:
            y -= 10
        else:
            y = 25
    if pressed[pygame.K_DOWN]:
        if y < H-25:
            y += 10
        else:
            y = H-25
    if pressed[pygame.K_LEFT]:
        if x > 25:
            x -= 10
        else:
            x = 25
    if pressed[pygame.K_RIGHT]:
        if x < W-25:
            x += 10
        else:
            x = W-25
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), 25)
    pygame.display.update()
    clock.tick(60)