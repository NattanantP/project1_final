
import pygame

class PowerUp:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 2

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)



