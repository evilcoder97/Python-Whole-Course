import pygame

pygame.init()

pygame.display.set_mode((400,400))

while True:
    for x in pygame.event.get():
        if x.type== pygame.QUIT:
            pygame.quit()