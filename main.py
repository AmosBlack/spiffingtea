from operator import sub
from func import *


# initialize
pygame.init()

# screen
gui = PygUI(700, 600, "Spiffin' Tea", pygame.image.load('teapot.png'), pygame.image.load("bg.jpg"))

pygame.display.set_caption(gui.game_NAME)
pygame.display.set_icon(gui.game_LOGO)

screen = pygame.display.set_mode((gui.screen_WIDTH, gui.screen_HEIGHT))

# characters
spiff = Bird(100, 300, pygame.image.load("teacup.png"), -0.15, 0.2)
# game_vars
velocity = [0,0]
cookies = Item(pygame.image.load('cookies.png'), "cookies")
teabag = Item(pygame.image.load('teabag.png'), "teabag")
salt = Item(pygame.image.load('salt.png'), "salt")
heartz = pygame.image.load('heart.png')
heartz_max = pygame.image.load("heart_hol.png")
level_pic = pygame.image.load('level.png')
level_pic_hl = pygame.image.load('hol_level.png')
level = 0
tea_plus = 0
tea_plus_max = 5

items = []
items_x = []
items_y = []
display = "menu"

# loop
run = True

# music
get = mixer.Sound("tea_get.wav")
ouch = mixer.Sound("salt_get.wav")
cookie = mixer.Sound("cookie.wav")
jump = mixer.Sound("jump.wav")

mixer.music.load('music_8bit.mp3')
mixer.music.play(-1)

# text
game_font = pygame.font.Font('font.ttf', 28)
game_font_title = pygame.font.Font('font.ttf', 70)


# class

