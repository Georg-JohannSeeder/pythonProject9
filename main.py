import pygame

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")


GREEN = [153, 255, 153]
RED = [255, 0, 0]



class ruudud:
    def __init__(self, color, sizea, sizeb, colorbg):
        self.color = color
        self.sizea = sizea
        self.sizeb = sizeb
        self.colorbg = colorbg

    def ruudustik (self):
        f = 1
        screen.fill(self.colorbg)
        for i in range(0, 50, 1):
            e = 1
            for j in range(0, 50, 1):
                pygame.draw.rect(screen, self.color, [e, f, self.sizea, self.sizeb])
                e += 18
            f += 18


ruudud.ruudustik (ruudud(GREEN, 15, 15, RED))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
