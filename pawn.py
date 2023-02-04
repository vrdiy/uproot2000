import os
import pygame as pg
from pygameBoilerplate import load_image, load_sound
from paths import PROJECT_ROOT, RESOURCES_DIR
from actor import Actor
import collision


class Pawn(Actor):
    def __init__(self, **kwargs):
        assert kwargs is not None, "Must provide keyword arguments to pawn constructor"
        assert 'filename' in kwargs, "Must provide keyword argument 'filename' to pawn constructor"
        assert 'movemode' in kwargs, "Must provide keyword argument 'movemode' to pawn constructor"
        self.filename = kwargs['filename']
        self.movemode = kwargs['movemode']
        self.collision_type_ = collision.Pawn
        self.world_position_ = (0,0,0)
        self.velocity_ = (0,0,0)
        self.moveRight = False
        self.moveDown = False
        self.sprite = pg.sprite.Sprite()
        pg.sprite.Sprite.__init__(self)
        self.sprite.image, self.sprite.rect= load_image(RESOURCES_DIR,self.filename,-1)

        self.boundingBox_ = self.sprite.rect
        self.collided = False
        self.hasMoved = False

    def x(self):
        return self.world_position[0]
    def y(self):
        return self.world_position[1]
    def update(self):
        self.collided = False
        self.hasMoved = False
        if self.movemode == 'mouse':
            self.movemodeMouse()
        elif self.movemode == 'wander':
            self.movemodeWander()

        self.draw()

    @property
    def boundingBox(self):
        return self.boundingBox_

    @boundingBox.setter
    def boundingBox(self, rectBounds):
        assert isinstance(rectBounds,pg.Rect), "Bounding Box needs to be pygame.Rect instance"
        #print("setter called")
        self.boundingBox_ = rectBounds


    @property
    def world_position(self):
        return self.world_position_

    @world_position.setter
    def world_position(self, absolute_world_position):
        self.world_position_ = absolute_world_position
        self.boundingBox_.x = absolute_world_position[0]
        self.boundingBox_.y = absolute_world_position[1]

    def draw(self):
        posx = self.world_position[0] - self.sprite.rect.width/2
        posy = self.world_position[1] - self.sprite.rect.height/2
        self.sprite.rect.topleft = (posx,posy)

    def movemodeMouse(self):
        pos = pg.mouse.get_pos()
        self.world_position = (pos[0],pos[1],0)
        self.hasMoved = True
    
    def movemodeWander(self, speed =0.1):
        #oldvel = self.velocity_
        oldpos = self.world_position
        screen = pg.display.get_window_size()
        newx = 0
        newy = 0
        if self.moveRight:
            newx = speed + oldpos[0]
        else:
            newx = (speed * -1) + oldpos[0]
        if self.moveDown:
            newy = speed + oldpos[1]
        else:
            newy = (speed * -1) + oldpos[1]

        self.world_position = (newx,newy,0)

        if self.world_position[0] < 0:
            self.moveRight = True
        if self.world_position[0] > screen[0]:
            self.moveRight = False
        if self.world_position[1] < 0:
            self.moveDown = True
        if self.world_position[1] > screen[1]:
            self.moveDown = False
            
        self.hasMoved = True
        
        
        
            
