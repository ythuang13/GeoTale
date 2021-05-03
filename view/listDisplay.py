import pygame


class ListDisplay:
    def __init__(self, pos_x, pos_y, width, height,
                 background_color=(255, 255, 255), item_count=4):
        self.image = pygame.Surface((width, height))
        self.image.fill(background_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

        self.background_color = background_color

        self.item_count = item_count
        self.item_list = [ListItem(pos_x + 2,
                                   pos_y + (height // item_count + 1) * x,
                                   width - 3, (height // item_count) - 4)
                          for x in range(self.item_count)]

    def draw(self, win):
        # draw background
        pygame.draw.rect(win, self.background_color, self.rect)

        # draw border
        pygame.draw.rect(win, (0, 0, 0), (self.rect.x - 2, self.rect.y - 2,
                                          self.rect.width + 4,
                                          self.rect.height + 4), 2)

        # draw items
        for item in self.item_list:
            item.draw(win)

    def events_handling(self, event):
        pass


class ListItem:
    def __init__(self, pos_x, pos_y, width, height,
                 background_color=(220, 220, 220),
                 title="No title", description="No description",
                 title_color=(0, 0, 0), font=None, font_size=35):
        self.image = pygame.Surface((width, height))
        self.image.fill(background_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

        self.background_color = background_color

        # text category
        self.title = title
        self.title_color = title_color
        self.font = pygame.font.SysFont(font, font_size)
        self.text_surface = self.font.render(self.title, True, self.title_color)

        # description category
        self.description = description
        self.description_surface = self.font.render(self.description,
                                                    True, self.title_color)

    def draw(self, win):
        # draw background
        pygame.draw.rect(win, self.background_color, self.rect)

        # draw border
        pygame.draw.rect(win, (0, 0, 0), (self.rect.x - 2, self.rect.y - 2,
                                          self.rect.width + 4,
                                          self.rect.height + 4), 1)

        # draw text and description
        win.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))
        _, y_offset = self.text_surface.get_size()
        win.blit(self.description_surface, (self.rect.x + 5,
                                            self.rect.y + 5 + y_offset + 2))

    def events_handling(self, event):
        pass
