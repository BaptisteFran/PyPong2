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