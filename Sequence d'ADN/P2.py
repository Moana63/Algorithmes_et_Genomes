#PARTIE 2
#calcule des proportion de chaque nucleotides dans la chaine d'adn

#COMPTE LES NUCLEOTIDES DE LA CHAINE ET LA LONGUEUR DE LA CHAINE (ET LES ERREURS)
def count_nucleotides(Sequence):
	nbA = nbT = nbC = nbG = nbTotal = nberror =0  # /!\ il faut déclarer les variables utilisées dans la fonction A L'INTERIEUR de la fonction
	for lettre in Sequence:
		if lettre == 'A':
			nbA = nbA + 1    #on peut aussi écrire nbA += 1
		elif lettre == 'T':
			nbT = nbT + 1
		elif lettre == "G":
			nbG = nbG + 1
		elif lettre == "C":
			nbC = nbC + 1
		else:
			nberror = nberror + 1
		nbTotal = nbTotal + 1

	return ( nbA, nbT, nbC, nbG, nbTotal, nberror )

#CALCULE ET IMPRIME LES PROPORTIONS DES NUCLEOTIDES ET LA LONGUEUR DE LA CHAINE (ET LES ERREURS)
def proportions(counts):
	nbA, nbT, nbC, nbG, nbTotal, nberror = counts # /!\ il faut déclarer les variables utilisées dans la fonction A L'INTERIEUR de la fonction. Count renvoi aux resultats de la fonction précédente.
	
	print('Total de la sequence=', nbTotal)
	print("Proportion in DNA:")
	print("%A=",100*nbA/nbTotal)  # on peut arrondir le résultat a 2 chiffres apres la virgule avec l'instruction print("A = {:.2%}".format(nbA / nbTotal))
	print("%T=", 100*nbT/nbTotal)
	print("%G=", 100*nbG/nbTotal)
	print("%C=", 100*nbC/nbTotal)
	print("CG = {:.2%}".format((nbC + nbG) / nbTotal))  #calcule la proportion de A et de T dans la sequence d'ADN; arrondi a 2 chiffres apres la virgule
	print("TA = {:.2%}".format((nbT + nbA) / nbTotal))  #calcule la proportion de C et de G dans la sequence d'ADN; arrondi a 2 chiffres apres la virgule
	print("error=", nberror)

dna = "TATCCTGACTGGACccGACAAaCGACGCAAT"
dna2="TATCATGCTCGACTAGTGACGGGACCCCAACGACGAATGGGGCCGCGTGGACAAT"

print("DNA 1 : ", dna)
proportions(count_nucleotides (dna))
print()
print("DNA 2 :", dna2)
proportions(count_nucleotides (dna2))