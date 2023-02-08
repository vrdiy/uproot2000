import os
import pygame as pg
from pygameBoilerplate import load_image, load_sound
from paths import PROJECT_ROOT, RESOURCES_DIR
from actor import Actor
import collision
from random import randrange
import numpy as np

DEFAULT_MASS = 1 #lbs
AUTO_MASS_SCALAR = 10

class RigidBody():
    def __init__(self,rectBounds,startingForce = 0,mass = -1):
        self.boundingBox = rectBounds
        self.force = startingForce
        if mass < 0:
            self.autoMass()
        else:
            self.mass = mass
    
    #Calculate approximate mass based on size of bounding box
    def autoMass(self):
        self.mass = (self.boundingBox.width * self.boundingBox.height) / AUTO_MASS_SCALAR


def solveCollision(obj1,obj2,deltaTime):
    v1 = obj1.rigidbody.velocity
    v2 = obj2.rigidbody.velocity

    obj1_acc = (v2 - v1) / deltaTime
    obj2_acc = (v1 - v2) / deltaTime
    
