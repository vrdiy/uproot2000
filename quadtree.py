import os
import pygame as pg
from pygameBoilerplate import load_image, load_sound
from paths import PROJECT_ROOT, RESOURCES_DIR
from actor import Actor
import collision

QUADRANT_ONE = 0
QUADRANT_TWO = 1
QUADRANT_THREE = 2
QUADRANT_FOUR = 3

class QuadTree:
    def __init__(self,surface,rectBounds,numOfObjs = 5):
        assert isinstance(rectBounds,pg.Rect), "Quadtree bounds must be a pygame.Rect instance"
        self.surface = surface
        self.rect = rectBounds
        self.hasChildren = False
        self.children = [None] * 4
        self.childRects = [None] * 4
        self.createChildRects()
        self.objLimit = numOfObjs
        self.objs = set()
        
    def createChildRects(self):
        half_width = self.rect.width / 2
        half_height = self.rect.height / 2
        x = self.rect.x
        y = self.rect.y

        #Quadrant 1/NE
        self.childRects[QUADRANT_ONE] = pg.Rect(x + half_width, y, half_width, half_height)
        #Quadrant 2/NW
        self.childRects[QUADRANT_TWO] = pg.Rect(x, y, half_width, half_height)
        #Quadrant 3/SW
        self.childRects[QUADRANT_THREE] = pg.Rect(x, y + half_height, half_width, half_height)
        #Quadrant 4/SE
        self.childRects[QUADRANT_FOUR] = pg.Rect(x + half_width, y + half_height, half_width, half_height)

    
    def insert(self,obj):
        if self.hasChildren:
            newQuadrant = self.getNewQuadrant(obj)
            if newQuadrant != -1:
                self.children[newQuadrant].insert(obj)
                return
            else:
                print("got bad quadrant")
        self.objs.add(obj)
        if len(self.objs) > self.objLimit and self.rect.width > 1:
            self.subdivide()

    def subdivide(self):
        #Quadrant 1/NE
        self.children[QUADRANT_ONE] = QuadTree(self.surface,self.childRects[QUADRANT_ONE],self.objLimit)
        #Quadrant 2/NW
        self.children[QUADRANT_TWO] = QuadTree(self.surface,self.childRects[QUADRANT_TWO],self.objLimit)
        #Quadrant 3/SW
        self.children[QUADRANT_THREE] = QuadTree(self.surface,self.childRects[QUADRANT_THREE],self.objLimit)
        #Quadrant 4/SE
        self.children[QUADRANT_FOUR] = QuadTree(self.surface,self.childRects[QUADRANT_FOUR],self.objLimit)

        self.hasChildren = True

        for obj in self.objs:
            newQuadrant = self.getNewQuadrant(obj)
            if newQuadrant != -1:
                self.children[newQuadrant].insert(obj)
        self.objs = set()


    def getQuadrants(self,obj):
        #later would do collide list of rects that define obj hitboxes
        pg.Rect.colliderect(obj.hitbox,self.childRects[QUADRANT_ONE])

    def getNewQuadrant(self,obj):
        x = obj.x()
        y = obj.y()
        y_axis_of_this_quadtree = self.rect.x + self.rect.width / 2 # 640 at first layer
        x_axis_of_this_quadtree = self.rect.y + self.rect.height / 2 # 360 at first layer

        top_half_of_this_quadtree = (y < x_axis_of_this_quadtree) and (y + obj.height < x_axis_of_this_quadtree)
        bottom_half_of_this_quadtree = y > x_axis_of_this_quadtree

        if x >= y_axis_of_this_quadtree and top_half_of_this_quadtree:
            return QUADRANT_ONE
        elif x < y_axis_of_this_quadtree and top_half_of_this_quadtree:
            return QUADRANT_TWO
        elif x < y_axis_of_this_quadtree and bottom_half_of_this_quadtree:
            return QUADRANT_THREE
        elif x >= y_axis_of_this_quadtree and bottom_half_of_this_quadtree:
            return QUADRANT_FOUR
        else:
            print(f"{obj},x: {x}, y: {y}")
            print(f"quadtree tested against: ")
            print(f"x: {self.rect.x}, y: {self.rect.y}, width: {self.rect.width}, height: {self.rect.height}")
            return -1

    def processNodes(self):

        if self.hasChildren:
            for quadrant in self.children:
                quadrant.processNodes()
        
            pg.draw.rect(self.surface,pg.Color(187,190,80,255),self.rect,3)
        else:
            pg.draw.rect(self.surface,pg.Color(255,0,0,255),self.rect,1)
