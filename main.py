import pygame
import sys
import sqlite3

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)
fps = 60

pygame.mixer.init()
pygame.mixer.music.load('папка пнг/bg_music.mp3')
pygame.mixer.music.play(-1, 0.0)
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

def setupRoomOne(all_sprites_list):
    wall_list = pygame.sprite.RenderPlain()
    walls = [[0, 0, 10, 750],
             [0, 0, 800, 10],
             [0, 740, 800, 10],
             [800, 0, 10, 750],
             [390, 0, 6, 125],
             [390, 125, 39, 6],
             [423, 0, 6, 125],
             [755, 60, 6, 65],
             [630, 60, 6, 65],
             [630, 60, 130, 6],
             [630, 125, 131, 6],
             [480, 60, 6, 65],
             [480, 60, 97, 6],
             [480, 125, 101, 6],
             [575, 60, 6, 65],
             [60, 60, 6, 65],
             [60, 60, 130, 6],
             [185, 60, 6, 65],
             [60, 125, 131, 6],
             [240, 60, 6, 65],
             [240, 60, 97, 6],
             [335, 60, 6, 65],
             [240, 125, 101, 6],
             [60, 175, 6, 15],
             [60, 175, 130, 6],
             [185, 175, 6, 15],
             [60, 190, 131, 6],
             [0, 240, 188, 6],
             [0, 485, 191, 6],
             [185, 240, 6, 245],
             [60, 530, 126, 6],
             [60, 530, 6, 20],
             [60, 550, 95, 6],
             [180, 535, 6, 105],
             [151, 550, 6, 90],
             [151, 640, 35, 6],
             [0, 600, 90, 6],
             [0, 640, 90, 6],
             [90, 600, 6, 46],
             [60, 683, 180, 6],
             [60, 683, 6, 20],
             [60, 698, 280, 6],
             [240, 600, 6, 89],
             [240, 600, 36, 6],
             [276, 600, 6, 89],
             [276, 683, 64, 6],
             [334, 683, 6, 20],
             [630, 240, 190, 6],
             [630, 240, 6, 245],
             [630, 485, 190, 6],
             [630, 175, 130, 6],
             [630, 175, 6, 15],
             [630, 190, 131, 6],
             [755, 175, 6, 15],
             [630, 530, 126, 6],
             [630, 530, 6, 110],
             [630, 640, 35, 6],
             [661, 550, 6, 96],
             [661, 550, 95, 6],
             [750, 530, 6, 20],
             [720, 600, 90, 6],
             [720, 600, 6, 46],
             [720, 640, 90, 6],
             [480, 698, 280, 6],
             [480, 683, 6, 20],
             [480, 683, 60, 6],
             [536, 600, 6, 89],
             [536, 600, 36, 6],
             [572, 600, 6, 89],
             [572, 683, 185, 6],
             [754, 683, 6, 20],
             [391, 698, 36, 6],
             [330, 600, 155, 6],
             [330, 600, 6, 36],
             [330, 636, 67, 6],
             [391, 636, 6, 67],
             [485, 600, 6, 36],
             [421, 636, 70, 6],
             [421, 636, 6, 67],
             [391, 545, 37, 6],
             [391, 480, 6, 70],
             [423, 480, 6, 70],
             [330, 480, 67, 6],
             [330, 450, 6, 36],
             [330, 450, 155, 6],
             [423, 480, 65, 6],
             [485, 450, 6, 36],
             [330, 330, 60, 6],
             [330, 390, 158, 6],
             [330, 330, 6, 66],
             [432, 330, 56, 6],
             [482, 330, 6, 63],
             [330, 175, 6, 40],
             [330, 175, 158, 6],
             [483, 175, 6, 40],
             [330, 210, 65, 6],
             [420, 210, 68, 6],
             [420, 210, 6, 70],
             [390, 210, 6, 70],
             [390, 280, 36, 6],
             [480, 550, 100, 6],
             [480, 535, 6, 20],
             [480, 535, 100, 6],
             [574, 535, 6, 20],
             [240, 550, 100, 6],
             [240, 535, 6, 20],
             [240, 535, 100, 6],
             [334, 535, 6, 20],
             [540, 390, 36, 6],
             [540, 390, 6, 100],
             [540, 484, 36, 6],
             [570, 390, 6, 100],
             [240, 390, 36, 6],
             [240, 390, 6, 100],
             [240, 484, 36, 6],
             [270, 390, 6, 100],
             [540, 175, 36, 6],
             [540, 175, 6, 94],
             [570, 175, 6, 160],
             [540, 330, 36, 6],
             [480, 264, 6, 20],
             [480, 264, 64, 6],
             [480, 278, 64, 6],
             [540, 278, 6, 58],
             [240, 175, 36, 6],
             [240, 175, 6, 160],
             [270, 175, 6, 94],
             [240, 329, 36, 6],
             [270, 263, 70, 6],
             [334, 263, 6, 20],
             [270, 277, 70, 6],
             [270, 277, 6, 58],
             ]

    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    return wall_list

