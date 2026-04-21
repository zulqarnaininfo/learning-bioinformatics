# Different Protein sequences

rna_input = input("Enter RNA sequence :").upper()

# Dictionaries
codon_dict1 = {
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
codon_dict2 = {
"UUU":"Phe","UUC":"Phe",
"UUA":"Leu","UUG":"Leu","CUU":"Leu","CUC":"Leu","CUA":"Leu","CUG":"Leu",
"UCU":"Ser","UCC":"Ser","UCA":"Ser","UCG":"Ser","AGU":"Ser","AGC":"Ser",
"UAU":"Tyr","UAC":"Tyr",
"UGU":"Cys","UGC":"Cys",
"UGG":"Trp",
"CCU":"Pro","CCC":"Pro","CCA":"Pro","CCG":"Pro",
"CAU":"His","CAC":"His",
"CAA":"Gln","CAG":"Gln",
"CGU":"Arg","CGC":"Arg","CGA":"Arg","CGG":"Arg","AGA":"Arg","AGG":"Arg",
"AUU":"Ile","AUC":"Ile","AUA":"Ile",
"AUG":"Met",
"ACU":"Thr","ACC":"Thr","ACA":"Thr","ACG":"Thr",
"AAU":"Asn","AAC":"Asn",
"AAA":"Lys","AAG":"Lys",
"GUU":"Val","GUC":"Val","GUA":"Val","GUG":"Val",
"GCU":"Ala","GCC":"Ala","GCA":"Ala","GCG":"Ala",
"GAU":"Asp","GAC":"Asp",
"GAA":"Glu","GAG":"Glu",
"GGU":"Gly","GGC":"Gly","GGA":"Gly","GGG":"Gly",
}
codon_dict3 = {
"UUU":"F","UUC":"F",
"UUA":"L","UUG":"L","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
"UCU":"S","UCC":"S","UCA":"S","UCG":"S","AGU":"S","AGC":"S",
"UAU":"Y","UAC":"Y",
"UGU":"C","UGC":"C",
"UGG":"W",
"CCU":"P","CCC":"P","CCA":"P","CCG":"P",
"CAU":"H","CAC":"H",
"CAA":"Q","CAG":"Q",
"CGU":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R",
"AUU":"I","AUC":"I","AUA":"I",
"AUG":"M",
"ACU":"T","ACC":"T","ACA":"T","ACG":"T",
"AAU":"N","AAC":"N",
"AAA":"K","AAG":"K",
"GUU":"V","GUC":"V","GUA":"V","GUG":"V",
"GCU":"A","GCC":"A","GCA":"A","GCG":"A",
"GAU":"D","GAC":"D",
"GAA":"E","GAG":"E",
"GGU":"G","GGC":"G","GGA":"G","GGG":"G",
}
separator1 = " - "
separator2 = "-"
separator3 = ""

# functions
def rna_cleaner(rna_sequence):
    clean = ""
    for base in rna_sequence:
        if base in ["A","U","G","C"]:
            clean += base
    return clean
def rna_to_protein(rna_sequence,codon_dictionary,separator):
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
            protein += amino_acid + separator
    if protein.endswith(" - "):
        protein = protein[:-3]
    if protein.endswith("-"):
        protein = protein[:-1]
    return protein

valid_rna = rna_cleaner(rna_input)
full_protein = rna_to_protein(valid_rna,codon_dict1,separator1)
l3protein = rna_to_protein(valid_rna,codon_dict2,separator2)
l1protein = rna_to_protein(valid_rna,codon_dict3,separator3)

while True:
    print("---Protein Sequence---")
    print("1. Full name of amino acids")
    print("2. 3-letter symbol of amino acids")
    print("3. 1-letter symbol of amino acids")
    print("4. Exit")
    choice = int(input("Select an option : "))
    if choice == 1:
        print("Full name of amino acids")
        print(f"Protein sequence :  {full_protein}")
    elif choice == 2:
        print("3-letter symbol of amino acids")
        print(f"Protein sequence :  {l3protein}")
    elif choice == 3:
        print("3. 1-letter symbol of amino acids")
        print(f"Protein sequence :  {l1protein}")
    elif choice == 4:
        print("Bye Bye")
        break
    else:
        print("Invalid option! Select again")
