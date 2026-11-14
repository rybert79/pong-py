import pygame

pygame.init()

HEIGHT = 400
WIDTH = 900

class Bola:
    def __init__(self, x, y) -> None:
        self.x_pos = x
        self.y_pos = y
        self.speed = 180
        self.arah_x = True  # kalo true ke kanan
        self.arah_y = True  # kalo true ke bawah

    def render(self):
        pygame.draw.circle(screen, (0, 255, 0), (self.x_pos, self.y_pos), 10)

    def gerak(self, dt):
        if self.arah_x:
            self.x_pos += self.speed * dt
            pass
        else:
            self.x_pos -= self.speed * dt

        if self.arah_y:
            self.y_pos += self.speed * dt
        else:
            self.y_pos -= self.speed * dt

    def cek_collision_layar(self):
        if self.y_pos > HEIGHT - 10 or self.y_pos < 10:
            self.arah_y = not self.arah_y   

    def cek_collision_player(self, p1, p2):
        for paddle in (p1, p2):

            closest_x = max(paddle.left, min(self.x_pos, paddle.right))
            closest_y = max(paddle.top, min(self.y_pos, paddle.bottom))

            dx = self.x_pos - closest_x
            dy = self.y_pos - closest_y

            if dx * dx + dy * dy < 10 * 10:
                self.arah_x = not self.arah_x
                return

    def cek_menang(self):
        if self.x_pos < 0:
            return 2
        elif self.x_pos > 900:
            return 1

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pong")

running = True
speed = 300
player1 = pygame.Rect(30, 100, 30, 150)
player2 = pygame.Rect(840, 100, 30, 150)
bola = Bola(300, 50)

while running:
    dt = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pemenang = bola.cek_menang()
    if pemenang in [1, 2]:
        print(f"pemenangnya adalah player{pemenang}")
        running = False

    bola.gerak(dt)
    bola.cek_collision_layar()
    bola.cek_collision_player(player1, player2)
    bola.render()

    if keys[pygame.K_w]:
        player1.y -= speed * dt

    if keys[pygame.K_s]:
        player1.y += speed * dt

    if keys[pygame.K_e]:
        player2.y -= speed * dt

    if keys[pygame.K_d]:
        player2.y += speed * dt

    player1.clamp_ip(screen.get_rect())
    player2.clamp_ip(screen.get_rect())

    pygame.draw.rect(screen, (255, 0, 0), player1)
    pygame.draw.rect(screen, (0, 0, 255), player2)

    pygame.display.flip()

pygame.quit()
