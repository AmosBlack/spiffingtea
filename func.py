from random import randint
from math import sqrt
import pygame
from pygame import mixer

# GAME_CLASSES

from sre_constants import JUMP


class Bird:
    def __init__(self, x, y, img, jump_velo,side_velo):
        self.x = x
        self.y = y
        self.img = img
        self.jump_velo = jump_velo
        self.side_velo = side_velo

class PygUI:
    def __init__(self, screen_WIDTH, screen_HEIGHT, game_NAME, game_LOGO, game_BG):
        self.screen_WIDTH = screen_WIDTH
        self.screen_HEIGHT = screen_HEIGHT
        self.game_NAME = game_NAME
        self.game_LOGO = game_LOGO
        self.game_BG = game_BG


class Item:
    def __init__(self, img, ID):
        self.img = img
        self.ID = ID



# GAME_VARS
tea_check = False
tea_bags = 0
hearts = 5
hearts_max = 5
meter = 100
over = True

cookies = Item(pygame.image.load('cookies.png'), "cookies")
teabag = Item(pygame.image.load('teabag.png'), "teabag")
salt = Item(pygame.image.load('salt.png'), "salt")
heartz = pygame.image.load('heart.png')
heartz_max = pygame.image.load("heart_hol.png")
level_pic = pygame.image.load('level.png')
level_pic_hl = pygame.image.load('hol_level.png')

# grav-var
velocity = [0, 0]
g = 0.0001



# GAME_FUNCTIONS








# call_in_the_loop
def item_move(arr, arr_y):
    # x-movement
    for item in range(len(arr)):

        arr_y[item] += 0.07
    # bobble-movement


# detect-collision
def is_collis(x1, y1, x2, y2):
    dist = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    if dist <= 50:
        return True



# update-after-collision

# what-to-do-on-collision


# reduce spiff-update it every teabag


# blit items
def item_blit(items, item_x, item_y, display):
    for item in range(len(items)):
        display.blit(items[item].img, (item_x[item], item_y[item]))

