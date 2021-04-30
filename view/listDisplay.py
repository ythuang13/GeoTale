import pygame


class ListDisplay:
    def __init__(self, pos_x, pos_y, width, height,
                 background_color=(255, 255, 255), ):
        self.image = pygame.Surface((width, height))
        self.image.fill(background_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

        self.background_color = background_color

    def draw(self, win):
        # draw background
        pygame.draw.rect(win, self.background_color, self.rect)

        # draw border
        pygame.draw.rect(win, (0, 0, 0), (self.rect.x - 2, self.rect.y - 2,
                                          self.rect.width + 4,
                                          self.rect.height + 4), 2)

    def events_handling(self, event):
        pass


class ListItem:
    def __init__(self):
        pass
