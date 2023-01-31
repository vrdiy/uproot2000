import os
import pygame as pg
from abc import ABC, abstractmethod, abstractproperty
from paths import PROJECT_ROOT, RESOURCES_DIR
import collision
from actor import Actor
from quadtree import QuadTree

class World():
    def __init__(self,rectBounds):
        self.actors = set()
        self.area = QuadTree()

    

    def tick(self):
        for actor in self.actors:
            actor.update
    def add(self,actor):
        assert isinstance(actor,Actor), "Only add actors to world"
        self.actors.add(actor)
