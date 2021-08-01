import pygame

class Button:
    def __init__(self, x_i, y_i, lato_x, lato_y, text, colore1, colore2, colore_testo, font, action, **kwargs):
        self.x_i = x_i
        self.y_i = y_i
        self.lato_x = lato_x
        self.lato_y = lato_y
        self.text = text
        self.colore1 = colore1
        self.colore2 = colore2
        self.action = action
        self.args = kwargs
        self.font = font
        self.colore_testo = colore_testo

    def draw(self, screen):
        self.text_render = self.font.render(self.text, True, self.colore_testo)
        self.text_rect = self.text_render.get_rect(center=(self.x_i + self.lato_x / 2, self.y_i + self.lato_y / 2))
        pygame.draw.rect(screen, self.colore1, [self.x_i, self.y_i, self.lato_x, self.lato_y])
        screen.blit(self.text_render, self.text_rect)

    def anim(self, screen):
        # self.text_render = self.font.render(self.text, True, colore_testo)
        # self.text_rect = self.text_render.get_rect(center=(self.x_i + self.lato_x / 2, self.y_i + self.lato_y / 2))
        pygame.draw.rect(screen, self.colore2, [self.x_i, self.y_i, self.lato_x, self.lato_y])
        screen.blit(self.text_render, self.text_rect)

    def func(self, op, op_scorsa, ans):
        return self.action(op, op_scorsa, ans, **self.args)

    def mouse_on_button(self, mouse):
        return self.x_i <= mouse[0] <= self.x_i + self.lato_x and self.y_i <= mouse[1] <= self.y_i + self.lato_y