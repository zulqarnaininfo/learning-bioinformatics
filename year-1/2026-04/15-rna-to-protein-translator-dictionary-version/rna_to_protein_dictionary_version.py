# DNA to Protein Translator (Dictionary Version)

rna_seq = str(input("Enter RNA sequence :")).upper()
protein = ""

# Dictionary for Codons
codon_dict = {
"UUU":"Phenylalanine","UUC":"Phenylalanine",
"UUA":"Leucine","UUG":"Leucine","CUU":"Leucine","CUC":"Leucine","CUA":"Leucine","CUG":"Leucine",
"UCU":"Serine","UCC":"Serine","UCA":"Serine","UCG":"Serine","AGU":"Serine","AGC":"Serine",
"UAU":"Tyrosine","UAC":"Tyrosine",
"UGU":"Cysteine","UGC":"Cysteine",
"UGG":"Tryptophan",
"CCU":"Proline","CCC":"Proline","CCA":"Proline","CCG":"Proline",
"CAU":"Histidine","CAC":"Histidine",
"CAA":"Glutamine","CAG":"Glutamine",
"CGU":"Arginine","CGC":"Arginine","CGA":"Arginine","CGG":"Arginine","AGA":"Arginine","AGG":"Arginine",
"AUU":"Isoleucine","AUC":"Isoleucine","AUA":"Isoleucine",
"AUG":"Methionine",
"ACU":"Threonine","ACC":"Threonine","ACA":"Threonine","ACG":"Threonine",
"AAU":"Asparagine","AAC":"Asparagine",
"AAA":"Lysine","AAG":"Lysine",
"GUU":"Valine","GUC":"Valine","GUA":"Valine","GUG":"Valine",
"GCU":"Alanine","GCC":"Alanine","GCA":"Alanine","GCG":"Alanine",
"GAU":"Aspartic acid","GAC":"Aspartic acid",
"GAA":"Glutamic acid","GAG":"Glutamic acid",
"GGU":"Glycine","GGC":"Glycine","GGA":"Glycine","GGG":"Glycine",
}
# conditional syntax
start_codon = False
for i in range(0,len(rna_seq),3):
    codon = rna_seq[i:i+3]
    if len(codon) < 3:
        break
    if codon == "AUG":
        start_codon = True
    if not start_codon:
        continue
    if codon in ["UAA","UAG","UGA"]:
        protein += "STOP"
        break
    amino_acid = codon_dict.get(codon)
    if amino_acid:
        protein += amino_acid + " - "
if protein.endswith(" - "):
    protein = protein[:-3]
print("Protein Sequence is :")
print(protein)
