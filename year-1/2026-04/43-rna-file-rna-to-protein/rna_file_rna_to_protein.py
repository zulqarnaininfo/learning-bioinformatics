# RNA to Protein from a file 

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

def rna_cleaner(rna_sequence):
    clean = ""
    for base in rna_sequence:
        if base in ["A","U","G","C"]:
            clean += base
    return clean
def rna_to_protein(rna_sequence,codon_dictionary=codon_dict):
    protein = ""
    start_codon = False
    for i in range(0,len(rna_sequence),3):
        codon = rna_sequence[i:i+3]
        if len(codon) < 3:
            break
        if codon == "AUG":
            start_codon = True
        if not start_codon:
            continue
        if codon in ["UAA","UAG","UGA"]:
            break
        amino_acid = codon_dictionary.get(codon)
        if amino_acid:
            protein += amino_acid + " - "
    if protein.endswith(" - "):
        protein = protein[:-3]
    return protein
with open("rna.txt","r") as f:
    for line in f:
        line = line.strip().upper()
        clean_rna = rna_cleaner(line)
        protein_seq = rna_to_protein(clean_rna)
        print(f"Original : {line}")
        print(f"Cleaned : {clean_rna}")
        print(f"Protein sequence : {protein_seq}\n")
