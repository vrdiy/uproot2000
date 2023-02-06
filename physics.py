import os
import pygame as pg
from pygameBoilerplate import load_image, load_sound
from paths import PROJECT_ROOT, RESOURCES_DIR
from actor import Actor
import collision
from random import randrange
import numpy as np


class RigidBody():
    def __init__(self):
        self.velocity = (0,0,0)


def solveCollision(obj1,obj2,deltaTime):
    v1 = obj1.velocity
    v2 = obj2.velocity

    obj1_acc = (v2 - v1) / deltaTime
    obj2_acc = (v1 - v2) / deltaTime
    
