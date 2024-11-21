from settings import *
from sprites import Player, Ball, Opponent

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.fps = 0.0
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.paddle_sprites = pygame.sprite.Group()
        self.player = Player(pos=POS['player'], groups=(self.all_sprites, self.paddle_sprites))
        self.ball = Ball(pos=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), groups=self.all_sprites, paddle_sprites=self.paddle_sprites)
        self.opponent = Opponent(pos=POS['opponent'], ball=self.ball, groups=(self.all_sprites, self.paddle_sprites))


    def show_fps(self):
        self.fps = "%.2f" % self.clock.get_fps()
        pygame.display.set_caption("PyPong. FPS : " + str(self.fps))

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.all_sprites.update(dt)

            # draw
            self.display_surface.fill(COLORS['bg'])
            self.all_sprites.draw(self.display_surface)

            # show fps in game title
            self.show_fps()

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
