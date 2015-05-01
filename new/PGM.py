# -*- coding: utf-8 -*-

__author__ = 'yinyan'

from sys import stdin
from sys import argv


class PGM:

    def __init__(self):
        self.type = 'P2'
        self.width = 600
        self.height = 400
        self.colorRage = 255
        self.backgroundColor = 255
        self.matrix = []
        self.painter = []
        self.get_file()
        self.temp = []
        self.paint()

    def get_file(self):
        if len(argv) > 5:
            self.width = int(argv[2])
            self.height = int(argv[3])
            self.backgroundColor = int(argv[4])
            self.painter = argv[5:]
            self.matrix_generate()
        else:
            self.painter = argv[1:]
            self.read_file()

        return self

    def read_file(self):
        self.matrix = []
        l = stdin.readlines()
        self.type = l[0][:-1]
        width_height = l[1][:-1].split()
        self.width = int(width_height[0])
        self.height = int(width_height[1])
        self.colorRage = int(l[2][:-1])

        l = l[4:]
        for i in l:
            tmp = i.split(' ')[:-1]
            self.matrix.append(tmp)

        return self

    def matrix_generate(self):
        for col in range(self.height):
            templist = []
            for rol in range(self.width):
                templist.append(self.backgroundColor)
            self.matrix.append(templist)
        return self

    def change_pixel(self, rol, col, change):
        self.matrix[rol][col] = change
        self.temp.append((rol, col))

        return self

    def matrix_to_string(self):
        res = ''
        for col in self.matrix:
            for rol in col:
                res += str(rol) + ' '
            res += '\n'
        return res

    def points_in_canvas(self,l): # function in: return list of tuples
        res = []
        for i in l:
            x = i[0]
            y = i[1]
            if (x>=0) and (y>=0) and (x<self.width) and (y<self.height):
                res.append(i)

        return res

    def change_pixels(self,pixels,change):
        for i in pixels:
            self.change_pixel(i[0],i[1],change)

        return self

    def paint(self):
        p = self.painter
        if len(p) == 0:
            return self
        else:
            if p[0] == "square":
                self.square(int(p[1]), int(p[2]), int(p[3]), int(p[4]))
            elif p[0] == "cercle":
                self.cercle(int(p[1]), int(p[2]), int(p[3]))
            elif p[0] == "disque":
                self.disque(int(p[1]), int(p[2]), int(p[3]))
            return self

    def square(self,x=10,y=10,length=100,width=150,color=0):
        """créer une caree , de taille length*width ,commencer par point(x,y),
    initialiser à point (10,10),taille 100*150,couleur=noire"""
        # x,y : les coordonnées left-top

        pixels = []
        for k in range(length):
            for i in range(width):
                pixels.append((x+i,y+k))

        pixels = self.points_in_canvas(pixels)

        self.change_pixels(pixels, color)

        return self

    def disque(self,x = 200, y = 200,r = 50, color = 0):
        """créer un disque , de taille r,commencer par point(x,y),
    initialiser à point (200,200),taille r=50,couleur=noire"""
        pixels = []
        for i in range(x-r,x+r-1):
            for k in range(y-r,y+r-1):
                if (i-x)**2 + (k-y)**2 <= r**2:
                    pixels.append((i,k))

        pixels = self.points_in_canvas(pixels)

        self.change_pixels(pixels,color)

        return self

    def cercle(self,x = 200, y = 200, r = 50, color = 0):
        """créer une cercle, de taille r,commencer par point(x,y),
    initialiser à point (200,200),taille r=50,couleur=noire"""
        pixels = []
        for i in range(x-r,x+r-1):
            for k in range(y-r,y+r-1):
                if ((i-x)**2 + (k-y)**2 <= r**2) and ((i-x)**2 + (k-y)**2 >= (r-2)**2):
                    pixels.append((i,k))

        pixels = self.points_in_canvas(pixels)

        self.change_pixels(pixels, color)

        return self

    def save_file(self):
        print self.type
        print self.width, self.height
        print self.colorRage
        print
        print self.matrix_to_string()

        return self

