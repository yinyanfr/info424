# Tuto en manipulation de matrice en python3

##intro
En Python on traite des matrices comme des n-uplets ou des n-dimentsion listes

chaque élement est un liste de liste de nombre

et chaque liste représente une ligne de la matrice

## créer un matrice
on initialise une matrice de taille 'row'*'col' en façon suivant:

```
self.matrix = [[head[3] for col in range(int(self.height))] for row in range(int(self.width))]
```
remarque :on peut modifier la matrice après l'initialiser dans Python, cependant en Java la matrice est une class,on ne peut plus la modifier après l'initialiser.

## manipuler un matrice
chaque élément dans la matrice est de format  matrix [x][y],x est le nombre de ligne et y est de nombre de colone
par ex ```print (matrix[x][y])```nous donne l'élément de x ligne y colone de la matrice 'matrix'.

on peut donner la valeur des l'élément de la matrice par ```matrix[x][y]= VALEUR```

```
def change_pixel(self,x,y,change):  # function in out: change a pixel in matrix/pic
        self.matrix[x][y] = change

        return self
```


###
on utilise boucles pour affiche tous les éléments de la matrice
```
    def matrix_to_string(self):  # function in : convert the matrix to string
        res = ""
        for col in self.matrix:
            for row in col:
                res += row + " "
            res += "\n"

        return res
```
