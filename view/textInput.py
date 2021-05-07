import pygame


class TextInput:
    def __init__(self, pos_x, pos_y, width, height,
                 field_color=(255, 255, 255), active_color=(245, 245, 245),
                 is_active=False, text="", text_color=(0, 0, 0),
                 text_hint="", font=None, font_size=35, max_string_length=-1,
                 restriction=None, description=None):
        self.image = pygame.Surface((width, height))
        self.image.fill(field_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

        self.field_color = self.original_field_color = field_color
        self.active_color = active_color
        self.is_active = is_active
        self.text = text
        self.text_color = text_color
        self.text_hint = text_hint
        self.font = pygame.font.SysFont(font, font_size)
        self.max_string_length = max_string_length
        self.restriction = restriction
        self.description = description

        self.desc_surface = self.font.render(self.description,
                                             True, self.text_color)
        self.text_surface = self.font.render(text, True, self.text_color)

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

    def draw(self, win):
        # draw description
        win.blit(self.desc_surface,
                 (self.rect.x - self.desc_surface.get_width(),
                  self.rect.y + 6))

        # draw input field border
        pygame.draw.rect(win, (0, 0, 0), (self.rect.x - 2, self.rect.y - 2,
                                          self.rect.width + 4,
                                          self.rect.height + 4), 2)
        # draw input field background
        if self.is_active:
            pygame.draw.rect(win, self.active_color, self.rect)
        else:
            pygame.draw.rect(win, self.field_color, self.rect)

        # draw text
        win.blit(self.text_surface, (self.rect.x + 6, self.rect.y + 7))

    def events_handling(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_active = True
            else:
                self.is_active = False
        if event.type == pygame.KEYDOWN and self.is_active:
            if event.key == pygame.K_RETURN:
                print(self.text)
                self.text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if not self.restriction or event.unicode in self.restriction:
                    self.text += event.unicode
                if self.max_string_length != -1:
                    self.text = self.text[:self.max_string_length]

        if self.is_active:
            self.text_surface = self.font.render(self.text + "|", True,
                                                 self.text_color)
            temp = -1 * len(self.text)
            i = 1
            while self.text_surface.get_width() >= self.rect.width:
                self.text_surface = self.font.render(self.text[temp + i:]
                                                     + "|",
                                                     True, self.text_color)
                i += 1
        else:
            self.text_surface = self.font.render(self.text, True,
                                                 self.text_color)
            temp = -1 * len(self.text)
            i = 1
            while self.text_surface.get_width() >= self.rect.width:
                self.text_surface = self.font.render(self.text[temp + i:],
                                                     True, self.text_color)
                i += 1