def setupGate(all_sprites_list):
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(390, 332, 42, 2, white))
    all_sprites_list.add(gate)
    return gate

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert()

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y

    def prevdirection(self):
        self.prev_x = self.change_x
        self.prev_y = self.change_y

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self, walls, gate):
        old_x = self.rect.left
        new_x = old_x + self.change_x
        prev_x = old_x + self.prev_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y
        prev_y = old_y + self.prev_y

        x_collide = pygame.sprite.spritecollide(self, walls, False)
        if x_collide:
            self.rect.left = old_x
        else:
            self.rect.top = new_y
            y_collide = pygame.sprite.spritecollide(self, walls, False)
            if y_collide:
                self.rect.top = old_y

        if gate != False:
            gate_hit = pygame.sprite.spritecollide(self, gate, False)
            if gate_hit:
                self.rect.left = old_x
                self.rect.top = old_y

class Ghost(Player):
    def changespeed(self, list, ghost, turn, steps, l):
        try:
            z = list[turn][2]
            if steps < z:
                self.change_x = list[turn][0]
                self.change_y = list[turn][1]
                steps += 1
            else:
                if turn < l:
                    turn += 1
                elif ghost == "clyde":
                    turn = 2
                elif ghost == "pinky":
                    turn = 2
                elif ghost == "blinky":
                    turn = 2
                elif ghost == "inky":
                    turn = 2
                else:
                    turn = 0
                self.change_x = list[turn][0]
                self.change_y = list[turn][1]
                steps = 0
            return [turn, steps]
        except IndexError:
            return [0, 0]


Pinky_directions = [
    [4, 0, 5],
    [0, -4, 13],
    [-10, 0, 10],
    [0, 10, 19],
    [-6, 0, 13],
    [0, -10, 46],
    [-6, 0, 28],
    [0, 8, 14],
    [8, 0, 20],
    [0, 8, 6],
    [-8, 0, 20],
    [0, -8, 6],
    [8, 0, 20],
    [0, -8, 14],
    [8, 0, 19],
    [0, 8, 14],
    [8, 0, 16],
    [0, 8, 10],
    [-8, 0, 6],
    [0, 8, 7],
    [8, 0, 7],
    [0, 8, 14],
    [-8, 0, 25],
    [0, -8, 6],
    [-8, 0, 10],
    [0, -8, 26],
    [8, 0, 9],
    [0, 8, 9],
    [8, 0, 7],
    [0, 8, 8],
    [8, 0, 5],
]

Blinky_directions = [
    [4, 0, 5],
    [0, -4, 13],
    [8, 0, 4],
    [0, -8, 7],
    [8, 0, 7],
    [0, -8, 10],
    [-8, 0, 6],
    [0, -8, 14],
    [8, 0, 40],
    [0, 8, 14],
    [-8, 0, 21],
    [0, 8, 7],
    [8, 0, 21],
    [0, -8, 22],
    [-8, 0, 21],
    [0, 8, 40],
    [-8, 0, 10],
    [0, 8, 17],
    [-8, 0, 7],
    [0, 8, 7],
    [-8, 0, 10],
    [0, -8, 7],
    [-8, 0, 19],
    [0, -8, 16],
    [8, 0, 10],
    [0, -8, 7],
    [8, 0, 13],
]

Inky_directions = [
    [4, 0, 5],
    [0, -4, 13],
    [8, 0, 12],
    [0, 8, 25],
    [8, 0, 10],
    [0, 8, 7],
    [-8, 0, 10],
    [0, 8, 10],
    [-8, 0, 7],
    [0, 8, 7],
    [-8, 0, 51],
    [0, -8, 7],
    [8, 0, 21],
    [0, -8, 10],
    [8, 0, 30],
    [0, -8, 7],
    [8, 0, 39],
    [0, 8, 7],
    [-8, 0, 12],
    [0, 8, 11],
    [8, 0, 11],
    [0, 8, 7],
    [-8, 0, 51],
    [0, -8, 6],
    [-8, 0, 6],
    [0, -8, 10],
    [-8, 0, 10],
    [0, -8, 7],
    [8, 0, 10],
    [0, -8, 25],
    [8, 0, 12],
]

