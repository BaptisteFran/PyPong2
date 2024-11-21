from random import choice, uniform

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.surf = pygame.Surface(SIZE['paddle'])
        self.surf.fill(COLORS['paddle'])
        self.rect = self.surf.get_frect(center=pos)
        self.image = self.surf
        self.direction = pygame.Vector2()

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.y = int(keys[pygame.K_s] - int(keys[pygame.K_z]))

    def move(self, dt):
        if (self.rect.top < 0 and self.direction.y == -1) or (self.rect.bottom > WINDOW_HEIGHT and self.direction.y == 1):
            self.direction.y = 0
        self.rect.centery += self.direction.y * SPEED['player'] * dt

    def update(self, dt):
        self.input()
        self.move(dt)

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos ,groups):
        super().__init__(groups)
        self.image = pygame.Surface(SIZE['ball'])
        self.image.fill(COLORS['ball'])
        self.rect = self.image.get_frect(center=pos)
        self.direction = pygame.Vector2(choice((-1, 1)), uniform(0.7, 0.8) * choice((-1, 1)))

    def move(self, dt):
        self.rect.center += self.direction * SPEED['ball'] * dt

    def wall_collision(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1

        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1

        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x *= -1

        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.direction.x *= -1


    def update(self, dt):
        self.move(dt)
        self.wall_collision()