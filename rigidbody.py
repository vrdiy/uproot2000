import os
import pygame as pg
from pygameBoilerplate import load_image, load_sound
from paths import PROJECT_ROOT, RESOURCES_DIR
from actor import Actor
import collision
from random import randrange


class RigidBody():
    def __init__(self):
        self.velocity = (0,0,0)
        