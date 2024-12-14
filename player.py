import pygame

class Player:
    def __init__(self, image, x, y):
        original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

