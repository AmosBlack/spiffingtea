from sre_constants import JUMP

class Bird:
    def __init__(self, x, y, img,jump_velo):
        self.x = x
        self.y = y
        self.img = img
        self.jump_velo = jump_velo


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

