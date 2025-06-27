from . import mopgi
import pygame
from pygame.locals import *

class Label(mopgi.Widget):
    def __init__(self, parent, rect, text):
        mopgi.Widget.__init__(self, parent, rect)
        self.text = text
        self.fgcolor = parent.fgcolor
        self.bgcolor = parent.bgcolor

    def setfgcolor(self, color):
        self.fgcolor = color
        self.parent.update()

    def setbgcolor(self, color):
        self.bgcolor = color
        self.parent.update()

    def setfont(self, font):
        self.font = font

    def paint(self, screen):
        pygame.draw.rect(screen, self.bgcolor, self.rect)
        y=self.rect.y
        if (type(self.text) == str): # string
            surface=self.getfont().render(self.text, True, self.fgcolor)
            screen.blit(surface, (self.rect.x, self.rect.y))
        elif (type(self.text) == list):
            for t in self.text:
                surface=self.getfont().render(t, True, self.fgcolor)
                screen.blit(surface, (self.rect.x, y))
                y+=self.getfont().get_height()

                
        
