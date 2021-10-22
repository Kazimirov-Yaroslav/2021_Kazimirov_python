import pygame
from ball import Ball
from superball import Superball
from operator import itemgetter
from pygame.image import load
from target import Target
from random import randint


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (175, 238, 238)
DODGER_BLUE = (30, 144, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def balls_create(s):
    """
    Create a group of sprites of class Ball, create balls and add balls to the group of all sprites.
    :param s: numbers balls
    :type s: int
    """
    for _ in range(s):
        random_color = randint(0, 5)
        Ball(COLORS[random_color], all_sprites, balls)


def superballs_create(s):
    """
    Create a group of sprites of class Superball, create superballs and add superballs to the group of all sprites.
    :param s: numbers superballs
    :type s: int
    """
    for _ in range(s):
        Superball(BLACK, all_sprites, balls)


def target_create(s):
    """
    Create a group of sprites of class Target, create targets and add targets to the group of all sprites.
    :param s: numbers targets
    :type s: int
    """
    for _ in range(s):
        Target('1602273595_7.png', all_sprites, amogus)


def tables(file1, file2, name_player, score):
    """
    Saving the result to file2, file1 is used as a draft.
    :param name_player: name player
    :param file1: draft
    :param file2: original
    """
    points = []
    table = open(file2, 'w')
    with open(file1, 'a') as output:
        print(name_player, '"', str(score), file=output)
    with open(file1, 'r') as f:
        for string in range(0, 1000, 1):
            line = f.readline()
            if line != '':
                pairs = line.split('" ')
                points.append(pairs)
                element = points[string][1]
                element.rstrip('\n')
                element = int(element)
                points[string][1] = element
    new_list = sorted(points, key=itemgetter(1))
    new_list.reverse()
    print('ТАБЛИЦА ЛИДЕРОВ', file=table)
    for i in range(0, len(new_list), 1):
        new_list[i][1] = str(new_list[i][1])
        print(''.join(new_list[i]), file=table)
    table.close()


def ask_name():
    """
    Entering a name
    """
    color_inactive = LIGHT_BLUE
    color_active = DODGER_BLUE
    color1 = color_inactive

    name = ''
    input_box = pygame.Rect(100, 100, 140, 32)
    text3 = font1.render('Введите своё имя:', True, WHITE)

    active = False
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color1 = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        finished = True
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode
        screen.fill(BLACK)
        txt_surface = font1.render(name, True, color1)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color1, input_box, 2)
        screen.blit(text3, (50, 70))

        pygame.display.flip()
        clock.tick(30)
    return name


def run():
    """
    The main cycle of the game
    """
    score = 0
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tables('Results', 'table', name, score)
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for sprite in balls:
                    a, b = pygame.mouse.get_pos()
                    x, y = sprite.rect.center
                    r = sprite.radius
                    if (a - x) ** 2 + (b - y) ** 2 <= r ** 2 and type(sprite) == Superball:
                        score += 8
                        print(score)
                        sprite.kill()
                        balls_create(1)
                    elif (a - x) ** 2 + (b - y) ** 2 <= r ** 2 and type(sprite) == Ball:
                        score += 2
                        print(score)
                        sprite.kill()
                        balls_create(1)
                for sprite in amogus:
                    a, b = pygame.mouse.get_pos()
                    x, y = sprite.rect.center
                    if sprite.rect.collidepoint((a, b)) and type(sprite) == Target:
                        score += 15
                        print(score)
                        sprite.kill()
                        target_create(1)

        all_sprites.update()

        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        text2 = font1.render('Очки: ' + str(score), True, BLACK)

        screen.blit(text2, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)


def end():
    """
    End of the game
    """
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        screen.fill((255, 255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(wizard, (500, 300))
        text2 = font2.render('ИДИ БОТАЙ', True, RED)
        screen.blit(text2, (100, 100))

        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    FPS = 60
    screen = pygame.display.set_mode((1200, 700))
    background = load('XXXL.jpg')
    wizard = load('C__fakepath_400px-Колдунов_Леонид_Модестович.png')
    wizard.set_colorkey((255, 255, 255))

    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 100)

    all_sprites = pygame.sprite.Group()
    balls = pygame.sprite.Group()
    amogus = pygame.sprite.Group()

    balls_create(6)
    superballs_create(3)
    target_create(3)
    clock = pygame.time.Clock()

    name = ask_name()
    run()
    end()

    pygame.quit()

