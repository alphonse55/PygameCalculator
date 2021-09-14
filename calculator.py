import pygame
from Button import Button
import actions

pygame.init()

operation = ""
last_operation = ""
answer = ""

# caps because constants
WIDTH, HEIGHT, FPS = 500, 700, 60  # display
COLUMNS, ROWS = 5, 5
MARGIN = 10
SIDE_MARGIN = 2 * MARGIN
width_without_margins = WIDTH - MARGIN * (COLUMNS - 1) - 2 * SIDE_MARGIN
SIDE_LENGTH = int(width_without_margins/COLUMNS) # convert it to int because if it is decimal it will add one pixel to one margin at some point
SIDE_MARGIN = (WIDTH - (SIDE_LENGTH * COLUMNS + MARGIN * (COLUMNS - 1))) / 2 # recalculate it to center the buttons perectly because of the int() conversion of SIDE_LENGTH

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

def change_page(buttons):
    screen.fill(BLACK)
    if buttons == first_page:
        button.text = "BACK"
        return second_page
    else:
        button.text = "2nd"
        return first_page

def merge(x1, y1, w1, h1, x2, y2, w2, h2):
    tot_width = (x2 + w2) - x1
    tot_height = (y2 + h2) - y1
    return (x1, y1, tot_width, tot_height)

std_button = (GREY, LIGHT_GREY, WHITE, font_40)
grid = [[(SIDE_MARGIN + x * (MARGIN + SIDE_LENGTH), HEIGHT - SIDE_MARGIN - SIDE_LENGTH - (ROWS - 1 - y) * (MARGIN + SIDE_LENGTH), SIDE_LENGTH, SIDE_LENGTH) for x in range(COLUMNS)] for y in range(ROWS)]

canc = Button("Canc", DARK_RED, RED, WHITE, font_40, actions.canc)
DEL = Button("DEL", DARK_GREY, GREY, WHITE, font_40, actions.delete)
left_bracket = Button("(", DARK_GREY, GREY, WHITE, font_40, actions.left)
right_bracket = Button(")", DARK_GREY, GREY, WHITE, font_40, actions.right)
other = Button("2nd", DARK_GREY, GREY, WHITE, font_40, actions.other)

decimal_point = Button(".", *std_button, actions.decimal_point)
zero = Button("0", *std_button, actions.number, n=0)
one = Button("1", *std_button, actions.number, n=1)
two = Button("2", *std_button, actions.number, n=2)
three = Button("3", *std_button, actions.number, n=3)
four = Button("4", *std_button, actions.number, n=4)
five = Button("5", *std_button, actions.number, n=5)
six = Button("6", *std_button, actions.number, n=6)
seven = Button("7", *std_button, actions.number, n=7)
eight = Button("8", *std_button, actions.number, n=8)
nine = Button("9", *std_button, actions.number, n=9)

ans = Button("Ans", DARK_BLUE, BLUE, WHITE, font_40, actions.ans)
power = Button("^", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, sign="^")
plus = Button("+", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, sign="+")
times = Button("x", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, sign="x")
equals = Button("=", DARK_BLUE, BLUE, WHITE, font_40, actions.equals)
minus = Button("-", DARK_BLUE, BLUE, WHITE, font_40, actions.minus)
divided = Button("/", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, sign="/")

pi = Button("π", *std_button, actions.constant, n="3.1416")
e = Button("e", *std_button, actions.constant, n="2.1828")
e_power = Button("e^", *std_button, actions.constant, n="2.1828^")
square = Button("x^2", *std_button, actions.sign, sign="^2")
cube = Button("x^3", *std_button, actions.sign, sign="^3")

# pi    e     e^    ^2    ^3
# root  3root yroot !     *10^
# sin   cos   tan   ln    logy
# sin-1 cos-1 tan-1 log2  log10

buttons = []
first_page = [
    [canc, DEL, left_bracket, right_bracket, other],
    [seven, eight, nine, plus, minus],
    [four, five, six, times, divided],
    [one, two, three, power, equals],
    [zero, zero, decimal_point, ans, equals]
]

second_page = [
    [canc, DEL, left_bracket, right_bracket, other],
    [pi, e, e_power, square, cube],
]

for y, row in enumerate(second_page):
    for x, button in enumerate(row):
        if button not in buttons:
            button.x_i, button.y_i, button.width, button.height = grid[y][x]
            buttons.append(button)
        else:
            for r in first_page:
                for b in r:
                    if b == button:
                        break
            button.x_i, button.y_i, button.width, button.height = merge(b.x_i, b.y_i, b.width, b.height, *grid[y][x])
second_page = buttons

buttons = []
for y, row in enumerate(first_page):
    for x, button in enumerate(row):
        if button not in buttons:
            button.x_i, button.y_i, button.width, button.height = grid[y][x]
            buttons.append(button)
        else:
            for r in first_page:
                for b in r:
                    if b == button:
                        break
            button.x_i, button.y_i, button.width, button.height = merge(b.x_i, b.y_i, b.width, b.height, *grid[y][x])
first_page = buttons

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
                    operation, last_operation, answer = button.action(operation, last_operation, answer, **button.args)
                    if button == other:
                        buttons = change_page(buttons)
                    break
    try: pygame.draw.rect(screen, BLACK, operation_rect)
    except NameError: pass

    try:
        try: pygame.draw.rect(screen, BLACK, last_operation_rect)
        except NameError: pass
        last_operation_render = font_40.render(last_operation, True, WHITE)
        last_operation_rect = last_operation_render.get_rect(bottomright = (WIDTH - 3 * MARGIN, HEIGHT - 6 * SIDE_LENGTH - 9 * MARGIN))
        screen.blit(last_operation_render, last_operation_rect)
    except NameError: pass

    operation_render = font_60.render(operation, True, WHITE)
    operation_rect = operation_render.get_rect(bottomright = (WIDTH - 3 * MARGIN, HEIGHT - 9 * MARGIN - 5 * SIDE_LENGTH))
    screen.blit(operation_render, operation_rect)

    pygame.display.update()

pygame.quit()