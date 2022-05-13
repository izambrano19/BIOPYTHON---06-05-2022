from Bio import Entrez
from Bio import SeqIO
import dnachisel
from dnachisel.biotools import reverse_translate
from Bio import Seq

Entrez.email = "izambrano19@ilg.cat"  # Always tell NCBI who you are


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
                fitxer.write("\n")
                e = str(i.qualifiers['translation']).strip("[']")
                fitxer.write(str("El CDS te: ") + str(len(e) * 3) + "\n")
                fitxer.write(str(i.location) + "\n")
                dna = reverse_translate(str(e))
                fitxer.write(dna + "\n")
                e = e[0:50]
                fitxer.write(e + "\n")
