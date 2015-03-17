__author__ = 'Shabi'

# This is the class for the pgm format
# At the moment as a prototype of generator which should be written by java
# And will after be used for analysing


class PGM:

    # Constant gray pgm
    WHITE = 255
    BLACK = 0
    GRAY = 166

    # self

    # Definition
    def __init__(self, create):  # enter a file name or "file name,height,width,background-color"

        self.format = ""
        self.height = 0
        self.width = 0
        self.graystage = 255
        self.matrix = [] # matrix[height][width]
        self.filecache = ""
        
        if create[-3:] == "pgm":
            self.get_file(create)  # if file name, open the file
        else:
            self.create_file(create) # else create one as ordered

        print(len(self.matrix[0]),len(self.matrix))
        self.backup()

    # Methods
    
    def get_file(self,name):
        """get infomation from the file """
        f = open(name, "r+")
        #  get content
        self.format = f.readline()[:-1]
        size = f.readline()[:-1] .split(" ")
        self.height = int(size[0])
        self.width = int(size[1])
        self.graystage = int(f.readline()[:-1])
        self.file = f
        self.file_to_mat();
        f.close()
        self.file = open(name,"r+")
        print(self.format,self.height,self.width,self.graystage)

        return self

    def saute_espace(self,char):
        res = ""
        for i in char:
            if i != " ":
                res += i
        return res
        
    
    def create_file(self, char):  # create file for initialisation
        # Constant gray pgm
        WHITE = 255
        BLACK = 0
        GRAY = 166
        head = self.saute_espace(char).split(",")  # ["filename.pgm", "height", "width", COLOR]
        #assert (head[0][-3:] != "pgm"), "File Extend Name Error"
        f = open(head[0], "w");
        whole = "P2\n" + head[1] + " " + head[2] + "\n"
        self.format = "P2"
        self.height = int(head[1])
        self.width = int(head[2])
        if len(head) == 3:
            head.append(WHITE)
        self.matrix = [[head[3] for col in range(int(self.height))] for row in range(int(self.width))]
        # matrix[height][width]
        whole += self.matrix_to_string()
        f.write(whole)
        self.file = open(head[0],"r+")

        return self

    def file_to_mat(self):  # function in out: convert file into a matrix
        l = self.file.readline()
        while True:
            l = self.file.readline()
            if l == "":
                return self
            tmp = l[:-1].split(" ")[:-1]
            self.matrix.append(tmp)
            
            


    def change_pixel(self,x,y,change):  # function in out: change a pixel in matrix/pic
        #print(x,y)
        self.matrix[x][y] = change

        return self

    def change_pixels(self,pixels,change):
        for i in pixels:
            self.change_pixel(i[0],i[1],change)

        return self

    def matrix_to_string(self):  # function in : convert the matrix to string
        res = ""
        for col in self.matrix:
            for row in col:
                res += str(row) + " "
            res += "\n"

        return res

    def points_in_canvas(self,l): # function in: return list of tuples
        res = []
        for i in l:
            x = i[0]
            y = i[1]
            if (x>=0) and (y>=0) and (x<self.width) and (y<self.height):
                res.append(i)

        return res

##    def smash_list(self,l):
##        res = []
##        for i in l:
##            for j in i:
##                res.append(j)
##        return res
                
    def square(self,x=10,y=10,length=100,width=150,color=0):
        """créer une carée , de taille length*width ,commencer par point(x,y),
    initialiser à point (10,10),taille 100*150,couleur=noire"""
        # x,y : les coordonnées left-top
        pixels = []
        for k in range(length):
            for i in range(width):
                pixels.append((x+i,y+k))

        pixels = self.points_in_canvas(pixels)

        self.change_pixels(pixels,color)

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

        self.change_pixels(pixels,color)

        return self

    def ligne(self,points,color = 0):
                 """créer une ligne , commencer et terminer par les valeur dans la liste points,
    couleur initialiser à noire"""
        pixels = []
        point1 = points[0]
        point2 = points[1]
        x1, y1 = point1[0], point1[1]
        x2, y2 = point2[0], point2[1]

        tmp = [x1,y1]
        gap = max(x2-x1,y2-y1)
        for i in range(gap):
                tmp[0] +=  gap//(x2-x1)
                tmp[1] += gap//(y2-y1)
                pixels.append((tmp[0],tmp[1]))

        pixels = self.points_in_canvas(pixels)

        self.change_pixels(pixels,color)

        return self
    

    def polygon(self, points, color = 0):
                 """créer une polygone qui parcourir tous les points de la liste points,couleur initialiser à noire"""
        for i in range(1,len(points)):
            self.ligne([points[i-1],points[i]])
            
        self.ligne([points[len(points)-1],points[0]])

        return self
    
    def backup(self):  # function in out: save the file
        head = self.format + "\n" + str(self.height) + " " + str(self.width) + "\n"+str(self.graystage) + "\n"
        middle = self.matrix_to_string()
        whole = head + "\n" + middle
        f = open("backup.pgm","w")
        f.write(whole)
        f.close()

        return self

    def preview(self):  # function in out: save the file
        head = self.format + "\n" + str(self.height) + " " + str(self.width) + "\n"+str(self.graystage) + "\n"
        middle = self.matrix_to_string()
        whole = head + "\n" + middle
        f = open("preview.pgm","w")
        f.write(whole)
        f.close()

        return self

    def save_file(self):  # function in out: save the file
        head = self.format + "\n" + str(self.height) + " " + str(self.width) + "\n"+str(self.graystage) + "\n"
        middle = self.matrix_to_string()
        whole = head + "\n" + middle
        self.file.write(whole)
        self.file.close()

        return True
