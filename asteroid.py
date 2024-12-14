import pygame
import random

class Asteroid:
    def __init__(self, image, x, y):
        size = random.randint(30, 70)
        original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(original_image, (size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.randint(1, 4)

    def move(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, 800 - self.rect.width)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


