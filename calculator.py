import pygame
import config

pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Calculator")

operation = ""
last_operation = ""
result = ""

def change_page(buttons):
    screen.fill(config.BLACK)
    if buttons == config.first_page:
        button.text = "1st"
        return config.second_page
    else:
        button.text = "2nd"
        return config.first_page

# GAME CLOCK
clock = pygame.time.Clock()
game = True

while game:
    pos = pygame.mouse.get_pos()

    screen.fill(config.BLACK)
    for button in config.buttons:
        button.draw(screen)
    
    if config.error:
        config.back.draw(screen)
        if config.back.mouse_on_button(pos):
            config.back.anim(screen)
    else:
        for button in config.buttons:
            if button.mouse_on_button(pos):
                button.anim(screen)

    clock.tick(config.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if config.error:
                if config.back.mouse_on_button(pos):
                    operation, last_operation, result = config.back.action(operation, last_operation, result)
            else:
                for button in config.buttons:
                    if button.mouse_on_button(pos):
                        operation, last_operation, result = button.action(operation, last_operation, result, **button.args)
                        if button == config.other:
                            config.buttons = change_page(config.buttons)
                        break

    try:
        last_operation_render = config.last_operation_font.render(last_operation, True, config.WHITE)
        last_operation_rect = last_operation_render.get_rect(topleft = (config.SIDE_MARGIN + config.MARGIN_OPERATION, config.MARGIN_OPERATION))
        if not config.error:
            pygame.draw.rect(screen, config.BLACK, last_operation_rect)
            screen.blit(last_operation_render, last_operation_rect)
    except NameError: pass

    operation_render = config.operation_font.render(operation, True, config.WHITE)
    operation_rect = operation_render.get_rect(bottomright = ((config.WIDTH - config.SIDE_MARGIN) - config.MARGIN_OPERATION, (config.HEIGHT - 5 * config.SIDE_LENGTH - 4 * config.MARGIN - config.SIDE_MARGIN) - config.MARGIN_OPERATION))
    pygame.draw.rect(screen, config.BLACK, operation_rect)
    screen.blit(operation_render, operation_rect)

    pygame.display.update()

pygame.quit()