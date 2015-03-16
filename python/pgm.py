__author__ = 'Ian'

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
        self.matrix = [] # matrix[height][width]
        self.filecache = ""
        
        if create[-3:] == "pgm":
            self.get_file(create)  # if file name, open the file
        else:
            self.create_file(create) # else create one as ordered

        print(len(self.matrix),len(self.matrix[0]))

    # Methods
    
    def get_file(self,name):
        f = open(name, "r+")
        #  get content
##        content = ""
##        while True:
##            l = f.readline()
##            if l == "":
##                break
##            content += l
##        f.close()
##        f = open(name,"r+")
##        f.write(content)
            
        self.format = f.readline()[:-1]
        size = f.readline()[:-1] .split(" ")
        self.height = int(size[0])
        self.width = int(size[1])
        self.file = f
        self.file_to_mat();

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
        f.close()
        self.file = open(head[0],"r+")
        

        return self

    def file_to_mat(self):  # function in out: convert file into a matrix
        while True:
            l = self.file.readline()
            self.matrix.append(l[:-1].split(" "))
            if l == "":
                return self
            


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

    def smash_list(self,l):
        res = []
        for i in l:
            for j in i:
                res.append(j)
        return res
                
    def square(self,x=10,y=10,length=100,width=150,color=0):
        # x,y : les coordonnées left-top
        pixels = []
        line = []
        for k in range(length):
            for i in range(width):
                line.append((x+i,y+k))
            pixels.append(line)
            line = []

        pixels = self.points_in_canvas(self.smash_list(pixels))

        self.change_pixels(pixels,color)

        return self
    

    def save_file(self):  # function in out: save the file
        head = self.format + "\n" + str(self.height) + " " + str(self.width) + "\n"
        middle = self.matrix_to_string()
        whole = head + "\n" + middle
        self.file.write(whole)
        self.file.close()

        return True