import os
import pygame as pg
from pygameBoilerplate import load_image, load_sound
from paths import PROJECT_ROOT, RESOURCES_DIR
from actor import Actor
import collision
from random import randrange


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
        self.height = self.sprite.rect.height
        self.width = self.sprite.rect.width
        self.boundingBox_ = pg.Rect(self.world_position_[0],self.world_position_[1],self.width,self.height)
        self.world_position_ = (self.sprite.rect.topleft[0],self.sprite.rect.topleft[1],0)
        self.color = pg.Color(255,0,0,255)
        self.collided = False
        self.hasMoved = False


    @property
    def boundingBox(self):
        return self.boundingBox_

    @boundingBox.setter
    def boundingBox(self, rectBounds):
        #print("setter called")
        self.boundingBox_ = pg.Rect(self.world_position_[0],self.world_position_[1],self.width,self.height)

    def x(self):
        return self.world_position[0]
    def y(self):
        return self.world_position[1]
    def update(self):
        self.hasMoved = False
        self.collided = False
        self.move()
        self.draw()
    def onCollision(self, obj):
        if(not self.collided):
            newPos = (self.boundingBox.x-obj.boundingBox.width,self.boundingBox.y-obj.boundingBox.height,0)
            newPos = (self.boundingBox.x+randrange(-50,50),self.boundingBox.y+randrange(-50,50))

            self.world_position = (newPos)
            #otherNewPos = (obj.hurtbox.x+self.hurtbox.width,obj.hurtbox.y+self.hurtbox.height,0)
            #obj.world_position_ = (otherNewPos)
            self.color = pg.Color(0,0,255,255)
            obj.color = pg.Color(0,255,0,255)
            self.collided = True
            self.hasMoved = True
            obj.collided = True
    def onOverlap(self, obj):
        return super().onOverlap(obj)
    def drawRect(self,surface):
        pg.draw.rect(surface,self.color,self.boundingBox,3)

    def move(self):
        if self.world_position[0] > 1280 or self.world_position[0] < 0:
            self.world_position = (640,360,0)
        if self.world_position[1] > 720 or self.world_position[1] < 0:
            self.world_position = (640,360,0)
        if 2 == randrange(1000):
            self.world_position = (self.boundingBox.x+randrange(-20,20),self.boundingBox.y+randrange(-50,50))
            self.hasMoved = True

    @property
    def world_position(self):
        return self.world_position_

    @world_position.setter
    def world_position(self, absolute_world_position):
        #print("setter called")
        self.world_position_ = absolute_world_position
        self.boundingBox = pg.Rect(self.world_position_[0],self.world_position_[1],self.width,self.height)

    def draw(self):
        self.sprite.rect.topleft = (self.world_position[0],self.world_position[1])

