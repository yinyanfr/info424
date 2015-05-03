# -*- coding: utf-8 -*-

__author__ = 'yinyan'

from sys import stdin
from sys import argv


class PPM:

    def __init__(self):
        self.type = 'P3'
        self.width = 600
        self.height = 400
        self.colorRage = 255
        self.backgroundColor = [255, 255, 255]
        self.matrix = []
        self.painter = []
        self.get_file()
        self.temp = []
        self.paint()

    def string_to_color(self, s):
        if s == "white":
            return [255, 255, 255]
        elif s == "red":
            return [255, 0, 0]
        elif s == "green":
            return [0, 255, 0]
        elif s == "blue":
            return [0, 0, 255]
        else:
            return [0, 0, 0]

    def get_file(self):
        if len(argv) > 5:
            self.width = int(argv[2])
            self.height = int(argv[3])
            self.backgroundColor = self.string_to_color(argv[4])
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
            tmpline = i.split(' ')[:-1]
            tmp = []
            for j in range(0,len(tmpline),3):
                tmp.append([tmpline[j],tmpline[j+1],tmpline[j+2]])
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

        def list_to_string(l):
            s = ""
            for i in l:
                s += str(i) + " "
            return s

        res = ''
        for col in self.matrix:
            for rol in col:
                res += list_to_string(rol) + ' '
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
                self.square(int(p[1]), int(p[2]), int(p[3]), int(p[4]), self.string_to_color(p[5]))
            elif p[0] == "cercle":
                self.cercle(int(p[1]), int(p[2]), int(p[3]), self.string_to_color(p[4]))
            elif p[0] == "disque":
                self.disque(int(p[1]), int(p[2]), int(p[3]), self.string_to_color(p[4]))
            elif p[0] == "triangle":
                self.triangle([[int(p[1]), int(p[2])], [int(p[3]), int(p[4])], [int(p[5]), int(p[6])]])
            return self

    def square(self,x=10,y=10,length=100,width=150, color = [0, 0, 0]):
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

    def disque(self,x = 200, y = 200,r = 50, color = [0, 0, 0]):
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

    def cercle(self,x = 200, y = 200, r = 50, color = [0, 0, 0]):
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
    def triangle(self,ligne =[[100,300],[300,300]],point=[200,200], color = [0, 0, 0]):
        pixels = []
        bian1=[]
        bian2=[]
        point1 = ligne[0]
        point2 = ligne[1]
        x1,y1 = point1[0],point1[1]
        x2,y2 = point2[0],point2[1]
        x0,y0 = point[0],point[1]
        for i in range(0,self.width):
            for j in range(1,self.height):
                if y0 < y1 :
                    if j==((y1-y0)//(x1-x0))*i+y0-((y1-y0)//(x1-x0))*x0 and y0<= j<=y1:
                        bian1.append((i,j))
                    if j==((y2-y0)//(x2-x0))*i+y0-((y2-y0)//(x2-x0))*x0 and y0<= j<=y2:
                        bian2.append((i,j))
                else :
                    if j==((y1-y0)//(x1-x0))*i+y0-((y1-y0)//(x1-x0))*x0 and y1<= j<=y0:
                        bian1.append((i,j))
                    if j==((y2-y0)//(x2-x0))*i+y0-((y2-y0)//(x2-x0))*x0 and y2<= j<=y0:
                        bian2.append((i,j))
        bian2.reverse()
        for v in range(1,len(bian1)):
            ##print (bian1[v][1])
            if int(bian1[v][1])-int(bian1[v-1][1]) != 1:
                for u in range(bian1[v][1]-bian1[v-1][1]):
                    bian1.append((v,bian1[v][1]+u))
                    bian2.append((v,bian1[v][1]+u))

        for k in range(len(bian1)):
            for h in range(bian1[k][0],bian2[k][0]):
                pixels.append([bian1[k][1],h])


        pixels = self.points_in_canvas(pixels)

        self.change_pixels(pixels, color)
        self.change_pixel(x0,y0,color)

        ##print(bian1)
        ##print(bian2)

        return self

    def save_file(self):
        print self.type
        print self.width, self.height
        print self.colorRage
        print
        print self.matrix_to_string()

        return self

    def equal_list(self,l1,l2):
        if len(l1) != len(l2):
            return False
        else:
            for i in range(len(l1)):
                if l1[i] != l2[i]:
                    return False
            return True

    def get_content(self):  # function in : return pixels
        # function primary
        pixels = []
        pixel = []
        ordonnee = []
        ordonnees = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if not self.equal_list(self.matrix[i][j], self.backgroundColor):
                    #print self.backgroundColor, self.matrix[i][j], int(self.matrix[i][j]) == self.backgroundColor
                    pixel.append(self.matrix[i][j])
                    ordonnee.append((i,j))

            if len(pixel) != 0:
                pixels.append(pixel)
                ordonnees.append(ordonnee)
            pixel = []
            ordonnee = []
        #print pixels
        #print ordonnees
        return pixels, ordonnees

    def analyse(self):
        pixels = self.get_content()[0]
        ordonnees = self.get_content()[1]

        ## square done

        def equal(pixels):
            l = len(pixels[0])
            for i in pixels:
                if len(i) != l:
                    return False
            return True

        def equalhead(pixels):
            l = pixels[0][0]
            for i in pixels:
                if not self.equal_list(i[1], l):
                    return False
            return True

        def square_exam(pixels):  # done
            return len(pixels) == len(pixels[0])

        def square_verifie(square):
            if square:
                print "C'est un carré"  # done
                print "de coordonneés left-top : ", ordonnees[0][0]
                print "et width : ", len(pixels)
            else:
                print("C'est un carré longue")
                print("de coordonneés left-top : ", ordonnees[0][0])
                print("et height : ",len(pixels[0]))
                print("et width : ",len(pixels))
            print("de couleur : ",pixels[0][0])

        ## disque done
        def disque_exam(pixels):
            length = len(pixels)
            top = len(pixels[0])
            midtop = len(pixels[int(0.25*length) - 1])
            mid = len(pixels[int(0.5*length) - 1])
            midbottom = len(pixels[int(0.75*length) - 1])
            bottom = len(pixels[length - 1])

            return (top < midtop) and (midtop < mid) and (mid > midbottom) and (midbottom > bottom)

        def disque_verifie():
            heart = 0.5*len(ordonnees)
            print("C'est un disque")
            print("de centre : ", ordonnees[int(heart)][int(heart)])
            print("de rayon : ", heart)
            print("de couleur : ",pixels[0][0])

        def triangle_exam(pixels):
            length = len(pixels)
            top = len(pixels[0])
            midtop = len(pixels[int(0.25*length) - 1])
            mid = len(pixels[int(0.5*length) - 1])
            midbottom = len(pixels[int(0.75*length) - 1])
            bottom = len(pixels[length - 1])

            return (top < midtop) and (midtop < mid) or (mid > midbottom) and (midbottom > bottom)

        ## Main analyse
        if equal(pixels) and equalhead(pixels):
            if square_exam(pixels):
                square_verifie(True)
            else:
                square_verifie(False)
        elif disque_exam(pixels):
            disque_verifie()
        else:
            print("Je ne sais pas")