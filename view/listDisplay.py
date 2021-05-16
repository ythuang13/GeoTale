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

        self.items_data = list()
        self.displayed_items = list()
        self.display_counter = 0

    def draw(self, win, update=False):
        # draw background
        pygame.draw.rect(win, self.background_color, self.rect)

        # draw border
        pygame.draw.rect(win, (0, 0, 0), (self.rect.x - 2, self.rect.y - 2,
                                          self.rect.width + 4,
                                          self.rect.height + 4), 2)

        # draw items
        for item in self.item_list:
            item.draw(win, update)

    def events_handling(self, event):
        pass

    def update_items(self, data: list) -> None:
        """
        update the items in the list display
        :param data: list of data to display for the items
        :return: None
        """
        self.items_data = data
        self.display_counter = 0
        self.displayed_items = self.items_data[0:self.item_count] \
            if len(self.items_data) >= self.item_count else self.items_data[0:]
        self.display_update()

    def display_update(self):
        for i, (item_title, item_desc) in enumerate(self.displayed_items):
            self.item_list[i].title = item_title
            self.item_list[i].description = item_desc

        for j in range(i + 1, self.item_count):
            self.item_list[j].title = ""
            self.item_list[j].description = ""

    def list_up(self):
        if self.display_counter > 0:
            self.display_counter -= 1
            self.displayed_items = self.items_data[self.item_count
                                                   * self.display_counter:
                                                   self.item_count
                                                   + (self.item_count
                                                      * self.display_counter)
                                                   ] \
                if len(self.items_data) >= self.item_count \
                else self.items_data[self.item_count * self.display_counter:]
            self.display_update()

    def list_down(self):
        if self.display_counter < len(self.items_data) // 5:
            self.display_counter += 1
            self.displayed_items = self.items_data[self.item_count
                                                   * self.display_counter:
                                                   self.item_count
                                                   + (self.item_count
                                                      * self.display_counter)
                                                   ] \
                if len(self.items_data) >= self.item_count \
                else self.items_data[self.item_count * self.display_counter:]
            self.display_update()


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
        self.title_surface = self.font.render(self.title, True,
                                              self.title_color)

        # description category
        self.description = description
        self.description_surface = self.font.render(self.description,
                                                    True, self.title_color)

    def draw(self, win, update=False):
        # draw background
        pygame.draw.rect(win, self.background_color, self.rect)

        # draw border
        pygame.draw.rect(win, (0, 0, 0), (self.rect.x - 2, self.rect.y - 2,
                                          self.rect.width + 4,
                                          self.rect.height + 4), 1)

        # draw text and description
        if update:
            self.title_surface = self.font.render(self.title, True,
                                                  self.title_color)
            self.description_surface = self.font.render(self.description,
                                                        True, self.title_color)

        win.blit(self.title_surface, (self.rect.x + 5, self.rect.y + 5))
        _, y_offset = self.title_surface.get_size()
        win.blit(self.description_surface, (self.rect.x + 5,
                                            self.rect.y + 5 + y_offset + 2))

    def events_handling(self, event):
        pass
