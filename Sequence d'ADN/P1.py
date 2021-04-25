#PARTIE 1
#remplace toutes les lettres A, T,  G, C d'une sequence d'ADN par leur nom complet dans une liste appelée "chaine"
def liste(Sequence):
	chaine = []
	for lettre in Sequence:
		if lettre == 'A':
			chaine.append ("Adenine")
		elif lettre == 'T':
			chaine.append("Thymine")
		elif lettre == "G":
			chaine.append("Guanine")
		elif lettre == "C":
			chaine.append ("Cytosine")
		else:
			print("lettre non reconnue",lettre)
	print('Sequence:',chaine)

SeqA = "ACTGAATFG"
print("ADN : ", SeqA)
liste(SeqA)