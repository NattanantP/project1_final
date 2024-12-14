import pygame

class Bullet:
    def __init__(self, x, y):
        try:
            original_image = pygame.image.load("image/bullet.png")
            self.image = pygame.transform.scale(original_image, (30, 40))
            print("Bullet image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading bullet image: {e}")
            self.image = pygame.Surface((10, 20))
            self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7

    def move(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


