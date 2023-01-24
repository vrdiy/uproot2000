import os
import pygame as pg
from pygameBoilerplate import load_image, load_sound
from paths import PROJECT_ROOT, RESOURCES_DIR
from actor import Actor
from collision import PawnCollision


class Pawn(Actor):
    def __init__(self, **kwargs):
        assert kwargs is not None, "Must provide keyword arguments to pawn constructor"
        assert 'filename' in kwargs, "Must provide keyword argument 'filename' to pawn constructor"
        assert 'movemode' in kwargs, "Must provide keyword argument 'movemode' to pawn constructor"
        self.filename = kwargs['filename']
        self.movemode = kwargs['movemode']
        self.collision_type_ = PawnCollision()
        self.world_position_ = (0,0,0)
        self.sprite = pg.sprite.Sprite()
        pg.sprite.Sprite.__init__(self)
        self.sprite.image, self.sprite.rect= load_image(RESOURCES_DIR,self.filename,-1)

    def update(self):
        if self.movemode == 'mouse':
            self.movemodeMouse()

    @property
    def world_position(self):
        return self.world_position_

    @world_position.setter
    def world_position(self, absolute_world_position):
        self.world_position_ = absolute_world_position

    def movemodeMouse(self):
        pos = pg.mouse.get_pos()
        self.world_position = (1,1,1)
        posx = pos[0] - self.sprite.rect.width/2
        posy = pos[1] - self.sprite.rect.height/2

        self.sprite.rect.topleft = (posx,posy)