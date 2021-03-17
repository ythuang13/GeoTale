from controller.settings import *
import sys


class GuiState:
    def __init__(self, window):
        self.window = window
        self.state = "main_menu"
        self.time_delta = None

    def hear_menu(self):
        # events
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if MAIN_MENU_BTN.is_over((mx, my)):
                        MAIN_MENU_BTN.button_color = \
                            MAIN_MENU_BTN.original_button_color
                        self.state = "main_menu"
            if event.type == pygame.MOUSEMOTION:
                for btn in BTN_GROUP:
                    if btn.is_over((mx, my)):
                        btn.button_color = btn.hover_button_color
                    else:
                        btn.button_color = btn.original_button_color
            ZIP_INPUT.events_handling(event)

        # drawing
        self.window.blit(BACKGROUND_SURFACE, (0, 0))
        self.window.blit(ZIP_SURFACE, (50, 50))
        MAIN_MENU_BTN.draw(self.window)
        ZIP_INPUT.draw(self.window)

        # final display update
        pygame.display.flip()

    def add_menu(self):
        # events
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if MAIN_MENU_BTN.is_over((mx, my)):
                        MAIN_MENU_BTN.button_color = \
                            MAIN_MENU_BTN.original_button_color
                        self.state = "main_menu"
            if event.type == pygame.MOUSEMOTION:
                for btn in BTN_GROUP:
                    if btn.is_over((mx, my)):
                        btn.button_color = btn.hover_button_color
                    else:
                        btn.button_color = btn.original_button_color

        # drawing
        self.window.blit(BACKGROUND_SURFACE, (0, 0))
        MAIN_MENU_BTN.draw(self.window)

        # final display update
        pygame.display.flip()

    def main_menu(self):
        # events
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if ADD_MENU_BTN.is_over((mx, my)):
                        ADD_MENU_BTN.button_color = \
                            ADD_MENU_BTN.original_button_color
                        self.state = "add_menu"
                    elif HEAR_MENU_BTN.is_over((mx, my)):
                        HEAR_MENU_BTN.button_color = \
                            HEAR_MENU_BTN.original_button_color
                        self.state = "hear_menu"
            if event.type == pygame.MOUSEMOTION:
                for btn in BTN_GROUP:
                    if btn.is_over((mx, my)):
                        btn.button_color = btn.hover_button_color
                    else:
                        btn.button_color = btn.original_button_color
        # drawing
        self.window.blit(BACKGROUND_SURFACE, (0, 0))
        self.window.blit(MENU_TITLE_SURFACE, (MENU_X, MENU_Y))
        ADD_MENU_BTN.draw(self.window)
        HEAR_MENU_BTN.draw(self.window)

        # final display update
        pygame.display.flip()

    def state_manager(self):
        if self.state == "main_menu":
            self.main_menu()
        elif self.state == "hear_menu":
            self.hear_menu()
        elif self.state == "add_menu":
            self.add_menu()
