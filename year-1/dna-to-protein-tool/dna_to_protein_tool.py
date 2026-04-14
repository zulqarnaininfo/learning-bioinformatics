# DNA to Protein Tool

dna_input = str(input("Enter DNA sequence :")).upper()
dna_seq = ""
for base in dna_input:
    if base in ["A","T","G","C"]:
        dna_seq += base
rna_seq = dna_seq.replace("T","U")

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

while True:
    option = int(input("--Select an option--\n1.Clean DNA sequence\n2.Transcription(DNA to RNA)\n3.Translation(RNA to Protein)\n4.Exit\nEnter Your choice :"))
    if option == 1:
        print(f"Clean DNA : {dna_seq}")
    elif option == 2:
        print(f"RNA sequence is : {rna_seq}")
    elif option == 3:
        protein = ""
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
        print(f"Protein sequence is :\n{protein}")
    elif option == 4:
        print("Bye Bye")
        break
    else:
        print("Please select valid option.")
