##Version 1, fontion qui remplace les T de la sequence d'ADN par des U

Seq="ATCGTAGCTGACCAGTTAGAC"

def transcription(dna):
    return(dna.replace("T","U"))

print ("ADN :",Seq)
print("ARN :", transcription(Seq))



##Verion 2
def translate_dna_to_rna(dna):
    """"
    Traduit un brin d'ADN en ARN en remplaçant toutes
    les occurrences de T en U
    """
    rna = ""
    for nucleo in dna:
        # traduire une Thymine en Uracile
        if nucleo == 'T':
            rna += "U"
        else:
            rna += nucleo
    return rna