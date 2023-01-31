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
        self.quadTree = QuadTree(rectBounds)

    def tick(self):
        for actor in self.actors:
            if actor.hasMoved:
                self.quadTree.insert(actor)
            actor.update()
    
    def checkCollision(self,surface):
        self.quadTree.processNodes(surface)

    def add(self,actors):
        #assert isinstance(actors,list) or isinstance(actors,Actor), "Only add actors to world"
        for actor in actors:
            self.actors.add(actor)
            self.quadTree.insert(actor)


    