Clyde_directions = [
    [4, 0, 5],
    [0, -4, 13],
    [8, 0, 12],
    [0, 8, 14],
    [-8, 0, 25],
    [0, 8, 10],
    [-8, 0, 33],
    [0, 8, 7],
    [8, 0, 10],
    [0, 8, 10],
    [8, 0, 10],
    [0, -8, 10],
    [8, 0, 11],
    [0, 8, 10],
    [8, 0, 7],
    [0, 8, 7],
    [8, 0, 52],
    [0, -8, 7],
    [-8, 0, 21],
    [0, -8, 19],
    [-8, 0, 17],
    [0, 8, 9],
    [8, 0, 6],
    [0, 8, 10],
    [-8, 0, 7],
    [0, 8, 7],
    [-8, 0, 52],
    [0, -8, 7],
    [8, 0, 11],
    [0, -8, 11],
    [-8, 0, 10],
    [0, -8, 9],
    [8, 0, 22],
    [0, -8, 19],
    [8, 0, 10],
    [0, -8, 7],
    [8, 0, 12],
]

pl = len(Pinky_directions) - 1
bl = len(Blinky_directions) - 1
il = len(Inky_directions) - 1
cl = len(Clyde_directions) - 1

class ImageButton:
    def __init__(self, x, y, width, height, text, image_normal, image_hover):
        self.rect = pygame.Rect(x, y, width, height)
        self.image_normal = pygame.image.load(image_normal)
        self.image_hover = pygame.image.load(image_hover)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.text_rect = None
        self.image_rect = None
        self.update_text_and_image()

    def update_text_and_image(self):
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_width, text_height = text_surface.get_size()
        self.text_rect = pygame.Rect(
            self.rect.x + (self.rect.width - text_width) // 2,
            self.rect.y + (self.rect.height - text_height) // 2,
            text_width,
            text_height
        )
        self.image_rect = self.image_normal.get_rect(center=self.rect.center)

    def check_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def draw(self, screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.image_hover,
                        self.image_rect)
        else:
            screen.blit(self.image_normal, self.image_rect)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))

    def move(self, dx, dy):
        self.rect.move_img(dx, dy)
        self.text_rect.move_mg(dx, dy)
        self.image_rect.move_img(dx, dy)

pygame.init()
Width = 810
Height = 750
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Pacman')
main_background = pygame.image.load('папка пнг/background.png')


