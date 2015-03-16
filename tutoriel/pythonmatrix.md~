# Tuto en manipulation de matrice en python3

## créer un matrice

```
self.matrix = [[head[3] for col in range(int(self.height))] for row in range(int(self.width))]
```

```
    def file_to_mat(self):  # function in out: convert file into a matrix
        while True:
            l = self.file.readline()
            self.matrix.append(l[:-1].split(" "))
            if l == "":
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
```
