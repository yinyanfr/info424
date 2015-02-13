__author__ = 'Ian'

# This is the class for the pgm format
# At the moment as a prototype of generator which should be written by java
# And will after be used for analysing


class PGM:

    # Constant gray pgm
    WHITE = 0
    BLACK = 255
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
            get_file(create)  # if file name, open the file
        else:
            create_file(create) # else create one as ordered

    # Methods
    def get_file(self,name):
        f = open(name, "r")
        self.format = f.readline()[:-1]
        size = f.readline()[:-1].split(" ")
        self.height = size[0]
        self.width = size[1]
        self.file = f

        return self
        
    
    def create_file(self, char):  # create file for initialisation
        head = char.split(",")  # ["filename.pgm", "height", "width", COLOR]
        f = open(head[0], "w");
        whole = "P2\n" + head[1] + " " + head[2] + "\n"
        self.format = "P2"
        self.height = head[1]
        self.width = head[2]
        if not head[3]:
            head[3] = WHITE
        self.matrix = [[head[3] for col in range(self.height)] for row in range(self.width)]
        # matrix[height][width]
        whole += matrix_to_string()
        f.write(whole)
        f.close()
        self.file = open(head[0],"r")
        

        return self

    def file_to_mat(self):  # function in out: convert file into a matrix
        while True:
            l = self.file.readline()
            self.matrix.append(l[:-1].split(" "))
            if l = "":
                return self
            


    def change_pixel(self,x,y,change):  # function in out: change a pixel in matrix/pic
        self.matrix[x][y] = change

        return self

    def matrix_to_string(self):  # function in : convert the matrix to string
        res = ""
        for col in self.matrix:
            for row in col:
                res += row + " "
            res += "\n"

        return res

    def save_file(self):  # function in out: save the file
        head = self.format + "\n" + self.height + " " + self.width + "\n"
        middle = self.matrix_to_string(self)
        whole = head + "\n" + middle
        self.file.write(whole)
        self.file.close()

        return True
