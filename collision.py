import os
import pygame as pg
from abc import ABC, abstractmethod, abstractproperty
from paths import PROJECT_ROOT, RESOURCES_DIR


class CollisionType(ABC):
    
    @property
    @abstractmethod
    def ignore(self):
        pass

    @ignore.setter
    @abstractmethod
    def ignore(self,collision_types_to_ignore):
        pass
   
    @property
    @abstractmethod
    def collide(self):
        pass

    @collide.setter
    @abstractmethod
    def collide(self,collision_types_to_collide):
        pass
   
    @property
    @abstractmethod
    def overlap(self):
        pass

    @overlap.setter
    @abstractmethod
    def overlap(self,collision_types_to_overlap):
        pass


class PawnCollision(CollisionType):
    def __init__(self):
        self.ignore_ = []
        self.collide_ = []
        self.overlap_ = []

    def __str__(self) -> str:
        return 'Pawn Collision'

    @property
    def ignore(self):
        return self.ignore_

    @ignore.setter
    def ignore(self, collision_types_to_ignore):
        self.ignore_ = collision_types_to_ignore

    @property
    def collide(self):
        return self.collide_

    @collide.setter
    def collide(self, collision_types_to_collide):
        self.collide_ = collision_types_to_collide


    @property
    def overlap(self):
        return self.overlap_

    @overlap.setter
    def world_position(self, collision_types_to_overlap):
        self.overlap_ = collision_types_to_overlap

class StationaryCollision(CollisionType):
    def __init__(self):
        self.ignore_ = []
        self.collide_ = []
        self.overlap_ = []

    def __str__(self) -> str:
        return 'Stationary Collision'

    @property
    def ignore(self):
        return self.ignore_

    @ignore.setter
    def ignore(self, collision_types_to_ignore):
        self.ignore_ = collision_types_to_ignore

    @property
    def collide(self):
        return self.collide_

    @collide.setter
    def collide(self, collision_types_to_collide):
        self.collide_ = collision_types_to_collide


    @property
    def overlap(self):
        return self.overlap_

    @overlap.setter
    def world_position(self, collision_types_to_overlap):
        self.overlap_ = collision_types_to_overlap
