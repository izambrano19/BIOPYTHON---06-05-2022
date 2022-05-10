from Bio import Entrez
from Bio import SeqIO
from Bio import Seq
Entrez.email = "izambrano19@ilg.cat"  # Always tell NCBI who you are


with open("practica.txt", "w") as fitxer:
    #  NM_001354619.2
    handle = Entrez.efetch(db="nucleotide", id="NM_001354619.2", rettype="gb", retmode="text")
    #  NM_001324522.1
    handlee = Entrez.efetch(db="nucleotide", id="NM_001324522.1", rettype="gb", retmode="text")
    for rec in SeqIO.parse(handle, "gb"):
        j = 0
        fitxer.write("\n")
        fitxer.write(rec.description)
        fitxer.write("\n")
        #fitxer.write(str(rec.features))
        ##una feature es d'aquesta manera
        ##SeqFeature(FeatureLocation(ExactPosition(0), ExactPosition(1884), strand=1), type='source')
        ##SeqFeature(FeatureLocation(ExactPosition(0), ExactPosition(1884), strand=1), type='gene')
        for i in (rec.features):
            if i.type == 'exon':
                j +=1
                fitxer.write(str("Exo numero " + str(j) + " es:") + "\n")
                fitxer.write(str("  " + str(i.location) + "\n"))
        for i in (rec.features):
            if i.type == 'CDS':
                fitxer.write("\n")
                fitxer.write(str("El CDS te ") + "\n")
                fitxer.write(str("  " + str(i.location) + "\n"))






    for rec in SeqIO.parse(handlee, "gb"):
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
                fitxer.write(str("El CDS te ") + "\n")
                fitxer.write(str("  " + str(i.location) + "\n"))


