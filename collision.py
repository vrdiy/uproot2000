import os
import pygame as pg
from abc import ABC, abstractmethod, abstractproperty
from paths import PROJECT_ROOT, RESOURCES_DIR


class CollisionType():
    def __init__(self,blocks = (),ignores = (), overlaps = ()):
        self.blocks = set(blocks)
        self.ignores = set(ignores)
        self.overlaps = set(overlaps)

#default actor collision type
class Stationary(CollisionType):
    __instance = None
    def __new__(cls):
        if Stationary.__instance is None:
            Stationary.__instance = object.__new__(cls)
        return Stationary.__instance 

    def __init__(self):
        super().__init__(blocks=["Pawn","Stationary"], ignores=[],overlaps=[])

    def __str__(self) -> str:
        return 'Stationary Collision'

class Pawn(CollisionType):
    __instance = None
    def __new__(cls):
        if Pawn.__instance is None:
            Pawn.__instance = object.__new__(cls)
        return Pawn.__instance 

    def __init__(self):
        super().__init__(blocks=["Pawn"], ignores=[],overlaps=["Pickup"])
    def __str__(self) -> str:
        return 'Pawn Collision'

class Pickup(CollisionType):
    __instance = None
    def __new__(cls):
        if Pickup.__instance is None:
            Pickup.__instance = object.__new__(cls)
        return Pickup.__instance 

    def __init__(self):
        super().__init__(blocks=[], ignores=[],overlaps=["Pawn"])
    def __str__(self) -> str:
        return 'Pickup Collision'



def handle_collision(actor1,actor2):
    a1_collision = actor1.collision_type.__name__
    a2_collision = actor2.collision_type.__name__
    a2_collision_class = globals()[a2_collision]
    a2_collision_instance = a2_collision_class()

    if a1_collision in a2_collision_instance.blocks:
        return 'blocks'
    elif a1_collision in a2_collision_instance.overlaps:
        return 'overlaps'
    elif a1_collision in a2_collision_instance.ignores:
        return 'ignores'
    else:
        return 'ignores'