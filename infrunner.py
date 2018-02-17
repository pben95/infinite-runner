import random, pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect((100,500), (40,40))
        self.yChange = 0
        self.jumping = False
        self.score = 0
    def gravity(self):
        self.yChange += .1
        if self.rect.y > 500:
            self.rect.y = 500
            self.yChange = 0
            self.jumping = False
    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.yChange -= 6

class Block:
    def __init__(self, x, y, vel):
        self.rect = pygame.Rect((x, y), (40, 40))
        self.x, self.y = x, y
        self.vel = vel
        self.hit = False
        self.color = (random.randint(50,250),random.randint(50,250),random.randint(50,250))
    def reset(self):
        self.rect.height = 40*random.randint(1,3)
        self.rect.x, self.rect.y,  = self.x, 550 - self.rect.height
        if self.hit:
            player.score -= 1
            self.hit = False
        elif not self.hit:
            player.score += 1
        self.vel = -1 * random.randint(2,3)
        self.color = (random.randint(50,250),random.randint(50,250),random.randint(50,250))
    def move(self):
        self.rect.move_ip(self.vel,0)

player = Player()
obstacle = Block(600,500, -2)
pygame.init()
screen = pygame.display.set_mode((600, 600))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            player.jump()
    obstacle.move()
    if obstacle.rect.x < 0:
        obstacle.reset()
    if obstacle.rect.collidepoint(player.rect.x,player.rect.y) and not obstacle.hit:
        obstacle.hit = True
    player.rect.y += player.yChange
    player.gravity()
    screen.fill((0,0,0))
    screen.fill((100,0,0), player.rect)
    screen.fill(obstacle.color, obstacle.rect)
    screen.fill((255,255,255), pygame.Rect((0,540),(600,60)))
    screen.blit(pygame.font.Font(None, 24).render(str(player.score), False, (0, 0, 0), (255, 255, 255)), (0, 0))
    pygame.display.flip()