def main_menu():
    start_button = ImageButton(Width / 2 - (252 / 2), 250, 252, 74, "Новая игра", "папка пнг/beforebluebutton.png",
                               "папка пнг/afterbluebutton.png")
    record_button = ImageButton(Width / 2 - (252 / 2), 350, 252, 74, "Рекорды", "папка пнг/beforeyellowbutton.png",
                                "папка пнг/afteryellowbutton.png")
    exit_button = ImageButton(Width / 2 - (252 / 2), 450, 252, 74, "Выйти", "папка пнг/beforegreenbutton.png",
                              "папка пнг/aftergreenbutton.png")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (100, -120))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Меню", True, (255, 255, 0))
        text_rect = text_surface.get_rect(center=(Width / 2, 100))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == record_button:
                record()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == start_button:
                startGame()
            for btn in [start_button, record_button, exit_button]:
                btn.handle_event(event)
        for btn in [start_button, record_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        pygame.display.flip()


conn = sqlite3.connect("pacman_highscores.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS highscores(score INT);""")
conn.commit()


def get_top_scores():
    cursor.execute("SELECT score FROM highscores ORDER BY score DESC LIMIT 5")
    return cursor.fetchall()


def display_high_scores():
    top_scores = get_top_scores()

    font = pygame.font.Font(None, 72)
    y_position = 200

    for i, score in enumerate(top_scores, start=1):
        score_text = f"{i}. {score[0]}"
        score_surface = font.render(score_text, True, (255, 255, 0))
        score_rect = score_surface.get_rect(center=(Width / 4, y_position))
        screen.blit(score_surface, score_rect)
        y_position += 100


def record():
    exit_button = ImageButton(Width / 2 - (252 / 2), 450, 252, 504, "Выйти", "папка пнг/beforegreenbutton.png",
                              "папка пнг/aftergreenbutton.png")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (100, -120))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Рекорды", True, (255, 255, 0))
        text_rect = text_surface.get_rect(center=(Width / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                main_menu()
            for btn in [exit_button]:
                btn.handle_event(event)
        for btn in [exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        display_high_scores()
        pygame.display.flip()
    conn.close()

background = pygame.Surface(screen.get_size())

background = background.convert()

background.fill(black)

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("папка пнг/freesansbold.ttf", 24)

w = 378
h_p = 407
h = 346


def startGame():
    all_sprites_list = pygame.sprite.RenderPlain()

    block_list = pygame.sprite.RenderPlain()

    monsta_list = pygame.sprite.RenderPlain()

    pacman_collide = pygame.sprite.RenderPlain()

    wall_list = setupRoomOne(all_sprites_list)

    gate = setupGate(all_sprites_list)

    p_turn = 0
    p_steps = 0

    b_turn = 0
    b_steps = 0

    i_turn = 0
    i_steps = 0

    c_turn = 0
    c_steps = 0

    Pacman = Player(w, h_p, "папка пнг/pacman.png")
    all_sprites_list.add(Pacman)
    pacman_collide.add(Pacman)

    Blinky = Ghost(w, h, "папка пнг/Blinky.png")
    monsta_list.add(Blinky)
    all_sprites_list.add(Blinky)

    Pinky = Ghost(w, h, "папка пнг/Pinky.png")
    monsta_list.add(Pinky)
    all_sprites_list.add(Pinky)

    Inky = Ghost(w, h, "папка пнг/Inky.png")
    monsta_list.add(Inky)
    all_sprites_list.add(Inky)

    Clyde = Ghost(w, h, "папка пнг/Clyde.png")
    monsta_list.add(Clyde)
    all_sprites_list.add(Clyde)

    for row in range(24):
        for column in range(26):
            if ((column == 0 and (
                    row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 19 or row == 20))
                    or (column == 1 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 22))
                    or (column == 2 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 22))
                    or (column == 3 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 22))
                    or (column == 4 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 18 or row == 19 or row == 20 or row == 22))
                    or (column == 5 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 18 or row == 19 or row == 20 or row == 22))
                    or (column == 6 and row == 22)
                    or (column == 7 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 6 or row == 7 or row == 8 or row == 9 or row == 10 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 21 or row == 22))
                    or (column == 8 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 6 or row == 7 or row == 8 or row == 9 or row == 10 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 21 or row == 22))
                    or (column == 9 and (row == 1 or row == 2 or row == 3 or row == 8 or row == 17 or row == 22))
                    or (column == 10 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 6 or row == 8 or row == 10 or row == 11 or row == 12 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 22))
                    or (column == 11 and (
                            row == 5 or row == 6 or row == 10 or row == 11 or row == 12 or row == 14 or row == 15 or row == 19 or row == 20))
                    or (column == 12 and (
                            row == 0 or row == 1 or row == 2 or row == 3 or row == 5 or row == 6 or row == 7 or row == 8 or row == 10 or row == 11 or row == 12 or row == 14 or row == 15 or row == 16 or row == 17 or row == 19 or row == 20 or row == 21 or row == 22))
                    or (column == 13 and (
                            row == 0 or row == 1 or row == 2 or row == 3 or row == 5 or row == 6 or row == 7 or row == 8 or row == 10 or row == 11 or row == 12 or row == 14 or row == 15 or row == 16 or row == 17 or row == 19 or row == 20 or row == 21 or row == 22))
                    or (column == 14 and (
                            row == 5 or row == 6 or row == 10 or row == 11 or row == 12 or row == 14 or row == 15 or row == 19 or row == 20))
                    or (column == 15 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 6 or row == 8 or row == 10 or row == 11 or row == 12 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 22))
                    or (column == 16 and (row == 1 or row == 2 or row == 3 or row == 8 or row == 17 or row == 22))
                    or (column == 17 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 6 or row == 7 or row == 8 or row == 9 or row == 10 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 21 or row == 22))
                    or (column == 18 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 6 or row == 7 or row == 8 or row == 9 or row == 10 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 21 or row == 22))
                    or (column == 19 and row == 22)
                    or (column == 20 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 18 or row == 19 or row == 20 or row == 22))
                    or (column == 21 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 18 or row == 19 or row == 20 or row == 22))
                    or (column == 22 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 22))
                    or (column == 23 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 22))
                    or (column == 24 and (
                            row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 22))
                    or (column == 25 and (
                            row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 19 or row == 20))
            ):
                continue
            else:
                block = Block(yellow, 4, 4)

                block.rect.x = (30 * column + 6) + 26
                block.rect.y = (30 * row + 6) + 26

                b_collide = pygame.sprite.spritecollide(block, wall_list, False)
                p_collide = pygame.sprite.spritecollide(block, pacman_collide, False)
                if b_collide:
                    continue
                elif p_collide:
                    continue
                else:
                    block_list.add(block)
                    all_sprites_list.add(block)

    bll = len(block_list)

    score = 0

    done = False

    i = 0

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Pacman.changespeed(-15, 0)
                if event.key == pygame.K_RIGHT:
                    Pacman.changespeed(15, 0)
                if event.key == pygame.K_UP:
                    Pacman.changespeed(0, -15)
                if event.key == pygame.K_DOWN:
                    Pacman.changespeed(0, 15)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Pacman.changespeed(15, 0)
                if event.key == pygame.K_RIGHT:
                    Pacman.changespeed(-15, 0)
                if event.key == pygame.K_UP:
                    Pacman.changespeed(0, 15)
                if event.key == pygame.K_DOWN:
                    Pacman.changespeed(0, -15)

        Pacman.update(wall_list, gate)

        returned = Pinky.changespeed(Pinky_directions, "pinky", p_turn, p_steps, pl)
        p_turn = returned[0]
        p_steps = returned[1]
        Pinky.changespeed(Pinky_directions, "pinky", p_turn, p_steps, pl)
        Pinky.update(wall_list, False)

        returned = Blinky.changespeed(Blinky_directions, "blinky", b_turn, b_steps, bl)
        b_turn = returned[0]
        b_steps = returned[1]
        Blinky.changespeed(Blinky_directions, "blinky", b_turn, b_steps, bl)
        Blinky.update(wall_list, False)

        returned = Inky.changespeed(Inky_directions, "inky", i_turn, i_steps, il)
        i_turn = returned[0]
        i_steps = returned[1]
        Inky.changespeed(Inky_directions, "inky", i_turn, i_steps, il)
        Inky.update(wall_list, False)

        returned = Clyde.changespeed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        c_turn = returned[0]
        c_steps = returned[1]
        Clyde.changespeed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        Clyde.update(wall_list, False)

        blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)

        if len(blocks_hit_list) > 0:
            score += len(blocks_hit_list)
        monsta_hit_list = pygame.sprite.spritecollide(Pacman, monsta_list, False)

        if monsta_hit_list:
            mass_list = []
            mass_list.append(score)
            data_base = sqlite3.connect('pacman_highscores.db')
            cur = data_base.cursor()
            cur.execute("INSERT INTO highscores VALUES (?)", mass_list)
            data_base.commit()
            cur.close()
            data_base.close()
            mass_list.clear()
        if score == bll:
            mass_list = []
            mass_list.append(score)
            data_base = sqlite3.connect('pacman_highscores.db')
            cur = data_base.cursor()
            cur.execute("INSERT INTO highscores VALUES (?)", mass_list)
            data_base.commit()
            cur.close()
            data_base.close()
            mass_list.clear()

        screen.fill(black)

        wall_list.draw(screen)
        gate.draw(screen)
        all_sprites_list.draw(screen)
        monsta_list.draw(screen)

        text = font.render("Score: " + str(score) + "/" + str(bll), True, red)
        screen.blit(text, [10, 10])

        if score == bll:
            doNext("Congratulations, you won!", 245, all_sprites_list, block_list, monsta_list, pacman_collide,
                   wall_list, gate)

        if monsta_hit_list:
            doNext("Game Over", 335, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate)

        pygame.display.flip()

        clock.tick(10)
def doNext(message, left, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                if event.key == pygame.K_RETURN:
                    del all_sprites_list
                    del block_list
                    del monsta_list
                    del pacman_collide
                    del wall_list
                    del gate
                    startGame()

        w = pygame.Surface((400, 200))
        w.set_alpha(10)
        w.fill((128, 128, 128))
        screen.blit(w, (200, 300))

        text1 = font.render(message, True, white)
        screen.blit(text1, [left, 333])

        text2 = font.render("To play again, press ENTER.", True, white)
        screen.blit(text2, [235, 403])
        text3 = font.render("To quit, press ESCAPE.", True, white)
        screen.blit(text3, [265, 433])

        pygame.display.flip()

        clock.tick(10)

if __name__ == "__main__":
    main_menu()

pygame.quit()