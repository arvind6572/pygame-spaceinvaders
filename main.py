import pygame
import random
from pygame import  mixer
pygame.init()
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((600, 600))
pygame.font.init()
my_font = pygame.font.Font('freesansbold.ttf', 30)
score_val = 0

# UFO-------------------------------------------
ufo = []
ufo_x = []
ufo_y = []
ufo_y_change = []
ufo_x_change = []
num_of_enemies = 3
for i in range(num_of_enemies):
    ufo.append(pygame.image.load("ufo.png"))
    ufo_x.append(random.randint(0, 600))
    ufo_y.append(random.randint(0, 100))
    ufo_x_change.append(1)
    ufo_y_change.append(5)

# ----------------------------------------------
# Player
player = pygame.image.load("space-invaders.png")
player_x = 220
player_y = 570
player_x_change = 0
player_y_change = 0
# ----------------------------------------------

# bullets---------------------------------------
bullet = pygame.image.load("bullet.png")
bullet_x = player_x - 100
bullet_y = player_y - 10
bullet_x_change = 0
bullet_y_change = -5

background = pygame.image.load("155.jpg")
running = True
i = 0
my_font2 = pygame.font.Font('freesansbold.ttf', 40)


def game_over_foo():
    final_score = my_font2.render("Final score: " + str(score_val), True, (255, 255, 255))
    screen.blit(final_score, (150, 200))


def my_score():
    score = my_font.render("score : " + str(score_val), True,  (255, 255, 255))
    screen.blit(score, (10, 10))


def ufo_move(x, y):
    screen.blit(ufo[i], (x, y))


def player_move(x, y):
    screen.blit(player, (x, y))


def bullets_move(x, y):
    screen.blit(bullet, (x, y))


bullet_morn = False
player_left = False
player_right = False
end_score = 0

while running:
    screen.blit(background, (0, 0))
    screen.blit(bullet, (bullet_x, bullet_y))
    screen.blit(player, (player_x, player_y))
    for i in range(num_of_enemies):
        screen.blit(ufo[i], (ufo_x[i], ufo_y[i]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_morn = True
            if event.key == pygame.K_LEFT:
                player_left = True
            if event.key == pygame.K_RIGHT:
                player_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_left = False
                player_right = False

    # player------------------------------
    if player_right:
        player_x_change = 2
    elif player_left:
        player_x_change = -2
    else:
        player_x_change = 0

    if 570 >= player_x + player_x_change >= 0:
        player_x += player_x_change
        player_move(player_x, player_y)

    # ufo --------------------------------

    for i in range(num_of_enemies):
        if 570 <= ufo_x[i] < 1500:
            ufo_x_change[i] = -1
            ufo_y_change[i] = 20
        elif ufo_x[i] <= 0:
            ufo_x_change[i] = 1
            ufo_y_change[i] = 5
        elif 5 < ufo_x[i] < 590:
            ufo_y_change[i] = 0

        ufo_x[i] += ufo_x_change[i]
        ufo_y[i] += ufo_y_change[i]
        ufo_move(ufo_x[i], ufo_y[i])
        if ufo_y[i] >= 530:
            for j in range(num_of_enemies):
                ufo_x[j] = 2000
                ufo_y[j] = 2000
                game_over_foo()

        if bullet_x - 20 <= ufo_x[i] <= bullet_x + 20:
            if bullet_y - 20 <= ufo_y[i] <= bullet_y + 20:
                (ufo_x[i], ufo_y[i]) = (random.randint(0, 600), random.randint(0, 100))
                score_val += 1
                bullet_y = player_y
                bullet_morn = False
                # explosion sound--------------------------------------------
                hit_sound = mixer.music.load("explosion.wav")
                mixer.music . play()

    # bullet -------------------------------
    if bullet_morn:
        if bullet_y == player_y - 10:
            shoot_sound = mixer.music.load("shoot.wav")
            mixer.music.play()
        bullet_y += bullet_y_change

    if bullet_y == 0:
        bullet_morn = False
        bullet_x = player_x
        bullet_y = player_y

    if not bullet_morn:
        bullet_x = player_x+8
        bullet_y = player_y

    bullets_move(bullet_x, bullet_y)
    my_score()
    pygame.display.update()
