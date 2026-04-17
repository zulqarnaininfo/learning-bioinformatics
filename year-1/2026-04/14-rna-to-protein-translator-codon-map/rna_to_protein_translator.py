# RNA to Protein Translator(Extended)

rna_seq = str(input()).upper()
protein = ""
for i in range(0,len(rna_seq),3):
    codon = rna_seq[i:i+3]
    if codon in ["UAA","UAG","UGA"]:
        protein += "STOP"
        break
    elif codon in ["UUU","UUC"]:
        protein += "Phenylalanine - "
    elif codon in ["UUA","UUG","CUU","CUC","CUA","CUG"]:
        protein += "Leucine - "
    elif codon in ["UCU","UCC","UCA","UCG","AGU","AGC"]:
        protein += "Serine - "
    elif codon in ["UAU","UAC"]:
        protein += "Tyrosine - "
    elif codon in ["UGU","UGC"]:
        protein += "Cysteine - "
    elif codon in ["UGG"]:
        protein += "Tryptophan - "
    elif codon in ["CCU","CCC","CCA","CCG"]:
        protein += "Proline - "
    elif codon in ["CAU","CAC"]:
        protein += "Histidine - "
    elif codon in ["CAA","CAG"]:
        protein += "Glutamine - "
    elif codon in ["CGU","CGC","CGA","CGG","AGA","AGG"]:
        protein += "Arginine - "
    elif codon in ["AUU","AUC","AUA"]:
        protein += "Isoleucine - "
    elif codon in ["AUG"]:
        protein += "START Methionine - "
    elif codon in ["ACU","ACC","ACA","ACG"]:
        protein += "Threonine - "
    elif codon in ["AAU","AAC"]:
        protein += "Asparagine - "
    elif codon in ["AAA","AAG"]:
        protein += "Lysine - "
    elif codon in ["GUU","GUC","GUA","GUG"]:
        protein += "Valine - "
    elif codon in ["GCU","GCC","GCA","GCG"]:
        protein += "Alanine - "
    elif codon in ["GAU","GAC"]:
        protein += "Aspartic acid - "
    elif codon in ["GAA","GAG"]:
        protein += "Glutamic acid - "
    elif codon in ["GGU","GGC","GGA","GGG"]:
        protein += "Glycine - "
if protein.endswith(" - "):
        protein = protein[:-3]
print("Protein Sequence is :")
print(protein)
