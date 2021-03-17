from view.button import Button
from view.textInput import TextInput
import string
import pygame

# gui settings
CAPTION = "GeoTale"
SCREEN_WIDTH, SCREEN_HEIGHT = 720, 480
MOUSE_VISIBILITY = True

# elements setting
MENU_X, MENU_Y = 180, 80

# preset colors
BG_COLOR = (250, 250, 180)  # egg shell
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE = (51, 173, 255)
LIGHT_BLUE = (128, 204, 255)

# pygame font
pygame.font.init()  # initialize font
FONT_CHOICE = "georgia"
MENU_FONT = pygame.font.SysFont(FONT_CHOICE, 100)
ZIP_FONT = pygame.font.SysFont(FONT_CHOICE, 35)

# render text
MENU_TITLE_SURFACE = MENU_FONT.render("GeoTale", True, BLACK)
ZIP_SURFACE = ZIP_FONT.render("Zip Code: ", True, BLACK)

# load image/assets
BACKGROUND_SURFACE = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND_SURFACE.fill(BG_COLOR)

# gui ui elements
HEAR_MENU_BTN = Button(360, 260, 180, 60, LIGHT_BLUE, SKY_BLUE,
                       text="Hear story", font=FONT_CHOICE)
ADD_MENU_BTN = Button(360, 330, 180, 60, LIGHT_BLUE, SKY_BLUE,
                      text="Add Story", font=FONT_CHOICE)
MAIN_MENU_BTN = Button(670, 50, 50, 50, LIGHT_BLUE, SKY_BLUE,
                       text="H", font=FONT_CHOICE)
BTN_GROUP = [ADD_MENU_BTN, HEAR_MENU_BTN, MAIN_MENU_BTN]

ZIP_INPUT = TextInput(205, 50, 300, 50, text="", font_size=50,
                      max_string_length=5, restriction=string.digits)
