import pygame

pygame.init()

WIDTH = 700
HEIGHT = 700
FPS = 60
COLS = 10
ROWS = 6

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (80, 175, 90)
BLUE = (60, 160, 200)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout_Game")
clock = pygame.time.Clock()


# Brick class
class Brick():
    def __init__(self):
        self.width = int(WIDTH / COLS)
        self.hieght = 30

    def create_bricks(self):
        self.bricks = []
        for r in range(ROWS):
            bricks_row = []
            for c in range(COLS):
                bricks_x = c * self.width
                bricks_y = r * self.hieght
                br = pygame.Rect(bricks_x, bricks_y, self.width, self.hieght)
                bricks_row.append(br)
            self.bricks.append(bricks_row)

    def draw_bricks(self):
        for row in self.bricks:
            for br in row:
                pygame.draw.rect(win, GREEN, br)
                pygame.draw.rect(win, BLACK, br, 2)


class Paddle():
    def __init__(self):
        self.width = int(WIDTH / COLS)
        self.height = 20
        self.x = int(WIDTH / 2) - int(self.width / 2)
        self.y = HEIGHT - 40
        self.speed = 20
        self.rec = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_paddle(self):
        pygame.draw.rect(win, WHITE, self.rec)

    def move_paddle(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rec.left > 0:
            self.rec.x -= self.speed
        if key[pygame.K_RIGHT] and self.rec.right < WIDTH:
            self.rec.x += self.speed


class Ball():
    def __init__(self, x, y):
        self.radius = 10
        self.x = x - self.radius
        self.y = y
        self.rec = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.dx = 3
        self.dy = -3
        self.game_status = 0

    def draw_circle(self):
        pygame.draw.circle(win, BLUE, (self.rec.x, self.rec.y), self.radius)

    def move_ball(self):
        if self.rec.right > WIDTH or self.rec.left < 0:
            self.dx *= -1
        if self.rec.top < 2:
            self.dy *= -1
        if self.rec.bottom > HEIGHT:
            self.game_status = -1
        # paddle_collision
        if self.rec.colliderect(paddle_obj.rec) and self.dy > 0:
            self.dy *= -1
            sound = pygame.mixer.Sound("bounce.wav")
            sound.play()

        # brick Collision
        all_done = True
        row_num = 0
        for r in brick_obj.bricks:
            col_num = 0
            for br in r:
                if self.rec.colliderect(br):
                    hit_sound = pygame.mixer.Sound('hit.wav')
                    hit_sound.play()
                    if abs(self.rec.bottom - br.top) < 5 and self.dy > 0:
                        self.dy *= -1
                    if abs(self.rec.top - br.bottom) < 5 and self.dy < 0:
                        self.dy *= -1
                    if abs(self.rec.left - br.right) < 5 and self.dx < 0:
                        self.dx *= -1
                    if abs(self.rec.right - br.left) < 5 and self.dx > 0:
                        self.dx *= -1
                    brick_obj.bricks[row_num][col_num] = (0, 0, 0, 0)
                if brick_obj.bricks[row_num][col_num] != (0,0,0,0):
                    all_done = False
                col_num += 1
            row_num += 1
        if all_done:
            self.game_status = 1
        self.rec.x += self.dx
        self.rec.y += self.dy
        return self.game_status


paddle_obj = Paddle()
ball = Ball(paddle_obj.x + int(paddle_obj.width / 2), paddle_obj.y - paddle_obj.height)
brick_obj = Brick()
brick_obj.create_bricks()
run = True
while run:
    clock.tick(FPS)
    win.fill(BLACK)
    paddle_obj.draw_paddle()
    paddle_obj.move_paddle()
    ball.draw_circle()
    brick_obj.draw_bricks()
    game_status = ball.move_ball()
    if game_status == -1:
        win.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        text = font.render('GAME OVER', True, BLUE)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        win.blit(text, text_rect)
    if game_status == 1:
        win.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        text = font.render('YOU WIN', True, BLUE)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        win.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
