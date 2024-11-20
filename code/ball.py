from settings import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos ,groups):
        super().__init__(groups)
        self.surf = pygame.Surface(SIZE['ball'])
        self.surf.fill(COLORS['ball'])
        self.rect = self.surf.get_frect(center=pos)
        self.image = self.surf
        self.direction = pygame.Vector2(1, 1)

    def move(self, dt):
        if self.rect.right > WINDOW_WIDTH or self.rect.left < 0:
            self.direction.x = -self.direction.x
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
            self.direction.y = -self.direction.y
        self.rect.center += self.direction * SPEED['ball'] * dt

    def update(self, dt):
        self.move(dt)