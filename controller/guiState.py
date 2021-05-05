from controller.settings import *
from controller.geoTale import GeoTale
from tkinter.filedialog import askopenfilename
from os import path
from pygame import mixer
import tkinter
import sys


class GuiState:
    def __init__(self, window):
        self.window = window
        self.state = "main_menu"
        self.time_delta = None
        self.geotale = GeoTale()
        if not self.geotale.network.id:
            self.state = "no_connection_menu"

    def hear_menu(self):
        # events
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if MAIN_MENU_BTN.is_over((mx, my)):
                        MAIN_MENU_BTN.button_color = \
                            MAIN_MENU_BTN.original_button_color
                        self.state = "main_menu"
                    elif HEAR_SUBMIT_BTN.is_over((mx, my)):
                        self.hear_submit()
                    elif ID_SUBMIT_BTN.is_over((mx, my)):
                        self.download_and_play()
            if event.type == pygame.MOUSEMOTION:
                for btn in BTN_GROUP:
                    if btn.is_over((mx, my)):
                        btn.button_color = btn.hover_button_color
                    else:
                        btn.button_color = btn.original_button_color
                if HEAR_SUBMIT_BTN.is_over((mx, my)):
                    HEAR_SUBMIT_BTN.button_color = \
                        HEAR_SUBMIT_BTN.hover_button_color
                else:
                    HEAR_SUBMIT_BTN.button_color = \
                        HEAR_SUBMIT_BTN.original_button_color
                if ID_SUBMIT_BTN.is_over((mx, my)):
                    ID_SUBMIT_BTN.button_color = \
                        ID_SUBMIT_BTN.hover_button_color
                else:
                    ID_SUBMIT_BTN.button_color = \
                        ID_SUBMIT_BTN.original_button_color

            HEAR_ZIP_INPUT.events_handling(event)
            ID_INPUT.events_handling(event)

        # drawing
        self.window.blit(BACKGROUND_SURFACE, (0, 0))
        for widget in HEAR_UI_GROUP:
            widget.draw(self.window)

        # final display update
        pygame.display.flip()

    def hear_submit(self) -> None:
        """
        Handle submit function for the hear screen.
        Pull information from input fields and submit.
        :return: None
        """
        zip_input = HEAR_ZIP_INPUT.text
        if len(zip_input) not in [0, 5]:
            raise ValueError("Zip code is 5 digits")
        query_result = self.geotale.query_story(zip_input)

        if query_result:
            temp_data = []
            for story in query_result:
                story_id = story.get("story_id")
                story_title = story.get("title")
                story_author = story.get("author")
                story_length = story.get("length")
                story_description = story.get("description")
                story_date = story.get("create_date")
                temp_data.append((f"{story_id}: {story_title} by "
                                  f"{story_author}. {story_length}s, "
                                  f"{story_date}",
                                  f"{story_description}"))
            DISPLAY_UI.update_items(temp_data)
        else:
            DISPLAY_UI.update_items([("No data", "No data found"),
                                     ("", ""),
                                     ("", ""),
                                     ("", "")])
        DISPLAY_UI.draw(self.window, True)

    def add_menu(self):
        # events
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if MAIN_MENU_BTN.is_over((mx, my)):
                        MAIN_MENU_BTN.button_color = \
                            MAIN_MENU_BTN.original_button_color
                        self.state = "main_menu"
                    elif ADD_SUBMIT_BTN.is_over((mx, my)):
                        self.add_submit()
                    elif ADD_FILE_BTN.is_over((mx, my)):
                        self.add_file_selection()
            if event.type == pygame.MOUSEMOTION:
                for btn in BTN_GROUP:
                    if btn.is_over((mx, my)):
                        btn.button_color = btn.hover_button_color
                    else:
                        btn.button_color = btn.original_button_color
                if ADD_SUBMIT_BTN.is_over((mx, my)):
                    ADD_SUBMIT_BTN.button_color = \
                        ADD_SUBMIT_BTN.hover_button_color
                else:
                    ADD_SUBMIT_BTN.button_color = \
                        ADD_SUBMIT_BTN.original_button_color
                if ADD_FILE_BTN.is_over((mx, my)):
                    ADD_FILE_BTN.button_color = \
                        ADD_FILE_BTN.hover_button_color
                else:
                    ADD_FILE_BTN.button_color = \
                        ADD_FILE_BTN.original_button_color

            ADD_ZIP_INPUT.events_handling(event)
            ADD_TITLE_INPUT.events_handling(event)
            ADD_AUTHOR_INPUT.events_handling(event)
            ADD_DESC_INPUT.events_handling(event)
            ADD_FILE_INPUT.events_handling(event)

        # drawing
        self.window.blit(BACKGROUND_SURFACE, (0, 0))
        for widget in ADD_UI_GROUP:
            widget.draw(self.window)

        # final display update
        pygame.display.flip()

    def add_submit(self) -> None:
        """
        Handle submit function for the add screen.
        Pull information from input fields and submit
        :return: None
        """
        # get input
        zip_input = ADD_ZIP_INPUT.text
        title_input = ADD_TITLE_INPUT.text
        author_input = ADD_AUTHOR_INPUT.text
        description_input = ADD_DESC_INPUT.text
        file_input = ADD_FILE_INPUT.text

        # reset
        ADD_ZIP_INPUT.text = ""
        ADD_TITLE_INPUT.text = ""
        ADD_AUTHOR_INPUT.text = ""
        ADD_DESC_INPUT.text = ""
        ADD_FILE_INPUT.text = ""
        pygame.display.flip()

        # send information
        self.geotale.add_story(zip_input, title_input, author_input,
                               file_input, description_input)

    def main_menu(self):
        # events
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
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
                    if EXIT_MENU_BTN.is_over((mx, my)):
                        EXIT_MENU_BTN.button_color = \
                            EXIT_MENU_BTN.original_button_color
                        self.quit()
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
        EXIT_MENU_BTN.draw(self.window)

        # final display update
        pygame.display.flip()

    def no_connection_menu(self):
        # event
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if EXIT_MENU_BTN.is_over((mx, my)):
                        EXIT_MENU_BTN.button_color = \
                            EXIT_MENU_BTN.original_button_color
                        self.quit()
            if event.type == pygame.MOUSEMOTION:
                for btn in BTN_GROUP:
                    if btn.is_over((mx, my)):
                        btn.button_color = btn.hover_button_color
                    else:
                        btn.button_color = btn.original_button_color

        # draw
        self.window.blit(BACKGROUND_SURFACE, (0, 0))
        EXIT_MENU_BTN.draw(self.window)

        # text
        self.window.blit(MENU_TITLE_SURFACE, (MENU_X, MENU_Y))
        text_font = pygame.font.SysFont(FONT_CHOICE, 50)
        text_surface = text_font.render("No Connection!", True, BLACK)
        self.window.blit(text_surface, (180, 200))

        # final display update
        pygame.display.flip()

    def state_manager(self):
        if self.state == "main_menu":
            self.main_menu()
        elif self.state == "hear_menu":
            self.hear_menu()
        elif self.state == "add_menu":
            self.add_menu()
        elif self.state == "no_connection_menu":
            self.no_connection_menu()

    def quit(self):
        pygame.quit()
        self.geotale.quit()
        sys.exit()

    @staticmethod
    def add_file_selection():
        root = tkinter.Tk()
        root.withdraw()
        file_path = askopenfilename(filetype=(("Audio files", ".mp3 .wav"),))
        root.update()
        if file_path:
            ADD_FILE_INPUT.text = file_path

    def download_and_play(self) -> None:
        """
        Download and play the audio file from server, check if file exist first
        :return: None
        """
        try:
            story_id = int(ID_INPUT.text)
        except ValueError:
            raise ValueError("Invalid story id")

        # check if file exist already
        file_exist = path.exists(path.join("tmp", f"{story_id}.wav")) \
            or path.exists(path.join("tmp", f"{story_id}.mp3"))

        # if not, download
        if not file_exist:
            self.geotale.download_story(story_id)

        # select file
        if path.exists(path.join("tmp", f"{story_id}.wav")):
            file_path = path.join("tmp", f"{story_id}.wav")
        elif path.exists(path.join("tmp", f"{story_id}.mp3")):
            file_path = path.join("tmp", f"{story_id}.mp3")

        # play audio
        mixer.music.load(file_path)
        mixer.music.play()
