# Info224 TD3 4 Yin Yan

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
    t = input("tapez des flottants wtf ")
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


