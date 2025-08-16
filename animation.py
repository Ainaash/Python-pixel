import pygame
from pygame.examples.moveit import WIDTH, HEIGHT

pygame .init()

WIDTH= 640
HEIGHT=640

screen =pygame. display.set_mode((WIDTH, HEIGHT))

x=60
y=60

speed_x=10
speed_y=10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    x+=speed_x
    y+=speed_y

    if x> WIDTH or x<0:
        speed_x= speed_x=-1

    if y> HEIGHT or y< 0:
        speed_y = speed_y=-1

    screen.fill(("blue"))

    pygame.draw.circle(screen, "green", (x,y), 60)

    pygame.display.update()
    pygame.time.delay(40)

