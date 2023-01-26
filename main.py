import os
import pygame as pg
from pygameBoilerplate import load_image, load_sound
from paths import PROJECT_ROOT, RESOURCES_DIR
from pawn import Pawn
import collision
from uprootCharacter import UprootCharacter

def main():
    pg.init()
    
    screen = pg.display.set_mode((1280,720),pg.SCALED)
    #pg.display.toggle_fullscreen()
    pg.mouse.set_visible(False)
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    pg.display.flip()

    uproot = UprootCharacter(filename = 'uprootpixel.png',movemode = 'mouse')
    uprootNPC = UprootCharacter(filename = 'uprootpixel.png',movemode = 'wander')

    sprites = pg.sprite.RenderPlain(([uproot.sprite,uprootNPC.sprite]))
    print(uproot.collision_type)
    uproot.collision_type = collision.Stationary
    print(uproot.collision_type)

    print(pg.display.get_window_size())
    exit = False
    while not exit:
        #print(uproot.world_position)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit = True
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                exit = True
        uproot.update()
        uprootNPC.update()
        screen.blit(background,(0,0))
        sprites.draw(screen)
        pg.display.flip()
        
    pg.quit()

main()