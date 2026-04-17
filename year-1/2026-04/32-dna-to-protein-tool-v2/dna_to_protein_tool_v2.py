# DNA to Protein Tool v2

dna_input = input("Enter DNA sequence :").upper()

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

# Functions
def dna_cleaner(dna_sequence):
    clean = ""
    for base in dna_sequence:
        if base in ["A","T","G","C"]:
            clean += base
    return clean
def transcription(dna_sequence):
    rna_sequence = dna_sequence.replace("T","U")
    return rna_sequence
def translation(rna_sequence,codon_dictionary=codon_dict):
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
            protein += "STOP"
            break
        amino_acid = codon_dictionary.get(codon)
        if amino_acid:
            protein += amino_acid + " - "
    if protein.endswith(" - "):
        protein = protein[:-3]
    return protein

# Menu
dna_seq = dna_cleaner(dna_input)
rna_seq = transcription(dna_seq)
protein_seq = translation(rna_seq)
while True:
    option = int(input("--Select an option--\n1.Clean DNA sequence\n2.Transcription(DNA to RNA)\n3.Translation(RNA to Protein)\n4.Exit\nEnter Your choice :"))
    if option == 1:
        print(f"Clean DNA : {dna_seq}")
    elif option == 2:
        print(f"RNA sequence is : {rna_seq}")
    elif option == 3:
        print(f"Protein sequence is :\n{protein_seq}")
    elif option == 4:
        print("Bye Bye")
        break
    else:
        print("Please select valid option.")
