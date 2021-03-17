from controller.settings import *
from controller.guiState import GuiState
import pygame


# General settings
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
pygame.mouse.set_visible(MOUSE_VISIBILITY)

# class initialize
gui_state = GuiState(screen)


def main():
    while True:
        gui_state.state_manager()


if __name__ == "__main__":
    main()
