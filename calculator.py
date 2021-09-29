import pygame
import config

pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Calculator")

# GAME CLOCK
clock = pygame.time.Clock()
game = True

while game:
    config.buttons = list(set(config.buttons) | {config.back, config.next})
    if config.operation_index <= 0:
        config.buttons = list(set(config.buttons) - {config.back})
    if config.operation_index >= len(config.operations) - 1:
        config.buttons = list(set(config.buttons) - {config.next})

    pos = pygame.mouse.get_pos()
    screen.fill(config.BLACK)
    for button in config.buttons:
        button.draw(screen)

    for button in config.buttons:
        if button.mouse_on_button(pos):
            # if not (config.solved and button in config.illegal_buttons):
            button.anim(screen)

    clock.tick(config.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in config.buttons:
                if button.mouse_on_button(pos):
                    if config.solved:
                        if button in config.resetting_buttons:
                            config.operations += [list(button.action("", result, **button.args))]
                            config.operation_index = len(config.operations) - 1
                            config.solved = False
                        elif button in config.neutral_buttons:
                            config.operations[config.operation_index] = list(button.action(operation, result, **button.args))
                    else:
                        config.operations[config.operation_index] = list(button.action(operation, result, **button.args))
                    break
                    
    operation, result = config.operations[config.operation_index]
    for font in config.font[config.MAX_OPERATION_FONT_SIZE::-1]:
        operation_render = font.render(operation, True, config.WHITE)
        operation_rect = operation_render.get_rect(topleft = (config.SIDE_MARGIN + config.WIDTH_ARROWS + config.MARGIN_OPERATION, config.SIDE_MARGIN + config.MARGIN_OPERATION))
        if operation_rect.width < config.MAX_TEXT_WIDTH:
            break
    pygame.draw.rect(screen, config.BLACK, operation_rect)
    screen.blit(operation_render, operation_rect)

    if config.solved or config.operation_index != len(config.operations) - 1:
        for font in config.font[config.MAX_RESULT_FONT_SIZE::-1]:
            result_render = font.render(result, True, config.WHITE)
            result_rect = result_render.get_rect(bottomright = (config.WIDTH - config.SIDE_MARGIN - config.WIDTH_ARROWS - config.MARGIN_OPERATION, config.HEIGHT - 5 * config.SIDE_LENGTH - 4 * config.MARGIN - 2 * config.SIDE_MARGIN - config.MARGIN_OPERATION))
            if result_rect.width < config.MAX_TEXT_WIDTH:
                break
        pygame.draw.rect(screen, config.BLACK, result_rect)
        screen.blit(result_render, result_rect)

    pygame.display.update()
pygame.quit()
