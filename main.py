from Bio import Entrez
from Bio import SeqIO
import dnachisel
from dnachisel.biotools import reverse_translate
from Bio import Seq

Entrez.email = "izambrano19@ilg.cat"  # Always tell NCBI who you are

c1 = 0
c2 = 0

def alinea(cadena1, cadena2):
    valor = 0
    for i in range(len(cadena1)):
        if cadena1[i] == cadena2[i]:
            valor += 1
    return valor

with open("practica.txt", "w") as fitxer:
    #  NM_001354619.2     NM_001324522.1
    handle = Entrez.efetch(db="nucleotide", id="NM_001354619.2 , NM_001324522.1", rettype="gb", retmode="text")

    for rec in SeqIO.parse(handle, "gb"):
        j = 0
        fitxer.write("\n")
        fitxer.write(rec.description)
        fitxer.write("\n")

        for i in (rec.features):
            if i.type == 'exon':
                j +=1
                fitxer.write(str("Exo numero " + str(j) + " es:") + "\n")
                fitxer.write(str("  " + str(i.location) + "\n"))

        for i in (rec.features):
            if i.type == 'CDS':
                if c1 == 0:
                    d1 = rec.description
                    fitxer.write("\n")
                    c1 = str(i.qualifiers['translation']).strip("[']")
                    fitxer.write(str("El CDS te: ") + str(len(c1) * 3) + "\n")
                    fitxer.write(str(i.location) + "\n")
                    dna = reverse_translate(str(c1))
                    fitxer.write(dna + "\n")
                    c1 = c1[0:50]
                    fitxer.write(c1 + "\n")

                else:
                    d2 = rec.description
                    fitxer.write("\n")
                    c2 = str(i.qualifiers['translation']).strip("[']")
                    fitxer.write(str("El CDS te: ") + str(len(c2) * 3) + "\n")
                    fitxer.write(str(i.location) + "\n")
                    dna = reverse_translate(str(c2))
                    fitxer.write(dna + "\n")
                    c2 = c2[0:50]
                    fitxer.write(c2 + "\n")
                    fitxer.write("\n")
    fitxer.write("La igualtat entre " + d1 + " i " + d2 + " es " + str(alinea(c1,c2)) + " sobre 50")

