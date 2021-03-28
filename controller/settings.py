from view.button import Button
from view.textInput import TextInput
import string
import pygame

# socket settings
HOST = "52.39.77.232"
PORT = 5555
HEADER_SIZE = 10
BUFFER_SIZE = 1024 * 4
FORMAT = "utf-8"

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

# render text
MENU_TITLE_SURFACE = MENU_FONT.render("GeoTale", True, BLACK)

# load image/assets
BACKGROUND_SURFACE = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND_SURFACE.fill(BG_COLOR)

# gui ui elements
# main menu
HEAR_MENU_BTN = Button(360, 260, 180, 60, LIGHT_BLUE, SKY_BLUE,
                       text="Hear story", font=FONT_CHOICE)
ADD_MENU_BTN = Button(360, 330, 180, 60, LIGHT_BLUE, SKY_BLUE,
                      text="Add Story", font=FONT_CHOICE)
MAIN_MENU_BTN = Button(670, 50, 50, 50, LIGHT_BLUE, SKY_BLUE,
                       text="H", font=FONT_CHOICE)
BTN_GROUP = [ADD_MENU_BTN, HEAR_MENU_BTN, MAIN_MENU_BTN]

# hear menu
HEAR_ZIP_INPUT = TextInput(205, 50, 300, 50, text="", font_size=50,
                           max_string_length=5, restriction=string.digits,
                           description="Zip code: ")
HEAR_UI_GROUP = [MAIN_MENU_BTN, HEAR_ZIP_INPUT]

# add menu
ADD_ZIP_INPUT = TextInput(220, 50, 300, 45, text="", font_size=50,
                          max_string_length=5, restriction=string.digits,
                          description="Zip code: ")
ADD_TITLE_INPUT = TextInput(220, 110, 300, 45, text="", font_size=50,
                            max_string_length=-1, description="Title: ")
ADD_AUTHOR_INPUT = TextInput(220, 170, 300, 45, text="", font_size=50,
                             max_string_length=-1, description="Author: ")
ADD_DESC_INPUT = TextInput(220, 230, 300, 45, text="", font_size=50,
                           max_string_length=-1, description="Description: ")
ADD_UI_GROUP = [MAIN_MENU_BTN, ADD_ZIP_INPUT, ADD_TITLE_INPUT,
                ADD_AUTHOR_INPUT, ADD_DESC_INPUT]
