import pygame
import datetime
pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
#Users/tursynk.e/Desktop/lab/lab7/clock/clock.png

clock = pygame.image.load("clock.png").convert()
clock = pygame.transform.scale(clock, (W, H))

left_arm = pygame.image.load("leftarm.png").convert_alpha()
right_arm = pygame.image.load("rightarm.png").convert_alpha()

left_arm = pygame.transform.scale(left_arm, (left_arm.get_width()//2.2, left_arm.get_height()//2.2))
right_arm = pygame.transform.scale(right_arm, (right_arm.get_width()//2.2, right_arm.get_height()//2.2))

right_arm = pygame.transform.rotate(right_arm, -54)
left_arm_rect = left_arm.get_rect(center=(W//2, H//2))
right_arm_rect = right_arm.get_rect(center=(W//2, H//2))


screen.blit(clock, (0, 0))
screen.blit(left_arm, left_arm_rect)
screen.blit(right_arm, right_arm_rect)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(clock, (0, 0))
    now = datetime.datetime.now()
    
    left_arm_copy = left_arm
    sec = now.second
    left_arm_copy = pygame.transform.rotate(left_arm_copy, -6*sec)
    left_arm_copy_rect = left_arm_copy.get_rect(center=(W//2, H//2))
    
    right_arm_copy = right_arm
    min = now.minute
    right_arm_copy = pygame.transform.rotate(right_arm_copy, -6*min)
    right_arm_copy_rect = right_arm_copy.get_rect(center=(W//2, H//2))
    
    screen.blit(right_arm_copy, right_arm_copy_rect)
    screen.blit(left_arm_copy, left_arm_copy_rect)
    
    pygame.display.update()
    