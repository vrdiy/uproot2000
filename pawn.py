import os
import pygame as pg
from pygameBoilerplate import load_image, load_sound
from paths import PROJECT_ROOT, RESOURCES_DIR


class Pawn(pg.sprite.Sprite):
    def __init__(self, **kwargs):
        assert kwargs is not None, "Must provide keyword arguments to pawn constructor"
        assert 'filename' in kwargs, "Must provide keyword argument 'filename' to pawn constructor"
        assert 'movemode' in kwargs, "Must provide keyword argument 'movemode' to pawn constructor"
        self.filename = kwargs['filename']
        self.movemode = kwargs['movemode']
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(RESOURCES_DIR,self.filename,-1)

    def update(self):
        if self.movemode == 'mouse':
            self.movemodeMouse()


    def movemodeMouse(self):
        pos = pg.mouse.get_pos()
        posx = pos[0] - self.rect.width/2
        posy = pos[1] - self.rect.height/2

        self.rect.topleft = (posx,posy)