class Button:

    def __init__(self, x, y, width, height, text, action):
        self.x = x
        self.y = y
        self.color = {
            'inactive': (77,77,77),
            'hover': (255, 191, 155),
            'active': (190, 62, 89),
        }
        self.status = "inactive"
        self.width = width
        self.height = height
        self.text = game_font.render(text, True, (0, 0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.action = action

    def blit(self):
        rect_draw = pygame.draw.rect(screen, self.color[self.status], self.rect, 0, 5)
        screen.blit(self.text, (self.x + 70, self.y + 10))

    def interact(self):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.status = 'hover'
            if pygame.mouse.get_pressed()[0]:
                global display
                self.status = "active"
                display = self.action


        else:
            self.status = "inactive"


# buttons


play_button = Button(250, 300, 200, 50, "Play", "game")
descr_button = Button(250, 400, 200, 50, "Descr.", "descr")
tut_button = Button(250, 500, 200, 50, "Tutor.", "tutor")
replay_button = Button(250,400,200,50,"Replay","game")
menu_button = Button(250,470,200,50,"Menu","menu")

# f(x)
# item-sel
def item_sel(arr, arr_x, arr_y, items):
    num = [7, 8, 12, 15, 21, 24, 29, 31, 36]

    for item in range(items):
        if num[randint(0, 4)] % 3 == 0:
            arr.append(teabag)
        else:
            arr.append(salt)
        arr_x.append(randint(50, 650))
        arr_y.append(-randint(50, 450))


def item_create(teabag, items, items_x, items_y):
    if (teabag % 2) == 0:
        print('wood')
        for item in range(2):
            # use item_sel probability selection for cookie, salt, hot water, teabag
            items.append(teabag)
            items_x.append(randint(50, 650))
            items_y.append(-randint(50, 450))


def item_update(index, item_arr, arr_x, arr_y, teabag, cookies, salt):
    tea_prob = 11 - level
    cookie_prob = (22 - tea_prob) / 4 + tea_prob

    prob_num = randint(1, 22)

    if prob_num < tea_prob:
        item_arr[index] = teabag
    elif prob_num >= tea_prob and prob_num < cookie_prob:
        item_arr[index] = cookies
    else:
        item_arr[index] = salt

    arr_x[index] = randint(50, 650)
    arr_y[index] = -(randint(50, 250))


def spiffy_meter():
    global tea_check, meter, hearts
    if not tea_check and meter > 0:
        meter -= 0.015
    elif not tea_check and meter <= 0:
        meter = 100
        tea_check = True
        hearts -= 1
        mixer.Sound.play(ouch)

    elif tea_check:
        tea_check = False
        meter = 100


def on_collision(bird, item_x, item_y, item_arr):
    global tea_bags, hearts, tea_plus
    for item in range(len(item_arr)):
        if is_collis(bird.x, bird.y, item_x[item], item_y[item]):
            ID = item_arr[item].ID

            if ID == "cookies":
                if hearts < 5:
                    hearts += 1
                mixer.Sound.play(cookie)
            elif ID == "teabag":
                global tea_check
                tea_check = True
                tea_bags += 1
                tea_plus += 1
                mixer.Sound.play(get)
            elif ID == "salt":
                mixer.Sound.play(ouch)
                hearts -= 1

            item_update(item, item_arr, item_x, item_y, teabag, cookies, salt)


def alive(hearts):
    global run
    if hearts <= 0:
        global display
        display = 'game_over'


def re_place(items, item_x, item_y):
    for item in range(len(items)):
        if item_y[item] >= 500:
            item_update(item, items, item_x, item_y, teabag, cookies, salt)


def dimension_limit(bird):
    global hearts
    if bird.x >= 780:
        bird.x = -30
    elif bird.x <= -85:
        bird.x = 720
    if bird.y >= 470:
        bird.y = 300
        hearts -= 1
        mixer.Sound.play(ouch)
    elif bird.y <= 0:
        bird.y = 0


def reset():
    global level,tea_plus,tea_plus_max,tea_bags,items,items_x,items_y,meter,tea_check,hearts,velocity
    level = 0
    tea_plus = 0
    tea_plus_max = 5
    velocity[0] = 0
    items = []
    items_x = []
    items_y = []
    meter = 100
    tea_check = False
    tea_bags = 0
    hearts = 5
    item_sel(items,items_x,items_y,4)

def item_offset(items,items_y):
    for item in range(len(items)):
        items_y[item] += 20


item_sel(items, items_x, items_y, 4)
while run:
    # MENU
    # key-events

    if display == "menu":
        screen.fill((180, 96, 96))
        # title-text
        title = game_font_title.render("Spiffing Tea", True, (0, 0, 0))
        subtitle = game_font.render("powered by Yolkshire Tea", True, (0, 0, 0))
        screen.blit(title, (130, 100))
        screen.blit(subtitle, (280, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # button-actions
        play_button.interact()
        descr_button.interact()
        tut_button.interact()

        play_button.blit()
        descr_button.blit()
        tut_button.blit()
        #restcontrol
        over = True

    # GAME
    elif display == "game":
        if over:
            over = False
            reset()
        screen.blit(gui.game_BG, (0, 0))
        alive(hearts)
        screen.blit(spiff.img, (spiff.x, spiff.y))

        # key-press events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and meter > 0:
                    velocity[1] = spiff.jump_velo

                    mixer.Sound.play(jump)
                if event.key == pygame.K_d:
                    velocity[0] = spiff.side_velo
                if event.key == pygame.K_a:
                    velocity[0] = -spiff.side_velo
                if event.key == pygame.K_p:
                    display = "pause"
                if event.key == pygame.K_m:
                    reset()
                    display = "menu"

        # spiff-movements
        spiff.y += velocity[1]
        spiff.x += velocity[0]
        velocity[1] += g
        if velocity[0] != 0:
            if velocity[0] > 0:
                velocity[0] -= 0.0001
            if velocity[0] < 0:
                velocity[0] += 0.0001
            # jump adj

            item_move(items, items_y)
        on_collision(spiff, items_x, items_y, items)

        dimension_limit(spiff)
        spiffy_meter()

        # item_create()
        re_place(items, items_x, items_y)
        item_blit(items, items_x, items_y, screen)

        # UI
        info_bar_main = pygame.draw.rect(screen, (252, 180, 117), pygame.Rect(5, 550, 690, 45), 0, 5)
        teabag_counter = game_font.render(f"x{tea_bags}", True, (0, 0, 0))
        spiff_level = pygame.draw.rect(screen, (50, 200, 100), pygame.Rect(100, 565, meter, 20), 0, 5)
        spiff_def_level = pygame.draw.rect(screen, (50, 150, 100), pygame.Rect(100, 565, 100, 20), 2, 5)
        screen.blit(teabag_counter, (55, 560))
        screen.blit(teabag.img, (0, 538))

        # hearts
        delta_xh = 450
        for heart in range(hearts):
            x = delta_xh + 45 * heart
            screen.blit(heartz, (x, 560))

        for heart in range(hearts_max):
            x = delta_xh + 45 * heart
            screen.blit(heartz_max, (x, 560))
        hp = game_font.render(f"HP", True, (0, 0, 0))
        screen.blit(hp, (410, 560))

        # levels
        delta_xl = 270
        level_txt = game_font.render(f"Lvl {level}", True, (0, 0, 0))
        screen.blit(level_txt, (210, 560))
        for hplus in range(tea_plus_max):
            x1 = delta_xl + 25 * hplus
            screen.blit(level_pic_hl, (x1, 560))
        for plus in range(tea_plus):
            x1 = delta_xl + 25 * plus
            screen.blit(level_pic, (x1, 560))


        if (tea_plus % 5) == 0 and tea_plus > 1:
            tea_plus = 0
            level += 1
            item_sel(items, items_x, items_y, level)

    elif display == "pause":
        screen.fill((255, 244, 224))
        pause_txt = game_font_title.render("Game Paused", True, (0, 0, 0))
        tea_txt = game_font.render(f"Teabags: x{tea_bags}", True, (0, 0, 0))
        screen.blit(pause_txt, (150, 150))
        screen.blit(tea_txt, (250, 220))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        play_button.interact()
        play_button.blit()
        replay_button.blit()
        replay_button.interact()
        menu_button.blit()
        menu_button.interact()

    elif display == "game_over":
        over = True
        with open("scores.txt") as file:
            try:
                score = int(file.read())
            except:
                score = 0
            else:
                print(file.read())

            if score > tea_bags:
                file.write(tea_bags)

        screen.fill((180, 96, 96))
        game_overtxt = game_font_title.render("Game Over", True, (0, 0, 0))
        tea_txt = game_font.render(f"Teabags: x{tea_bags}", True, (0, 0, 0))
        screen.blit(game_overtxt, (170, 150))
        screen.blit(tea_txt, (270, 220))
        replay_button.blit()
        replay_button.interact()
        menu_button.blit()
        menu_button.interact()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    elif display == "tutor":
        screen.fill((255, 244, 224))
        tut_txt = game_font.render("W to Jump , A-D For left and right Lunges",True,(0,0,0))
        tut_txt1 = game_font.render("Collect Teabags and Cookies,avoid the Salt",True,(0,0,0))
        screen.blit(tut_txt,(100,200))
        screen.blit(tut_txt1,(100,250))
        menu_button.blit()
        menu_button.interact()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    elif display == "descr":
        screen.fill((237,242,174))
        menu_button.blit()
        menu_button.interact()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    pygame.display.update()
