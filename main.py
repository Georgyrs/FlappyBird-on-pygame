import pygame
import random
import pyglet as s
pygame.init()
screen_width, screen_height = 350, 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')


backgroundday = pygame.image.load("Material/background-day.png")
backgroundnight = pygame.image.load("Material/background-night.png")
birdanimation = [pygame.image.load("Material/redbird-downflap.png"), pygame.image.load("Material/redbird-midflap.png"),
                 pygame.image.load("Material/redbird-upflap.png")]
pipe_image = pygame.image.load("Material/pipe-red.png")
gameover = pygame.image.load("Material/gameover.png")
floor = pygame.image.load("Material/base.png")
pipedown = pygame.image.load("Material/pipereddown.png")
message = pygame.image.load("Material/message.png")
digits = [pygame.image.load(f"Material/{i}.png") for i in range(10)]

backgroundday1 = pygame.transform.scale(backgroundday, (screen_width, screen_height))
backgroundnight1 = pygame.transform.scale(backgroundnight, (screen_width, screen_height))
floor1 = pygame.transform.scale(floor, (400, 112))
score = 0
max_score = 0
music = s.media.load("Material/bcmusic.mp3")
point_sound = pygame.mixer.Sound("Material/point.wav")
swoosh_sound = pygame.mixer.Sound("Material/swoosh.wav")
wing_sound = pygame.mixer.Sound("Material/wing.wav")
hit_sound = pygame.mixer.Sound("Material/hit.wav")
die_sound = pygame.mixer.Sound("Material/die.wav")
bcmusic = pygame.mixer.Sound("Material/bcmusic.mp3")
clock = pygame.time.Clock()
pipes = []
pipesup = []
BLACK = (0, 0, 0)
time = 0
bird_y = 300
birdv = 0
gravity = 0.25
jump = -5
collisiontime = 0
score1 = pygame.font.Font(None, 30)
run = False
bird = pygame.image.load("Material/redbird-midflap.png")
running = True
show_message = True
showmessage = True
cycle = True
collision = True
time_counter = 0
sound = 1
YELLOW = (255, 255, 0)
music.play()
print(type(score), type(max_score))
try:
    with open("max_score.txt", "r") as file:

        max_score = str(file.read())
except FileNotFoundError:
    pass
while running:
    with open("max_score.txt", "w") as file:
         file.write(str(max_score))
    with open("max_score.txt", "r") as file:
        score2 = score1.render('Рекорд: ' + str(file.read()), True, YELLOW )
    time += 1
    time_counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            wing_sound.play()
            birdv = jump
            if show_message:
                show_message = False
                birdv = jump

    if time == 150:
        time = 0
        pipe_height = random.randint(250, 300)
        pipedown_height = random.randint(-200, -150)
        pipes.append(pygame.Rect(screen_width, pipe_height, pipe_image.get_width(), pipe_image.get_height()))
        pipesup.append(pygame.Rect(screen_width, pipedown_height, pipedown.get_width(), pipedown.get_height()))

    if not show_message:
        birdv += gravity
        bird_y += birdv
    bird_rect = pygame.Rect(155, bird_y, bird.get_width(), bird.get_height())
    bird_index = (pygame.time.get_ticks() // 100) % 3
    bird = birdanimation[bird_index]
    if time_counter % 160 == 0:
        score += 1
        if int(score) > int(max_score):
            max_score = score
        if time_counter // 160 == 10:
            time_counter = 0
        else:
            time_counter = (time_counter // 160) * 160
    screen.blit(backgroundday1, (0, 0))
    screen.blit(floor1, (0, 400))
    if show_message:
        screen.blit(message, (80, 80))
    else:
        screen.blit(bird, (155, bird_y))
    if cycle:
        for i in pipes:
            i[0] -= 1
        for g in pipesup:
            g[0] -= 1

    for i in pipes:
        screen.blit(pipe_image, (i[0], i[1]))
    for g in pipesup:
        screen.blit(pipedown, (g[0], g[1]))

    for pipe_rect in pipes:
        if bird_rect.colliderect(pipe_rect):
            if bird_rect.colliderect(pipe_rect):
                cycle = False
                gravity = 1
                score = 0
                jump = 0
                birdv = 0
                current_digit = 0
                time_counter = 0
                if sound == 1:
                    die_sound.play()
                    hit_sound.play()
                    sound = 0
                if not collision:
                   collision = True
                   die_sound.play()
                   hit_sound.play()
                   collision = False
            if bird_rect.colliderect(pipe_rect):
               screen.blit(gameover, (70, 256))
               current_digit = 0
               score = 0
               time_counter = 0
               if sound == 1:
                   die_sound.play()
                   hit_sound.play()
                   sound = 0
               if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                   if showmessage:
                       showmessage = False
                       birdv = jump
                   if not show_message:
                       birdv += gravity
                       bird_y += birdv
                       cycle = True
                       gravity = 0.25
                       jump = -5
                       bird_y = 300
                       pipes = []
                       pipesup = []
                       bird_y = 300
                       birdv += gravity
                       bird_y += birdv
                       sound = 1
    for pipe_rect in pipesup:
        if bird_rect.colliderect(pipe_rect):
           cycle = False
           score = 0
           current_digit = 0
           time_counter = 0
           jump = 0
           birdv = 0
           gravity = 1
           if sound == 1:
               die_sound.play()
               hit_sound.play()
               sound = 0
               current_digit = 0
               time_counter = 0
        if bird_rect.colliderect(pipe_rect):
            current_digit = 0
            score = 0
            time_counter = 0
            if sound == 1:
                die_sound.play()
                hit_sound.play()
                sound = 0
                current_digit = 0
                time_counter = 0
            screen.blit(gameover, (70, 256))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if showmessage:
                   showmessage = False
                   birdv = jump
                if not show_message:
                    birdv += gravity
                    bird_y += birdv
                    cycle = True
                    gravity = 0.25
                    jump = -5
                    bird_y = 300
                    pipes = []
                    pipesup = []
                    bird_y = 300
                    birdv += gravity
                    bird_y += birdv
                    sound = 1
    screen.blit(score2, (0, 0))
    print("1", max_score)
    current_digit = (time_counter // 160) % 10
    screen.blit(digits[current_digit], (160, 40))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()