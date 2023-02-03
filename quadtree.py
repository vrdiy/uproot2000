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

OBJ_LIMIT = 5
MIN_SIZE = 256

class QuadTree:
    def __init__(self,rectBounds,numOfObjs = OBJ_LIMIT):
        assert isinstance(rectBounds,pg.Rect), "Quadtree bounds must be a pygame.Rect instance"
        #print("init quadtree")
        self.rect = rectBounds
        self.hasChildren = False
        self.children = [None] * 4
        self.childRects = [None] * 4
        self.createChildRects()
        #print(self.childRects)
        self.objLimit = numOfObjs
        self.objs = set()
        
    def tryMerge(self):
        if self.hasChildren:
            for child in self.children:
                if child.hasChildren:
                    return False
                if len(child.objs) > 0:
                    return False
            self.children = [None] * 4
            self.hasChildren = False

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
        #print("insert called")

        if self.hasChildren:
            #check which child quadtrees it overlaps
            quadrants = self.getQuadrants(obj)
            #print(quadrants)
            for i in range(4):
                if quadrants[i] == True:
                    self.children[i].insert(obj)
        else:
            self.objs.add(obj)
            if (len(self.objs) > self.objLimit) and (self.rect.width > MIN_SIZE):
                self.subdivide()

    def subdivide(self):
        #print("subdivide called")

        #Quadrant 1/NE
        self.children[QUADRANT_ONE] = QuadTree(self.childRects[QUADRANT_ONE],self.objLimit)
        #Quadrant 2/NW
        self.children[QUADRANT_TWO] = QuadTree(self.childRects[QUADRANT_TWO],self.objLimit)
        #Quadrant 3/SW
        self.children[QUADRANT_THREE] = QuadTree(self.childRects[QUADRANT_THREE],self.objLimit)
        #Quadrant 4/SE
        self.children[QUADRANT_FOUR] = QuadTree(self.childRects[QUADRANT_FOUR],self.objLimit)

        self.hasChildren = True

        for obj in self.objs:
            #check which child quadtrees it overlaps
            quadrants = self.getQuadrants(obj)
           # print(quadrants)
            for i in range(4):
                #print(f"quadrant {i}: {quadrants[i]}")
                if quadrants[i] == True:
                    self.children[i].insert(obj)

        self.objs = set()


    def getQuadrants(self,obj):
        #print("get quadrants called")
        assert isinstance(obj.boundingBox,pg.Rect), "Object needs hurtbox which is pg.Rect instance"
        #later would do collide list of rects that define obj hitboxes
       # print(f"obj rect:{obj.hurtbox}, quadrant 1 rect: {self.childRects[QUADRANT_ONE]}")
        inQuadOne = pg.Rect.colliderect(obj.boundingBox,self.childRects[QUADRANT_ONE])
        #print(f"obj rect:{obj.hurtbox}, quadrant 2 rect: {self.childRects[QUADRANT_TWO]}")
        inQuadTwo = pg.Rect.colliderect(obj.boundingBox,self.childRects[QUADRANT_TWO])
       # print(f"obj rect:{obj.hurtbox}, quadrant 3 rect: {self.childRects[QUADRANT_THREE]}")
        inQuadThree = pg.Rect.colliderect(obj.boundingBox,self.childRects[QUADRANT_THREE])
        #print(f"obj rect:{obj.hurtbox}, quadrant 4 rect: {self.childRects[QUADRANT_FOUR]}")
        inQuadFour = pg.Rect.colliderect(obj.boundingBox,self.childRects[QUADRANT_FOUR])
       
        quads =  [inQuadOne,inQuadTwo,inQuadThree,inQuadFour]
       # print(quads)
        return [inQuadOne,inQuadTwo,inQuadThree,inQuadFour]

    def processNodes(self,surface):
        self.tryMerge()
        if self.hasChildren:
            for quadrant in self.children:
                quadrant.processNodes(surface)
        
            pg.draw.rect(surface,pg.Color(187,190,80,255),self.rect,3)
        else:
            for obj in self.objs:
                for other_obj in self.objs:
                    if obj is not other_obj:
                        if pg.Rect.colliderect(obj.boundingBox,other_obj.boundingBox):
                            if collision.handle_collision(obj,other_obj) == 'blocks':
                                obj.onCollision(other_obj)
                            elif collision.handle_collision(obj,other_obj) == 'overlaps':
                                obj.onOverlaps(other_obj)
            unmovedObjs = set()
            for obj in self.objs:
                if not obj.hasMoved:
                    unmovedObjs.add(obj)
            self.objs = unmovedObjs
            pg.draw.rect(surface,pg.Color(255,0,0,255),self.rect,1)
