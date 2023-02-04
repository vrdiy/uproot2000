import os
import pygame as pg
from abc import ABC, abstractmethod, abstractproperty
from paths import PROJECT_ROOT, RESOURCES_DIR
import collision

class Actor(ABC):

    @abstractmethod
    def __init__(self, **kwargs):
        self.collision_type(collision.Stationary)
        self.world_position_ = (0,0,0)
        self.boundingBox_ = pg.Rect(0,0,100,100)
        self.collided = False
        self.hasMoved = False
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def onCollision(self,obj):
        pass
    
    @abstractmethod
    def onOverlap(self,obj):
        pass

    @property
    @abstractmethod
    def world_position(self):
        return self.world_position_

    @world_position.setter
    @abstractmethod
    def world_position(self,absolute_world_position):
        assert isinstance(absolute_world_position,tuple), "World position is a 3 dimensional tuple"
        self.world_position_ = absolute_world_position
        return

    @property
    def boundingBox(self):
        pass
    @boundingBox.setter
    def boundingBox(self,rectBounds):
        pass

    @property
    def collision_type(self):
        return self.collision_type_

    @collision_type.setter
    def collision_type(self,type):
        self.collision_type_ = type

    