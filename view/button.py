import pygame


class Button:

    def __init__(self, pos_x, pos_y, width, height,
                 button_color=(255, 255, 255),
                 hover_button_color=(200, 200, 200),
                 text="", text_color=(0, 0, 0), font=None, font_size=35):
        self.image = pygame.Surface((width, height))
        self.image.fill(button_color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

        self.button_color = self.original_button_color = button_color
        self.hover_button_color = hover_button_color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont(font, font_size)
        self.font_size = font_size

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline,
                             (self.x - 2, self.y - 2,
                              self.width + 4, self.height + 4),
                             0)
        pygame.draw.rect(win, self.button_color, self.rect, 0)
        if self.text != "":
            text_surface = self.font.render(self.text, True, self.text_color)
            win.blit(text_surface,
                     (self.x + (self.width / 2 - text_surface.get_width() / 2),
                      self.y + (self.height / 2
                                - text_surface.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False
