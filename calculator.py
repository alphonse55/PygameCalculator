import pygame
from Button import Button
import actions

pygame.init()

operation = ""
last_operation = ""
answer = ""

# caps because constants
WIDTH, HEIGHT, FPS = 500, 700, 60  # display
SIDE_LENGTH = 95
MARGIN = (WIDTH - 5 * SIDE_LENGTH) / 8 # margin between buttons, depends on the width so it can be changed easily

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (100, 100, 100)
GREY = (80, 80, 80)
DARK_GREY = (30, 30, 30)
RED = (255, 0, 0)
DARK_RED = (200, 0, 0)
DARK_BLUE = (16, 54, 97)
BLUE = (25, 85, 152)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculator")

# GAME CLOCK
clock = pygame.time.Clock()
game = True

font_40 = pygame.font.Font(None, 40)
font_50 = pygame.font.Font(None, 50)
font_60 = pygame.font.Font(None, 60)
screen.fill(BLACK)

std_button = (GREY, LIGHT_GREY, WHITE, font_40)
grid = [[(2 * MARGIN + x * (MARGIN + SIDE_LENGTH), HEIGHT - 2 * MARGIN - SIDE_LENGTH - (4 - y) * (MARGIN + SIDE_LENGTH), SIDE_LENGTH, SIDE_LENGTH) for x in range(5)] for y in range(5)]

def merge(x1, y1, w1, h1, x2, y2, w2, h2):
    tot_width = (x2 + w2) - x1
    tot_height = (y2 + h2) - y1
    return (x1, y1, tot_width, tot_height)

zero = Button(*merge(*grid[4][0], *grid[4][1]), "0", *std_button, actions.number, n=0)
decimal_point = Button(*grid[4][2], ".", *std_button, actions.decimal_point)

one = Button(*grid[3][0], "1", *std_button, actions.number, n=1)
two = Button(*grid[3][1], "2", *std_button, actions.number, n=2)
three = Button(*grid[3][2], "3", *std_button, actions.number, n=3)
four = Button(*grid[2][0], "4", *std_button, actions.number, n=4)
five = Button(*grid[2][1], "5", *std_button, actions.number, n=5)
six = Button(*grid[2][2], "6", *std_button, actions.number, n=6)
seven = Button(*grid[1][0], "7", *std_button, actions.number, n=7)
eight = Button(*grid[1][1], "8", *std_button, actions.number, n=8)
nine = Button(*grid[1][2], "9", *std_button, actions.number, n=9)

ans = Button(*grid[4][3], "Ans", DARK_BLUE, BLUE, WHITE, font_40, actions.ans)
power = Button(*grid[3][3], "^", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, sign="^")
plus = Button(*grid[2][3], "+", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, sign="+")
times = Button(*grid[1][3], "x", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, sign="x")
equals = Button(*merge(*grid[3][4], *grid[4][4]), "=", DARK_BLUE, BLUE, WHITE, font_40, actions.equals)
minus = Button(*grid[2][4], "-", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, sign="-")
divided = Button(*grid[1][4], "/", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, sign="/")


canc = Button(*grid[0][0], "Canc", DARK_RED, RED, WHITE, font_40, actions.canc)
DEL = Button(*grid[0][1], "DEL", DARK_GREY, GREY, WHITE, font_40, actions.delete)
left_bracket = Button(*grid[0][2], "(", DARK_GREY, GREY, WHITE, font_40, actions.left)
right_bracket = Button(*grid[0][3], ")", DARK_GREY, GREY, WHITE, font_40, actions.right)
other = Button(*grid[0][4], "2nd", DARK_GREY, GREY, WHITE, font_40, actions.other)

pi = Button(*grid[1][0], "π", *std_button, actions.constant, n="3.1416")
e = Button(*grid[1][1], "e", *std_button, actions.constant, n="2.1828")
e_power = Button(*grid[1][2], "e^", *std_button, actions.constant, n="2.1828^")
square = Button(*grid[1][3], "x^2", *std_button, actions.sign, sign="^2")
cube = Button(*grid[1][4], "x^3", *std_button, actions.sign, sign="^3")
# ^2,    ^3,    e^    # e,    pi
# root,  3root, yroot # !,    *10^
# sin,   cos,   tan   # ln,   logy
# sin-1, cos-1, tan-1 # log2, log10

buttons_1 = [zero, decimal_point, one, two, three, four, five, six, seven, eight, nine, ans, power, plus, times, equals, minus, divided, canc, DEL, left_bracket, right_bracket, other]
buttons_2 = [canc, DEL, left_bracket, right_bracket, other, pi, e, e_power, square, cube]
buttons = buttons_1

while game:
    pos = pygame.mouse.get_pos()

    for button in buttons:
        button.draw(screen)

        if button.mouse_on_button(pos):
            button.anim(screen)

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.mouse_on_button(pos):
                    if button == other:
                        screen.fill(BLACK)
                        if buttons == buttons_1:
                            buttons = buttons_2
                            button.text = "BACK"
                        else:
                            buttons = buttons_1
                            button.text = "2nd"
                    else:
                        operation, last_operation, answer = button.action(operation, last_operation, answer, **button.args)
                    break

    try:
        pygame.draw.rect(screen, BLACK, operation_rect)
    except NameError:
        pass

    try:
        try:
            pygame.draw.rect(screen, BLACK, last_operation_rect)
        except NameError:
            pass
        last_operation_render = font_40.render(last_operation, True, WHITE)
        last_operation_rect = last_operation_render.get_rect(bottomright=(WIDTH - 3 * MARGIN, HEIGHT - 6 * SIDE_LENGTH - 9 * MARGIN))
        screen.blit(last_operation_render, last_operation_rect)
    except NameError:
        pass

    operation_render = font_60.render(operation, True, WHITE)
    operation_rect = operation_render.get_rect(bottomright=(WIDTH - 3 * MARGIN, HEIGHT - 9 * MARGIN - 5 * SIDE_LENGTH))
    screen.blit(operation_render, operation_rect)

    pygame.display.update()

pygame.quit()