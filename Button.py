import pygame

class Button:
    def __init__(self, x_i, y_i, width, height, text, color_1, color_2, text_color, font, action, **kwargs):
        self.x_i = x_i
        self.y_i = y_i
        self.width = width
        self.height = height
        self.text = text
        self.color_1 = color_1
        self.color_2 = color_2
        self.action = action
        self.args = kwargs
        self.font = font
        self.text_color = text_color

    def draw(self, screen):
        self.text_render = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_render.get_rect(center=(self.x_i + self.width / 2, self.y_i + self.height / 2))
        pygame.draw.rect(screen, self.color_1, [self.x_i, self.y_i, self.width, self.height])
        screen.blit(self.text_render, self.text_rect)

    def anim(self, screen):
        pygame.draw.rect(screen, self.color_2, [self.x_i, self.y_i, self.width, self.height])
        screen.blit(self.text_render, self.text_rect)

    def func(self, op, op_scorsa, ans):
        return self.action(op, op_scorsa, ans, **self.args)

    def mouse_on_button(self, mouse):
        return self.x_i <= mouse[0] <= self.x_i + self.width and self.y_i <= mouse[1] <= self.y_i + self.height