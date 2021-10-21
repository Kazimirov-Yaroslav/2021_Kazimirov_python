import random
import pygame.image

image = pygame.image.load('400px-Колдунов_Леонид_Модестович.png')
screen = pygame.Surface((200, 200))
screen.blit(image, (0, 0))
print(screen.get_at((90, 90)))



