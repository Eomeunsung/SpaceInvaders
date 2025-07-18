import pygame

from objects.beam import Beam
from objects.fighter import Fighter
from objects.alien import Alien
from constants import *

print("Startup")
pygame.init()
pygame.key.set_repeat(500, 500)
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 이미지 가로 640 세로 480
clock = pygame.time.Clock()

fighter = Fighter()
beam = None

aliens = []
for y in range(3):
    for x in range(5):
        alien = Alien()
        aliens.append(alien)
        alien.x = 70 + 50 * x
        alien.y = 100 + 70 * y

bombs = []


while True:

    #print("Update")
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            print("Shutdown")
            pygame.quit()
            exit()
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter.direction_x = -1
            if event.key == pygame.K_RIGHT:
                fighter.direction_x = +1
            if event.key == pygame.K_SPACE:
                if beam is None:
                    beam = Beam(fighter.x + fighter.image.get_width()/2 ,fighter.y)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter.direction_x = 0
            if event.key == pygame.K_RIGHT:
                fighter.direction_x = 0
            # if event.key in [pygame.K_UP, pygame.K_DOWN]:
            #     direction = 0

    delta_seconds = clock.tick(FPS) / 1000 ## FPS 만족하게끔 시간 딜레이
    fighter.update(delta_seconds)

    if beam:
        beam.update(delta_seconds)
        if beam.y < 0:
            beam = None

    for alien in aliens:
        alien.update(delta_seconds)

        bomb = alien.shoot()
        if bomb:
            bombs.append(bomb)

    for bomb in bombs:
        bomb.update(delta_seconds)
        if SCREEN_HEIGHT < bomb.y:
            bombs.remove(bomb)


    if Alien.should_change_direction:
        Alien.should_change_direction = False

        for alien in aliens:
            alien.direction_x *= -1
            alien.move(0, 50)

    #print("Render")
    surface.fill((0, 0, 0)) ##rgb 블랙색 나타냄 메서드 안에 가로를 튜플 이라고 함
    fighter.draw(surface)

    if beam:
        beam.draw(surface)
    #surface.blit(scale_up_alien_image, (alien_x, alien_y))

    for alien in aliens:
        alien.draw(surface)

    for bomb in bombs:
        bomb.draw(surface)
    pygame.display.update()
    # clock.tick(FPS)