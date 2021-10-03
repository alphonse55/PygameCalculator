import pygame
import config

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

    # draw operation
    for font in config.font[config.MAX_OPERATION_FONT_SIZE::-1]:
        operation_render = font.render(operation, True, config.WHITE)
        operation_rect = operation_render.get_rect(topleft = (config.SIDE_MARGIN + config.WIDTH_ARROWS + config.MARGIN_OPERATION, config.SIDE_MARGIN + config.MARGIN_OPERATION))
        if operation_rect.width < config.MAX_TEXT_WIDTH:
            break
    pygame.draw.rect(screen, config.BLACK, operation_rect)
    screen.blit(operation_render, operation_rect)

    # draw result
    if config.solved:
        for font in config.font[config.MAX_RESULT_FONT_SIZE::-1]:
            result_render = font.render(result, True, config.WHITE)
            result_rect = result_render.get_rect(bottomright = (config.WIDTH - config.SIDE_MARGIN - config.WIDTH_ARROWS - config.MARGIN_OPERATION, config.HEIGHT - 5 * config.SIDE_LENGTH - 4 * config.MARGIN - 2 * config.SIDE_MARGIN - config.MARGIN_OPERATION))
            if result_rect.width < config.MAX_TEXT_WIDTH:
                break
        pygame.draw.rect(screen, config.BLACK, result_rect)
        screen.blit(result_render, result_rect)

    pygame.display.update()
pygame.quit()
