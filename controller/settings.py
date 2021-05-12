from view.button import Button
from view.textInput import TextInput
from view.listDisplay import ListDisplay
from os import path
import string
import pygame

# socket settings
HOST = "54.186.6.243"
PORT = 5555
HEADER_SIZE = 10
BUFFER_SIZE = 1024 * 4
FORMAT = "utf-8"

# gui settings
CAPTION = "GeoTale"
SCREEN_WIDTH, SCREEN_HEIGHT = 720, 480
MOUSE_VISIBILITY = True

# elements setting
MENU_X, MENU_Y = 180, 50

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
HEAR_MENU_BTN = Button(360, 190, 180, 60, LIGHT_BLUE, SKY_BLUE,
                       text="Hear story", font=FONT_CHOICE)
ADD_MENU_BTN = Button(360, 260, 180, 60, LIGHT_BLUE, SKY_BLUE,
                      text="Add Story", font=FONT_CHOICE)
HOME_BTN = Button(670, 50, 50, 50, LIGHT_BLUE, SKY_BLUE,
                  image=path.join("asset", "home.png"), font=FONT_CHOICE)
EXIT_MENU_BTN = Button(360, 330, 180, 60, LIGHT_BLUE, SKY_BLUE,
                       text="Exit", font=FONT_CHOICE)
BTN_GROUP = [ADD_MENU_BTN, HEAR_MENU_BTN, HOME_BTN, EXIT_MENU_BTN]


# hear menu
HEAR_ZIP_INPUT = TextInput(205, 25, 300, 50, text="", font_size=50,
                           max_string_length=5, restriction=string.digits,
                           description="Zip code: ")
HEAR_SUBMIT_BTN = Button(575, 50, 120, 50, LIGHT_BLUE, SKY_BLUE, text="Submit",
                         font=FONT_CHOICE)
ID_INPUT = TextInput(205, 85, 300, 50, text="", font_size=50,
                     restriction=string.digits, description="Story id: ")
ID_SUBMIT_BTN = Button(575, 110, 120, 50, LIGHT_BLUE, SKY_BLUE, text="Listen",
                       font=FONT_CHOICE)
DISPLAY_UI = ListDisplay(50, 150, 585, 300, item_count=4)
UP_BTN = Button(670, 250, 50, 50, LIGHT_BLUE, SKY_BLUE,
                image=path.join("asset", "up.png"))
DOWN_BTN = Button(670, 320, 50, 50, LIGHT_BLUE, SKY_BLUE,
                  image=path.join("asset", "down.png"))
HEAR_UI_GROUP = [HOME_BTN, HEAR_ZIP_INPUT, HEAR_SUBMIT_BTN, ID_SUBMIT_BTN,
                 ID_INPUT, DISPLAY_UI, UP_BTN, DOWN_BTN]


# add menu
ADD_ZIP_INPUT = TextInput(275, 50, 300, 45, text="", font_size=50,
                          max_string_length=5, restriction=string.digits,
                          description="Zip code: ")
ADD_TITLE_INPUT = TextInput(275, 110, 300, 45, text="", font_size=50,
                            max_string_length=15, description="Title: ")
ADD_AUTHOR_INPUT = TextInput(275, 170, 300, 45, text="", font_size=50,
                             max_string_length=15, description="Author: ")
ADD_DESC_INPUT = TextInput(275, 230, 300, 45, text="", font_size=50,
                           max_string_length=128, description="Description: ")
ADD_FILE_INPUT = TextInput(275, 290, 300, 45, text="", font_size=50,
                           max_string_length=-1, description="File: ")
ADD_FILE_BTN = Button(615, 315, 50, 35, LIGHT_BLUE, SKY_BLUE,
                      text="...", font=FONT_CHOICE)
ADD_SUBMIT_BTN = Button(350, 400, 150, 50, LIGHT_BLUE, SKY_BLUE, text="Submit",
                        font=FONT_CHOICE)
ADD_UI_GROUP = [HOME_BTN, ADD_ZIP_INPUT, ADD_TITLE_INPUT,
                ADD_AUTHOR_INPUT, ADD_DESC_INPUT, ADD_FILE_INPUT,
                ADD_SUBMIT_BTN, ADD_FILE_BTN]
