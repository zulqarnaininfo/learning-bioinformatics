# RNA to Protein (Translation)

"""
Inside cells, DNA is used to make proteins. There are two main steps:
1. Transcription is the process in which RNA polymerase(an enzyme) copy DNA strand to make mRNA.
2. Translation is the process in which mRNA strand is converted into amino acids(protein) inside ribosome.
"""
"""
Some codon make a certain amino acid
e.g. AUG-Methionine, UUU-Phenylalanine, GGC-Glycine etc
All together make a chain of amino acids(a protein)
Some codon stops this process
e.g. UAA, UAG etc
"""
# Let's say
rna_seq = "AUGUUUGGC"
codons = []
protein = ""
for i in range(0,len(rna_seq),3):
    codon = rna_seq[i:i+3]
    if codon == "AUG":
        protein += "Methionine - "
    elif codon == "UUU":
        protein += "Phenylalanine - "
    elif codon == "GGC":
        protein += "Glycine - "
print("Protien Sequence :")
print(protein)
