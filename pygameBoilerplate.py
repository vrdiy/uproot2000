import os
import pygame as pg

def load_image(resourceDirectory,filename, colorkey=None, scale=1):
    full_path = os.path.join(resourceDirectory, filename)
    image = pg.image.load(full_path)
    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()

def load_sound(resourceDirectory,filename):
    assert pg.mixer == True, "mixer module not imported correctly"
    assert pg.mixer.get_init() == True, "mixer module init failed"
    fullname = os.path.join(filename, resourceDirectory)
    sound = pg.mixer.Sound(fullname)

    return sound