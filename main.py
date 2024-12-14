import pygame
import random
from player import Player
from asteroid import Asteroid
from bullet import Bullet
from powerup import PowerUp

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ASTEROID_COUNT = 5
FONT_SIZE = 30
POWER_UP_CHANCE = 0.1

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroid Remake")
    clock = pygame.time.Clock()

    # Upload Background
    background = pygame.image.load("image/background.png")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player("image/ship.png", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
    bullets = []
    asteroids = [Asteroid("image/asteroid.png", random.randint(0, SCREEN_WIDTH), random.randint(-150, -50)) for _ in range(ASTEROID_COUNT)]
    power_ups = []

    score = 0
    lives = 3
    font = pygame.font.Font(None, FONT_SIZE)

    running = True
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(player.rect.centerx, player.rect.top))

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Updating bullets
        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)
            bullet.draw(screen)

        # Updating Asteroid
        for asteroid in asteroids[:]:
            asteroid.move()
            asteroid.draw(screen)

            # detect collision of ship and asteroid
            if player.rect.colliderect(asteroid.rect):
                lives -= 1
                asteroids.remove(asteroid)
                asteroids.append(Asteroid("image/asteroid.png", random.randint(0, SCREEN_WIDTH), random.randint(-150, -50)))

                if lives <= 0:
                    running = False

            # detect collision of bullet and asteroid
            for bullet in bullets[:]:
                if bullet.rect.colliderect(asteroid.rect):
                    score += 10
                    bullets.remove(bullet)
                    asteroids.remove(asteroid)
                    asteroids.append(Asteroid("image/asteroid.png", random.randint(0, SCREEN_WIDTH), random.randint(-150, -50)))

                    # Change to get power up
                    if random.random() < POWER_UP_CHANCE:
                        power_ups.append(PowerUp("image/powerup.png", asteroid.rect.centerx, asteroid.rect.centery))

        # Updating power up
        for power_up in power_ups[:]:
            power_up.move()
            power_up.draw(screen)

            # detect power up and ship
            if player.rect.colliderect(power_up.rect):
                lives += 1
                power_ups.remove(power_up)

            # remove power up from screen
            if power_up.rect.top > SCREEN_HEIGHT:
                power_ups.remove(power_up)

        # draw the ship
        player.draw(screen)

        # score result
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))

        pygame.display.flip()
        clock.tick(60)

    # game over
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()

if __name__ == "__main__":
    main()
