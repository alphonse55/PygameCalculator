import pygame
from Button import Button
import actions

pygame.init()

operation = ""
last_operation = ""
answer = ""

# caps because constants
OPERATORS = ["+", "-", "x", "/", "^"]
WIDTH, HEIGHT, FPS = 500, 700, 60  # display
BUTTON_WIDTH = 95  # side length of square buttons
MARGIN = (WIDTH - 5 * BUTTON_WIDTH) / 8 # margin between buttons, depends on the width so it can be changed easily

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

zero = Button(2 * MARGIN, HEIGHT - 2 * MARGIN - BUTTON_WIDTH, 2 * BUTTON_WIDTH + MARGIN, BUTTON_WIDTH, "0", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=0)
decimal_point = Button(4 * MARGIN + 2 * BUTTON_WIDTH, HEIGHT - 2 * MARGIN - BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, ".", GREY, LIGHT_GREY, WHITE, font_40, actions.decimal_point, OPERATORS=OPERATORS)

one = Button(2 * MARGIN, HEIGHT - 3 * MARGIN - 2 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "1", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=1)
two = Button(3 * MARGIN + BUTTON_WIDTH, HEIGHT - 3 * MARGIN - 2 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "2", GREY,LIGHT_GREY, WHITE, font_40, actions.number, n=2)
three = Button(4 * MARGIN + 2 * BUTTON_WIDTH, HEIGHT - 3 * MARGIN - 2 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "3", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=3)
four = Button(2 * MARGIN, HEIGHT - 4 * MARGIN - 3 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "4", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=4)
five = Button(3 * MARGIN + BUTTON_WIDTH, HEIGHT - 4 * MARGIN - 3 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "5", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=5)
six = Button(4 * MARGIN + 2 * BUTTON_WIDTH, HEIGHT - 4 * MARGIN - 3 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "6", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=6)
seven = Button(2 * MARGIN, HEIGHT - 5 * MARGIN - 4 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "7", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=7)
eight = Button(3 * MARGIN + BUTTON_WIDTH, HEIGHT - 5 * MARGIN - 4 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "8", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=8)
nine = Button(4 * MARGIN + 2 * BUTTON_WIDTH, HEIGHT - 5 * MARGIN - 4 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "9", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=9)

ans = Button(5 * MARGIN + 3 * BUTTON_WIDTH, HEIGHT - 2 * MARGIN - BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "Ans", DARK_BLUE, BLUE, WHITE, font_40, actions.ans, OPERATORS=OPERATORS)
power = Button(5 * MARGIN + 3 * BUTTON_WIDTH, HEIGHT - 3 * MARGIN - 2 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "^", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, segno="^")
plus = Button(5 * MARGIN + 3 * BUTTON_WIDTH,HEIGHT - 4 * MARGIN - 3 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "+", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, segno="+")
times = Button(5 * MARGIN + 3 * BUTTON_WIDTH, HEIGHT - 5 * MARGIN - 4 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "x", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, segno="x")
equals = Button(6 * MARGIN + 4 * BUTTON_WIDTH, HEIGHT - 3 * MARGIN - 2 * BUTTON_WIDTH, BUTTON_WIDTH, 2 * BUTTON_WIDTH + MARGIN, "=", DARK_BLUE, BLUE, WHITE, font_40, actions.equals, OPERATORS=OPERATORS)
minus = Button(6 * MARGIN + 4 * BUTTON_WIDTH, HEIGHT - 4 * MARGIN - 3 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "-", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, segno="-")
divided = Button(6 * MARGIN + 4 * BUTTON_WIDTH, HEIGHT - 5 * MARGIN - 4 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "/", DARK_BLUE, BLUE, WHITE, font_40, actions.sign, segno="/")


canc = Button(2 * MARGIN, HEIGHT - 6 * MARGIN - 5 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "Canc", DARK_RED, RED, WHITE, font_40, actions.canc)
DEL = Button(3 * MARGIN + BUTTON_WIDTH, HEIGHT - 6 * MARGIN - 5 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "DEL", DARK_GREY, GREY, WHITE, font_40, actions.delete)
left_bracket = Button(4 * MARGIN + 2 * BUTTON_WIDTH, HEIGHT - 6 * MARGIN - 5 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "(", DARK_GREY, GREY, WHITE, font_40, actions.left)
right_bracket = Button(5 * MARGIN + 3 * BUTTON_WIDTH, HEIGHT - 6 * MARGIN - 5 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, ")", DARK_GREY, GREY, WHITE, font_40, actions.right)
other = Button(6 * MARGIN + 4 * BUTTON_WIDTH, HEIGHT - 6 * MARGIN - 5 * BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH, "2nd", DARK_GREY, GREY, WHITE, font_40, actions.other)

# ^2,    ^3,    e^    # e,    pi
# root,  3root, yroot # !,    *10^
# sin,   cos,   tan   # ln,   logy
# sin-1, cos-1, tan-1 # log2, log10

buttons_1 = [zero, decimal_point, one, two, three, four, five, six, seven, eight, nine, ans, power, plus, times, equals, minus, divided, canc, DEL, left_bracket, right_bracket, other]
buttons_2 = [canc, DEL, left_bracket, right_bracket, other]
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
        last_operation_rect = last_operation_render.get_rect(bottomright=(WIDTH - 3 * MARGIN, HEIGHT - 6 * BUTTON_WIDTH - 9 * MARGIN))
        screen.blit(last_operation_render, last_operation_rect)
    except NameError:
        pass

    operation_render = font_60.render(operation, True, WHITE)
    operation_rect = operation_render.get_rect(bottomright=(WIDTH - 3 * MARGIN, HEIGHT - 9 * MARGIN - 5 * BUTTON_WIDTH))
    screen.blit(operation_render, operation_rect)

    pygame.display.update()

pygame.quit()