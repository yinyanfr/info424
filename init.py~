# Info224 TD3 4 Yin Yan
# Petit modif bidon

# Exo 1
def supprime_espace_aux_extremites(chaine):
    res=""
    i=0
    z=len(chaine)-1
    while chaine[i] == " ": # supprimer des espaces au début
        i = i+1
    while chaine[z] == " ": # supprimer des espaces à la fin
        z = z-1
    res = chaine[i:z+1]
    return res

# Exo 3
def exo3_main():
    t = input("tapez des flottants ")
    return exo3_output(t)

def exo3_output(t):
    element=""
    table=[]
    for i in range(len(t)):
        if t[i] != ";" and t[i] != ",":
            element = element + t[i]
        elif t[i] == ",":
            element = element + "."
        else:
            table = table + [ float(supprime_espace_aux_extremites(element)) ]
            element = ""
    table = table + [ float(supprime_espace_aux_extremites(element)) ]
    return table

def exo3_output2(t):
    
    return

# Palindrome
# Q1
def renverse(c):
    res=""
    for i in range(len(c)-1,-1,-1):
        res = res + c[i]
    return res

# Q2
def est(c):
    t=True
    for i in range(len(c)):
        if c[i]!=c[-i-1]:
            t=False
    return t

from math import *
###1
##def surfacecercle(rayon):
##    return rayon**2*pi
##
##print("Donnez le rayon, pour terminer taper 0")
##r=float(input("rayon ? "))
##while r != 0:
##    print("Le cercle de rayon ",r," a comme surface ",surfacecercle(r))
##    r=float(input("rayon ? "))
    
###2
##def distance(x,y):
##    return sqrt(x**2+y**2)
##    
##print("Pour terminer taper 0")
##a = float(input"x ? "))
##b = float(input"y ? "))
##while a!=0 and b!=0:
##    print("la distence de( ",a ,b," à l'origin est ",distance(a,b))
##    a = float(input"x ? "))
##    b = float(input"y ? "))

#3
def estPremier(nbr):
    t=False
    for i in range(2,int(sqrt(nbr)),1):
        if nbr%i != 0:
            t=True
    return t

n=int(input("Pour terminer taper 0. Entier ? "))
while n!=0:
    print(n," est permier : ",estPremier(n))
    n=int(input("Pour terminer taper 0. Entier ? "))

###4
##def maxTab(tableu):
##    a=tab[0]
##    for i in range(0,len(tab),1):
##        if a<tab[i]:
##            a=tab[i]
##    return a
##
##n = int(input("Combien d'éléments ? "))
##tab=[0]*n
##for i in range(0,len(tab),1):
##    tab[i]=int(input("élémemt "+str(i)+" ? "))
##print("Le maxparmi ",tab," est : ",maxTab(tab))

###5
##def f(x):
##    return 1/(1+x**2)
##
##def integrale(a,b,n,f):
##    s=0
##    for i in range(0,n,1):
##        s=s+((b-a)/n)*(f(a+(b-a)/n*i))
##    return s
##
##a=float(input("Donnez a ? "))
##b=float(input("Donnez b ? "))
##n=int(input("Donnez n ? "))
##print("L'intégrale est : ",integrale(a,b,n,f))



            
