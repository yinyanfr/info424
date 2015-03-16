cible: fichier1 fichier2
 "commande de compil"// à changé

all:prog1 prog2
prog1:image.java
java -cp=. image.java

prog2:analise.py
python -m py-compile analyse.py
