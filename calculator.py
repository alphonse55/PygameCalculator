import pygame
from Button import Button
import actions

pygame.init()

operazione = ""
operazione_scorsa = ""
answer = ""

OPERATORS = ["+", "-", "x", "/", "^"]

# maiuscolo perché costante
LARGHEZZA, ALTEZZA, FPS = 500, 700, 60  # display
LATO_NUMERI = 95  # dimensione lato buttons quadrati

MARGINE = (LARGHEZZA - 5 * LATO_NUMERI) / 8

# COLORI
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (100, 100, 100)
GREY = (80, 80, 80)
DARK_GREY = (30, 30, 30)
ROSSO = (255, 0, 0)
ROSSO_SCURO = (200, 0, 0)
BLU_SCURO = (16, 54, 97)
BLU = (25, 85, 152)

screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Calculator")

# GAME CLOCK
orologio = pygame.time.Clock()
gioco = True

font_40 = pygame.font.Font(None, 40)
font_50 = pygame.font.Font(None, 50)
font_60 = pygame.font.Font(None, 60)
screen.fill(BLACK)

zero = Button(2 * MARGINE, ALTEZZA - 2 * MARGINE - LATO_NUMERI, 2 * LATO_NUMERI + MARGINE, LATO_NUMERI, "0", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=0)
virgola = Button(4 * MARGINE + 2 * LATO_NUMERI, ALTEZZA - 2 * MARGINE - LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, ",", GREY, LIGHT_GREY, WHITE, font_40, actions.virgola, OPERATORS=OPERATORS)

uno = Button(2 * MARGINE, ALTEZZA - 3 * MARGINE - 2 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "1", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=1)
due = Button(3 * MARGINE + LATO_NUMERI, ALTEZZA - 3 * MARGINE - 2 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "2", GREY,LIGHT_GREY, WHITE, font_40, actions.number, n=2)
tre = Button(4 * MARGINE + 2 * LATO_NUMERI, ALTEZZA - 3 * MARGINE - 2 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "3", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=3)
quattro = Button(2 * MARGINE, ALTEZZA - 4 * MARGINE - 3 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "4", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=4)
cinque = Button(3 * MARGINE + LATO_NUMERI, ALTEZZA - 4 * MARGINE - 3 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "5", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=5)
sei = Button(4 * MARGINE + 2 * LATO_NUMERI, ALTEZZA - 4 * MARGINE - 3 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "6", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=6)
sette = Button(2 * MARGINE, ALTEZZA - 5 * MARGINE - 4 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "7", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=7)
otto = Button(3 * MARGINE + LATO_NUMERI, ALTEZZA - 5 * MARGINE - 4 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "8", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=8)
nove = Button(4 * MARGINE + 2 * LATO_NUMERI, ALTEZZA - 5 * MARGINE - 4 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "9", GREY, LIGHT_GREY, WHITE, font_40, actions.number, n=9)

ans = Button(5 * MARGINE + 3 * LATO_NUMERI, ALTEZZA - 2 * MARGINE - LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "Ans", BLU_SCURO, BLU, WHITE, font_40, actions.ans, OPERATORS=OPERATORS)
potenza = Button(5 * MARGINE + 3 * LATO_NUMERI, ALTEZZA - 3 * MARGINE - 2 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "^", BLU_SCURO, BLU, WHITE, font_40, actions.segno, segno="^")
più = Button(5 * MARGINE + 3 * LATO_NUMERI,ALTEZZA - 4 * MARGINE - 3 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "+", BLU_SCURO, BLU, WHITE, font_40, actions.segno, segno="+")
per = Button(5 * MARGINE + 3 * LATO_NUMERI, ALTEZZA - 5 * MARGINE - 4 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "x", BLU_SCURO, BLU, WHITE, font_40, actions.segno, segno="x")
uguale = Button(6 * MARGINE + 4 * LATO_NUMERI, ALTEZZA - 3 * MARGINE - 2 * LATO_NUMERI, LATO_NUMERI, 2 * LATO_NUMERI + MARGINE, "=", BLU_SCURO, BLU, WHITE, font_40, actions.uguale, OPERATORS=OPERATORS)
meno = Button(6 * MARGINE + 4 * LATO_NUMERI, ALTEZZA - 4 * MARGINE - 3 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "-", BLU_SCURO, BLU, WHITE, font_40, actions.segno, segno="-")
diviso = Button(6 * MARGINE + 4 * LATO_NUMERI, ALTEZZA - 5 * MARGINE - 4 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "/", BLU_SCURO, BLU, WHITE, font_40, actions.segno, segno="/")

