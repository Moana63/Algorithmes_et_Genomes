#PARTIE 3, PROMENADE LE LONG DE L'ADN
#pour dessiner un fragment d'ADN dans un graphique on attribut a chacune des lettre un déplacement (haut, droite, gauche, bas)
#Le problème revient à calculer les coordonnées des points du chemin, sous la forme d'une liste d'abscisses 
#et une liste d'ordonnées et de les representer dans un graphique.
#Pour simplifier on ajoute au graphique les coordonnées d'une partie des lettres de la séquence seulemet (cf "multiple")

import matplotlib.pyplot as pyplot
import pylab
pylab.rcParams['figure.figsize'] = 8., 8.

#creation du dictionnaire avec les déplacements correspondants a chaque lettre
moves = {
	"A": [0,1],
	"T": [0,-1],
	"G": [-1,0],
	"C": [1,0]
}

#écrire une fonction qui prend en entrée un fragment d'ADN codé comme une chaine de caractères  (sequence) contenant les 4 abbréviations,
#et qui retourne deux listes list_x et list_y, correspondant respectivement aux coordonées x et y des points du chemin.

def coordonees_chemin (Sequence, multiple):
	list_x,list_y=[],[]
	x, y = 0, 0          #on démarre a 0 sur le graphique, point d'origine
	list_x.append (x)    #on ajoute les coordonées x et y du point de départ a la liste
	list_y.append(y)

	for position, lettre in enumerate(Sequence):   #enumerate permet de traiter l'index (position) et la premiere sous unité de la chaine de caratere (lettre) en une seule opération
		delta_x, delta_y= moves[lettre]  #on assigne les coordonnées a chaque lettre de la sequence a l'aide des correspondances stockées dans le dictionnaire
		x += delta_x                     # les valeurs de x et y sont modifiées apres chaque lecture de lettre
		y += delta_y
		if position % multiple ==0:          #on realise l'operation precedente pour chaque lettre dont la position est un multiple de la valeur "multiple" que l'on renseigne lors de l'utilisation de la fonction
			list_x.append (x)                #on ajoute aux listes list_x et list_y les nouvelles coordonées de x et y apres chaque lecture de lettre,
			list_y.append(y)                 # dont la position est un multiple de "multiple" ( ne s'applique pas a toutes les lettres)
	return list_x,list_y

# On trace les resultats des listes x et y dans un graphique
def chemin(Sequence, multiple):
	print("longueur de la séquence d'entrée", len(Sequence), "step:",multiple)
	X,Y=coordonees_chemin(Sequence, multiple)   #les listes list_x et list_y sont respectivement stockees dans les variables X et Y
	pyplot.plot(X,Y)       #On cree un graphique qui trace des lignes entre chaque coordonées définies par les listes X et Y
	pyplot.show()


#cree une sequence aleatorie d'adn de "lenght" bases
import random
 
def random_seq (length):

	a = ["A" , 'T', 'C', 'G']
	seq_adn2 = ""  
	for i in range(length):           #boucle for qui repete 50 fois l'operation
		result = random.choice(a)
		seq_adn2 += result        #stock la chaine dans une variable seq_adn2
	return seq_adn2

#On utilise la fonction pour tracer un graphique d'une séquence d'ADN de 10000 bases,
chemin(random_seq(10000),5)