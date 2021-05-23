import pygame

WIN_X, WIN_Y = 700, 500

BLACK = (0,0,0)
GREY = (39, 40, 35)

window = pygame.display.set_mode((WIN_X, WIN_Y))

clock = pygame.time.Clock()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(GREY)
    pygame.display.update()
    clock.tick(40)


