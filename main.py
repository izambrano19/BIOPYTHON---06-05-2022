from Bio import Entrez
from Bio import SeqIO
from Bio import Seq
Entrez.email = "izambrano19@ilg.cat"  # Always tell NCBI who you are

#  NM_001382665.1

with open("resultatexemple.txt", "w") as fitxer:
    handle = Entrez.efetch(db="nucleotide", id="NM_001354619.2", rettype="gb", retmode="text")
    handlee = Entrez.efetch(db="nucleotide", id="NM_001324522.1", rettype="gb", retmode="text")
    for rec in SeqIO.parse(handle, "gb"):
        j = 0
        fitxer.write(rec.id)
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
                fitxer.write(i.type)
                fitxer.write(str(" numero " + str(j) + " es:") + "\n")
                fitxer.write(str("  " + str(i.location) + "\n"))



