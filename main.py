import pygame
from settings import *
from player import Player
from sprite_and_objects import *
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.mouse.set_visible(False)
sc_map = pygame.Surface((WIDHT // MAP_SCALE, HEIGHT // MAP_SCALE))

sprites = Sprites()
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    drawing.background(player.angle)
    walls = ray_casting(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_object])
    drawing.fps(clock)
    drawing.mini_map(player)



    pygame.display.flip()
    clock.tick()
    # print(clock.get_fps())