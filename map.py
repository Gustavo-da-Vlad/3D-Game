from settings import *

text_map = [
    'SSSSSSSSSSSSSSSSSSSSSS',
    'SS......SS..SS.....SSS',
    'SSSSS..............SSS',
    'SSSS....DDDDDD....SSSS',
    'S.......DDD.......SSSS',
    'S...DD....DD...D..SSSS',
    'S...DDDDD.........SSSS',
    'S...............SSSSSS',
    'SSSSSSSSSSSSSSSSSSSSSS'
]

world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == 'D':
                world_map[(i * TILE, j * TILE)] = 'D'
            elif char == 'S':
                world_map[(i * TILE, j * TILE)] = 'S'