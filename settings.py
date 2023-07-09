import math

#setting and display
WIDHT = 1200
HEIGHT = 800
HALF_WIDHT = WIDHT // 2
HALF_HEIGHT = HEIGHT // 2
DOUBLE_HEIGHT = 2 * HEIGHT
FPS = 90
TILE = 60
FPS_POS = (WIDHT - 65, 5)



#texture setting (1024x1024)
TEXTURE_WIDHT = 1024
TEXTURE_HEIGHT = 1024
TEXTURE_SCALE = TEXTURE_WIDHT // TILE


#minimap setting
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HALF_WIDHT // MAP_SCALE)

#ray casting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 400
MAX_DEPTH = 1100
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 2 * DIST * TILE
SCALE = WIDHT // NUM_RAYS

#sprite settings
DOUBLE_PI = 2 * math.pi
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

#player
player_pos = (HALF_WIDHT, HALF_HEIGHT)
player_angle = 0
player_speed = 1


#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 225)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 166, 255)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)