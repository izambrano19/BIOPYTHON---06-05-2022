from Bio import Entrez
from Bio import SeqIO
from Bio import Seq
Entrez.email = "izambrano19@ilg.cat"  # Always tell NCBI who you are

#  NM_001382665.1

with open("resultatexemple.txt", "w") as fitxer:
    handle = Entrez.efetch(db="nucleotide", id="NM_001382665.1", rettype="gb", retmode="text")
    for rec in SeqIO.parse(handle, "gb"):
        fitxer.write(rec.id)
        fitxer.write("\n")
        fitxer.write(rec.description)
        fitxer.write("\n")
        #fitxer.write(str(rec.features))
        fitxer.write("\n")
        ##una feature es d'aquesta manera
        ##SeqFeature(FeatureLocation(ExactPosition(0), ExactPosition(1884), strand=1), type='source')
        ##SeqFeature(FeatureLocation(ExactPosition(0), ExactPosition(1884), strand=1), type='gene')
        for i in (rec.features):
            fitxer.write(i.type + "\n")
            fitxer.write(str(i.location) + "\n")
            fitxer.write(str(i.location.strand) + "\n")
            fitxer.write(str(i.qualifiers.keys()) + "\n")
            if i.type == 'exon':
                fitxer.write(str(i.qualifiers['gene']) + "\n")



