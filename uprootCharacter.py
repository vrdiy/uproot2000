import os
import pygame as pg
from pygameBoilerplate import load_image, load_sound
from paths import PROJECT_ROOT, RESOURCES_DIR
from actor import Actor
import collision
from pawn import Pawn

class UprootCharacter(Pawn):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    