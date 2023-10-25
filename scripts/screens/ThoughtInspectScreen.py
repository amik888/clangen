#!/usr/bin/env python3
# -*- coding: ascii -*-
import pygame

from ..cat.history import History
from ..cat.thoughts import Thoughts
from scripts.utility import scale
from .Screens import Screens
from scripts.utility import get_text_box_theme
from scripts.cat.cats import Cat

import pygame_gui
from scripts.game_structure.image_button import UIImageButton
from scripts.game_structure.game_essentials import game, screen_x, MANAGER


class ThoughtInspectScreen(Screens):

    def __init__(self, name=None):
        super().__init__(name)
        self.back_button = None
        self.elements = {}
        self.text = None
        self.scroll_container = None
        self.life_text = None
        self.header = None
        self.the_cat = None
        self.other_cat = None #TODO: init other cat w/ thought somehoww

    def screen_switches(self):
        self.hide_menu_buttons()
        self.the_cat = Cat.all_cats.get(game.switches['cat'])
        if self.the_cat.thought_id is None:
            self.header = pygame_gui.elements.UITextBox(str(self.the_cat.name) + ' has no thoughts to inspect. Id ' + str(self.the_cat.thought_id),
                                                        scale(pygame.Rect((200, 180), (1200, -1))),
                                                        object_id=get_text_box_theme(), manager=MANAGER)
            self.life_text = ""
        else:
             
            self.header = pygame_gui.elements.UITextBox(str(self.the_cat.name) + ' thought inspection',
                                                        scale(pygame.Rect((200, 180), (1200, -1))),
                                                        object_id=get_text_box_theme(), manager=MANAGER)
            
            
            
            # compile root text from decision tree
            
            decision_text = Cat.get_decision_text(self.the_cat)
            
            #todo: rename variable
            self.life_text = decision_text
            
            
            print("This feature isn't done yet!")
            

        

        self.scroll_container = pygame_gui.elements.UIScrollingContainer(scale(pygame.Rect((100, 300), (1400, 1000))))
        self.text = pygame_gui.elements.UITextBox(self.life_text,
                                                  scale(pygame.Rect((0, 0), (1100, -1))),
                                                  object_id=get_text_box_theme("#text_box_30_horizleft"),
                                                  container=self.scroll_container, manager=MANAGER)
        self.text.disable()
        self.back_button = UIImageButton(scale(pygame.Rect((50, 50), (210, 60))), "",
                                         object_id="#back_button", manager=MANAGER)
        
        
        #action_1 = 
        #self.action_buttons.append(UIImageButton(scale(pygame.Rect((500, 600), (200, 60))), "",
        #                                 object_id="#back_button", manager=MANAGER))
        
        self.elements["proceed"] = UIImageButton(scale(pygame.Rect((1100, 866), (344, 60))), "",
                                                 object_id="#proceed_button",
                                                 starting_height=2, manager=MANAGER)
        
        self.scroll_container.set_scrollable_area_dimensions((1360 / 1600 * screen_x, self.text.rect[3]))
        
    def update_text(self, new_text):
        self.text.kill()
        del self.text
        self.text = pygame_gui.elements.UITextBox(new_text,
                                                  scale(pygame.Rect((0, 0), (1100, -1))),
                                                  object_id=get_text_box_theme("#text_box_30_horizleft"),
                                                  container=self.scroll_container, manager=MANAGER)
        #also update scroll container size
        #self.scroll_container.kill
        #del self.scroll_container
        self.scroll_container.set_scrollable_area_dimensions((1360 / 1600 * screen_x, self.text.rect[3]))
        

    def exit_screen(self):
        self.header.kill()
        del self.header
        self.text.kill()
        del self.text
        self.scroll_container.kill()
        del self.scroll_container
        self.back_button.kill()
        del self.back_button
        #self.action_button.kill()
        #del self.action_button
        for elem in self.elements:
            self.elements[elem].kill()
        self.elements = {}

    def on_use(self):
        pass

    def handle_event(self, event):
        if game.switches['window_open']:
            pass
        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            if event.ui_element == self.back_button:
                self.change_screen('profile screen')
            elif event.ui_element == self.elements["proceed"]: #TODO: make action buttons
                #todo: eventual input variable ~
                path = Cat.create_decision_path(self.the_cat, game.clan.game_mode) #todo: this is a temporary function to prototype, not the end goal
                self.life_text = Cat.get_decision_text(self.the_cat)
                self.update_text(self.life_text)
            
            
        
        elif event.type == pygame.KEYDOWN and game.settings['keybinds']:
            if event.key == pygame.K_ESCAPE:
                self.change_screen('profile screen')
            
        return
