from typing import NewType
import pygame
import config

pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Calculator")

# GAME CLOCK
clock = pygame.time.Clock()
game = True

def transform(text):
    text = list(text)

    roots = []
    for i, c in enumerate(text):
        if c == "√":
            if i == 0:
                break
            for j, d in enumerate(reversed(text[:i])):
                if d not in config.NUMBERS + ".":
                    roots += [[i, i-j]]
                    break
                elif j == i - 1:
                    roots += [[i, i-j-1]]
    for i, root in enumerate(roots):
        text.insert(root[0] + i*2, "*")
        text.insert(root[1] + i*2, "*")

    exponents = []
    for i, c in enumerate(text):
        if c == "^":
            if i == len(text) - 1:
                break
            elif text[i+1] == "(":
                counter = 0
                for j, char in enumerate(text[i+1:]):
                    counter += 1 if char == "(" else (-1 if char == ")" else 0)
                    if counter == 0 or i + 1 + j == len(text) - 1:
                        exponents += [[i+1, i+1+j+2]]
                        break
            elif text[i+1] in config.NUMBERS:
                for j, char in enumerate(text[i+1:]):
                    if char not in config.NUMBERS + ".":
                        exponents += [[i+1, i+1+j+1]]
                        break
                    elif i + 1 + j == len(text) - 1:
                        exponents += [[i+1, i+1+j+2]]
                        break

    for i, exponent in enumerate(exponents):
        text.remove("^")
        text.insert(exponent[0] + i - 1, "*") #
        text.insert(exponent[1] + i - 1, "*")

    text = "".join(text)
    return text
            

def write(text, pos):
    text = transform(text)
    # decompose text
    texts = []
    while "_" in text or "*" in text:
        for i, c in enumerate(text):
            if c in "_*":
                texts += [text[:i]]
                for j, d in enumerate(text[i+1:]):
                    if d == c:
                        texts += [text[i:i+j+1]]
                        break
                text = text[i+j+2:]
                break
    texts += text
    while "" in texts:
        texts.remove("")
    
    rects, renders = [], []
    # find font
    max_font = config.MAX_OPERATION_FONT_SIZE if pos == 0 else config.MAX_RESULT_FONT_SIZE
    for font in config.font[max_font::-1]:
        rects, renders = [], []
        # renders
        for t in texts:
            if t[0] in "_*":
                renders += [config.font[config.font.index(font)//2].render(t[1:], True, config.WHITE)]
            else:
                renders += [font.render(t, True, config.WHITE)]
        # rects
        if pos == 0: # operation
            for i, render in enumerate(renders):
                x = config.SIDE_MARGIN + config.WIDTH_ARROWS + config.MARGIN_OPERATION
                y = config.SIDE_MARGIN + config.MARGIN_OPERATION
                rects += [render.get_rect(topleft = (x + sum([rect.width for rect in rects]), y + (3*config.font.index(font)//8 if texts[i][0] == "_" else (-config.font.index(font)//8 if texts[i][0] == "*" else 0))))]
        elif pos == 1: # result
            for i, render in reversed(list(enumerate(renders))):
                x = config.WIDTH - config.SIDE_MARGIN - config.WIDTH_ARROWS - config.MARGIN_OPERATION
                y = config.HEIGHT - 5 * config.SIDE_LENGTH - 4 * config.MARGIN - 2 * config.SIDE_MARGIN - config.MARGIN_OPERATION
                rects.insert(0, render.get_rect(bottomright = (x - sum([rect.width for rect in rects]), y - (3*config.font.index(font)//8 if texts[i][0] == "*" else 0))))
        if sum([rect.width for rect in rects]) < config.MAX_TEXT_WIDTH:
            break
    # write
    for render, rect in zip(renders, rects):
        pygame.draw.rect(screen, config.BLACK, rect)
        screen.blit(render, rect)

while game:
    if config.solved:
        buttons = list(set(config.buttons) | {config.back, config.next})
        if config.operation_index <= 0:
            buttons = list(set(buttons) - {config.back})
        if config.operation_index >= len(config.operations) - 1:
            buttons = list(set(buttons) - {config.next})
    else:
        buttons = list(set(config.buttons) - {config.back, config.next})

    pos = pygame.mouse.get_pos()
    screen.fill(config.BLACK)

    for button in buttons:
        button.draw(screen)

    for button in buttons:
        if button.mouse_on_button(pos):
            button.anim(screen)

    clock.tick(config.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.mouse_on_button(pos):
                    button.action(**button.args)
                    break
    
    operation, result = config.operations[config.operation_index]
    write(operation, 0)
    if config.solved:
        write(result, 1)

    pygame.display.update()

pygame.quit()
