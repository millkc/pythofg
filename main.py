import random

import pygame

size = wight, height = 800, 600
rungame = True
screen = pygame.display.set_mode(size)


# pygame.event.wait().type != pygame.QUIT
def game():
    global rungame
    pygame.init()
    pygame.display.flip()
    screen.fill((0, 0, 0))
    while rungame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rungame = False

        cross(screen)
        draw(screen)
        pygame.display.flip()


def cross(screen):
    x1, y1 = random.randrange(wight), random.randrange(height)
    x2, y2 = random.randrange(wight), random.randrange(height)
    pygame.draw.line(screen, (255, 255, 255,), (x1, y1), (x2, y2), 10)


def draw(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 70)
    text = font.render('Hello word!', 0, (100, 255, 100))
    text_x = wight // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_h = text.get_height()
    text_w = text.get_width()
    screen.blit(text, (text_x, text_y))


if __name__ == '__main__':
    game()