canc = Button(2 * MARGINE, ALTEZZA - 6 * MARGINE - 5 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "Canc", ROSSO_SCURO, ROSSO, WHITE, font_40, actions.canc)
DEL = Button(3 * MARGINE + LATO_NUMERI, ALTEZZA - 6 * MARGINE - 5 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "DEL", DARK_GREY, GREY, WHITE, font_40, actions.delete)
sinistra = Button(4 * MARGINE + 2 * LATO_NUMERI, ALTEZZA - 6 * MARGINE - 5 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "(", DARK_GREY, GREY, WHITE, font_40, actions.sinistra)
destra = Button(5 * MARGINE + 3 * LATO_NUMERI, ALTEZZA - 6 * MARGINE - 5 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, ")", DARK_GREY, GREY, WHITE, font_40, actions.destra)
altro = Button(6 * MARGINE + 4 * LATO_NUMERI, ALTEZZA - 6 * MARGINE - 5 * LATO_NUMERI, LATO_NUMERI, LATO_NUMERI, "2nd", DARK_GREY, GREY, WHITE, font_40, actions.altro)

bottoni_1st = [zero, virgola, uno, due, tre, quattro, cinque, sei, sette, otto, nove, ans, potenza, più, per, uguale, meno, diviso, canc, DEL, sinistra, destra, altro]
bottoni_2nd = [canc, DEL, sinistra, destra, altro]
buttons = bottoni_1st

while gioco:
    pos = pygame.mouse.get_pos()

    for button in buttons:
        button.draw(screen)

        if button.mouse_on_button(pos):
            button.anim(screen)

    orologio.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gioco = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.mouse_on_button(pos):
                    if button == altro:
                        screen.fill(BLACK)
                        if buttons == bottoni_1st:
                            buttons = bottoni_2nd
                            button.text = "1st"
                        else:
                            buttons = bottoni_1st
                            button.text = "2nd"
                    else:
                        operazione, operazione_scorsa, answer = button.func(operazione, operazione_scorsa, answer)
                        if operazione == answer:
                            operazione_scorsa += answer
                            operazione = ""
                    break

    try:
        pygame.draw.rect(screen, BLACK, operazione_rect)
    except NameError:
        pass

    try:
        try:
            pygame.draw.rect(screen, BLACK, operazione_scorsa_rect)
        except NameError:
            pass
        operazione_scorsa_render = font_40.render(operazione_scorsa, True, WHITE)
        operazione_scorsa_rect = operazione_scorsa_render.get_rect(
            bottomright=(
                LARGHEZZA - 3 * MARGINE,
                ALTEZZA - 6 * LATO_NUMERI - 9 * MARGINE,
            )
        )
        screen.blit(operazione_scorsa_render, operazione_scorsa_rect)
    except NameError:
        pass

    operazione_render = font_60.render(operazione, True, WHITE)
    operazione_rect = operazione_render.get_rect(
        bottomright=(LARGHEZZA - 3 * MARGINE, ALTEZZA - 9 * MARGINE - 5 * LATO_NUMERI)
    )
    screen.blit(operazione_render, operazione_rect)

    pygame.display.update()

pygame.quit()