from Corn import *
from Mouse import *
import random
import sys
sys.dont_write_bytecode = True
 
class World(object):
    karte = None
    things = None
    xSize = 0
    ySize = 0
    dict_things = None
    counter = 0
    

    def __init__(self,x,y):
        self.karte = [[None for i in range(y)] for i in range(x)]
        self.xSize = x
        self.ySize = y
        self.dict_things = dict()
        
    def pasteobject(self,x,y,object_paste):
        self.karte[y][x] = object_paste
        if object_paste == 'm':
            self.dict_things['m' + str(self.counter)] = object_paste
            self.counter += 1
        if object_paste == 'c':
            self.dict_things['c' + str(self.counter)] = object_paste
            self.counter += 1

    def pasterandomobjects(self,number,obj_type):
        for i in range(int(number)):
            #http://stackoverflow.com/questions/2772528/getting-the-indices-of-all-non-none-items-from-a-sub-list-in-python
            if not any([any([j is None for j in row]) for row in self.karte]):
                print("Error, not enough space to insert objects")
                return
            # Falls noch platz ist, fuege hinzu
            while True:
                x = random.randint(0,self.xSize-1)
                y = random.randint(0,self.ySize-1)
                if self.karte[y][x] == None:
                    break
            if obj_type == 'c':
                self.pasteobject(x,y,Corn(0,(y,x),5))
            elif obj_type == 'm':
                self.pasteobject(x,y,Mouse(0,(y,x),5))
                
    def removeobject(self,x,y,object_remove):
        self.karte[y][x] = None
        return self.karte
    def worldmap(self):
        line = ""
        for y in range(len(self.karte)):
            for x in range(len(self.karte[0])):
                if self.karte[y][x]:
                    line += self.karte[y][x].symbol
                else:
                    line += " "
            line += "\n"
        return line
    def getpos(self,a,b):
        if self.karte[a-1][b-1] == None:
            print('No thing here')
        if a==0 or b == 0:
            print('Position ungueltig')
        else:
            print(self.karte[a-1][b-1].symbol)
    def get_neighbour(self,x,y,p):
        res = [None,x,y]
        if p == 'n':
            if y < self.ySize-1:
                res[0] = self.karte[y+1][x]
                res[2]+= 1
            else:
                res[0] = self.karte[0][x]
                res[2] = 0
        if p == 's':
            if y > 0:
                res[0] = self.karte[y-1][x]
                res[2]-= 1
            else:
                res[0] = self.karte[0][x]
                res[2] = self.ySize-1
        if p == 'w':
            if x > 0:
                res[0] = self.karte[y][x-1]
                res[1]-= 1
            else:
                res[0] = self.karte[y][0]
                res[1] = self.xSize-1
        if p == 'e':
            if x < self.xSize-1:
                res[0] = self.karte[y][x+1]
                res[1]+= 1
            else:
                res[0] = self.karte[y][0]
                res[1] = 0
        else: # wrong input
            res = None
        return res
    def get_random_free_neighbour(self,x,y):
        r = ['n','s','w','e']
        random.shuffel(r)
        for el in r:
            n = self.get_neighbour(x,y,el)
            if n[0] == None:
                return n
            else: #no free neighbour
                return None
    def lifecycle(self):
        pass
    def move(self):
        pass
