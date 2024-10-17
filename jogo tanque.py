import pygame
import sys

# Configurações iniciais
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo de Tanques")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# FPS
clock = pygame.time.Clock()
tank_speed = 5
bullet_speed = 10

# Classes para o jogo
class Tank:
    def __init__(self, x, y, color, controls):
        self.x = x
        self.y = y
        self.color = color
        self.width = 40
        self.height = 40
        self.controls = controls
        self.speed = tank_speed

    def move(self, keys):
        if keys[self.controls["left"]]:
            self.x -= self.speed
        if keys[self.controls["right"]]:
            self.x += self.speed
        if keys[self.controls["up"]]:
            self.y -= self.speed
        if keys[self.controls["down"]]:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Bullet:
    def __init__(self, x, y, direction, color):
        self.x = x
        self.y = y
        self.direction = direction
        self.color = color
        self.width = 5
        self.height = 10

    def move(self):
        if self.direction == "up":
            self.y -= bullet_speed
        elif self.direction == "down":
            self.y += bullet_speed
        elif self.direction == "left":
            self.x -= bullet_speed
        elif self.direction == "right":
            self.x += bullet_speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Função principal do jogo
def game_loop():
    running = True
    bullets = []

    # Criando os tanques
    tank1_controls = {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s, "shoot": pygame.K_SPACE}
    tank1 = Tank(100, 300, RED, tank1_controls)

    tank2_controls = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP, "down": pygame.K_DOWN, "shoot": pygame.K_RETURN}
    tank2 = Tank(600, 300, BLUE, tank2_controls)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Movimentação dos tanques
        tank1.move(keys)
        tank2.move(keys)

        # Disparo dos tanques
        if keys[tank1.controls["shoot"]]:
            bullets.append(Bullet(tank1.x + tank1.width // 2, tank1.y, "up", RED))

        if keys[tank2.controls["shoot"]]:
            bullets.append(Bullet(tank2.x + tank2.width // 2, tank2.y, "down", BLUE))

        # Movimento dos projéteis
        for bullet in bullets[:]:
            bullet.move()
            if bullet.y < 0 or bullet.y > screen_height or bullet.x < 0 or bullet.x > screen_width:
                bullets.remove(bullet)

        # Desenho da tela
        screen.fill(WHITE)
        tank1.draw(screen)
        tank2.draw(screen)

        for bullet in bullets:
            bullet.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()