import pygame
import config
from write import write

pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Calculator")

# GAME CLOCK
clock = pygame.time.Clock()
game = True

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
    write(screen, operation, 0)
    if config.solved:
        write(screen, result, 1)

    pygame.display.update()

pygame.quit()
