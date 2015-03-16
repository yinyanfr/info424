__author__ = 'Ian'

# This is the class for the ppm format
# At the moment as a prototype of generator which should be written by java
# And will after be used for analysing


class PPM:

    # self

    # Definition
    def __init__(self, create):  # enter a file name or "file name, length, width, background-color"

        self.format = ""
        self.height = 0
        self.width = 0
        self.matrix = [[0 for col in range(self.height)] for row in range(self.width)] # matrix[height][width]

        if create[-3:] == "ppm":
            self.file = open(create,'r+')  # if file name, open the file
        else:
            self.file = open(self.create_file(create))  # else create one as ordered

    # Methods
    def create_file(self, char):  # create file for initialisation
        # TODO


        return self

    def first_deal(self):  # function in out: convert file into a matrix

        # TODO

        return self

    def change_pixel(self,x,y,change):  # function in out: change a pixel in matrix/pic
        self.matrix[x][y] = change

        return self

    def matrix_to_string(self):  # function in : convert the matrix to string
        res = ""
        # TODO
        # Differs from class pgm

        return res

    def save_file(self):  # function in out: save the file
        head = self.format + "\n" + self.height + " " + self.width + "\n"
        middle = self.matrix_to_string(self)
        all = head + "\n" + middle
        self.file.write(all)
        self.file.close()

        return True
