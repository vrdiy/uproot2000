import os
import pygame as pg
from abc import ABC, abstractmethod, abstractproperty
from paths import PROJECT_ROOT, RESOURCES_DIR
import collision

class Actor(ABC):

    @abstractmethod
    def __init__(self, **kwargs):
        self.collision_type(collision.Stationary)
        pass

    @abstractmethod
    def update(self):
        pass

    @property
    @abstractmethod
    def world_position(self):
        pass

    @world_position.setter
    @abstractmethod
    def world_position(self,absolute_world_position):
        pass
   
    @property
    def collision_type(self):
        return self.collision_type_

    @collision_type.setter
    def collision_type(self,type):
        self.collision_type_ = type

    