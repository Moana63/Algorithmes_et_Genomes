import json

#Transcrit l'ADN en ARN

def transcription (DNA):
	ARN=(DNA.replace("T","U"))
	return ARN

#Ouvre le dictionnaire de transcription codon-AA et retourne la clé (l'AA correspondant au codon)
#Creer une fonction qui remplace les codons par un AA

def traduction (DNA,phase):
	with open("dico_traduction.json") as f:
		data = json.load(f)
	ARN = transcription(DNA)

	protein = ""
	begin = phase-1
	lenght = len(ARN)
	while begin <= lenght-3:

		codon=ARN[begin:begin+3]
		AA = data[codon]
		protein+=AA
		begin+=3
	print("Proteine correpondante pour la phase", phase, ":", protein)
	return protein

DNA = "TATATAAGCAATGTAGGGACGCCAGCAAACCTAGC"

print("ADN :",DNA)
traduction(DNA,1)
traduction(DNA,2)
traduction(DNA,3)