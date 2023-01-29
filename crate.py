import os
import pygame as pg
from pygameBoilerplate import load_image, load_sound
from paths import PROJECT_ROOT, RESOURCES_DIR
from actor import Actor
import collision


class Crate(Actor):
    def __init__(self, **kwargs):
        assert kwargs is not None, "Must provide keyword arguments to crate constructor"
        assert 'filename' in kwargs, "Must provide keyword argument 'filename' to crate constructor"
        self.filename = kwargs['filename']
        self.collision_type_ = collision.Stationary
        self.world_position_ = (0,0,0)
        self.velocity_ = (0,0,0)
        self.moveRight = False
        self.moveDown = False
        self.sprite = pg.sprite.Sprite()
        pg.sprite.Sprite.__init__(self)
        self.sprite.image, self.sprite.rect= load_image(RESOURCES_DIR,self.filename,-1,1)
        self.resize_scale = 0.2
        self.img = pg.transform.scale(self.sprite.image,((int(self.sprite.rect.width*self.resize_scale)),int(self.sprite.rect.height*self.resize_scale)))
        self.sprite.image = self.img
        self.sprite.rect = self.img.get_rect()
        self.hurtbox = self.sprite.rect
        self.height = 1
        self.width = self.sprite.rect.width
        self.world_position_ = (self.sprite.rect.topleft[0],self.sprite.rect.topleft[1],0)

    def x(self):
        return self.world_position[0]
    def y(self):
        return self.world_position[1]
    def update(self):
        self.draw()

    @property
    def world_position(self):
        return self.world_position_

    @world_position.setter
    def world_position(self, absolute_world_position):
        self.world_position_ = absolute_world_position

    def draw(self):
        posx = self.world_position[0] - self.sprite.rect.width/2
        posy = self.world_position[1] - self.sprite.rect.height/2
        self.sprite.rect.topleft = (posx,posy)
