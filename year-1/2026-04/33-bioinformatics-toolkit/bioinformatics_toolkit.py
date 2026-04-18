# # Bioinformatics Toolkit (CLI Tool)

print("Welcome! This is a Bioinformatics tool, do you wish to continue?")
proceed = input("Y/N :").upper()

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
def dna_validator(dna_input,cleaned_dna):
    if dna_input == cleaned_dna:
        print("This DNA sequence is valid")
        return 0
    else:
        invalid_count = 0
        for base in dna_input:
            if base not in ["A","T","G","C"]:
                invalid_count += 1
        print(f"DNA is invalid. Invalid characters removed :{invalid_count}")
        return invalid_count
def dna_nucleotide_count(dna_sequence):
    countA = dna_sequence.count("A")
    countT = dna_sequence.count("T")
    countG = dna_sequence.count("G")
    countC = dna_sequence.count("C")
    return {"A":countA,"T":countT,"G":countG,"C":countC}
def gc_content_calc(dna_sequence):
    if len(dna_sequence) == 0:
        return 0
    countG = dna_sequence.count("G")
    countC = dna_sequence.count("C")
    gc_count = countG + countC
    gc_percent = ((gc_count/len(dna_sequence))*100).__round__(2)
    return gc_percent
def dna_pattern_find(dna_sequence,pattern):
    positions = []
    pattern_length = len(pattern)
    for i in range(len(dna_sequence)-pattern_length+1):
        if dna_sequence[i:i+pattern_length] == pattern:
            positions.append(i)
    return positions
def dna_mutation_detect(dna_seq1,dna_seq2):
    if len(dna_seq1) != len(dna_seq2):
        return "DNA sequences are not the same length!"
    mutations = []
    for i in range(len(dna_seq1)):
        if dna_seq1[i] != dna_seq2[i]:
            mutations.append(f"Position {i}: {dna_seq1[i]} -> {dna_seq2[i]}")
    if not mutations:
        return ["No mutation detected."]
    return mutations
def dna_to_rna(dna_sequence):
    rna = dna_sequence.replace("T","U")
    return rna
def dna_complement(dna_sequence):
    complement = ""
    for base in dna_sequence:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
    return complement
def dna_reverse_complement(dna_sequence):
    return dna_complement(dna_sequence)[::-1]
def rna_cleaner(rna_sequence):
    clean = ""
    for base in rna_sequence:
        if base in ["A","U","G","C"]:
            clean += base
    return clean
def rna_nucleotide_count(rna_sequence):
    countA = rna_sequence.count("A")
    countU = rna_sequence.count("U")
    countG = rna_sequence.count("G")
    countC = rna_sequence.count("C")
    return {"A":countA,"U":countU,"G":countG,"C":countC}
def rna_codon_frequency(rna_sequence):
    codon_count = {}
    for i in range(0,len(rna_sequence),3):
        codon = rna_sequence[i:i+3]
        if len(codon) < 3:
            break
        if codon in codon_count:
            codon_count[codon] += 1
        else:
            codon_count[codon] = 1
    print("Codon frequency :")
    for codon, count in codon_count.items():
        print(f"{codon}: {count}")
    return codon_count
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
            protein += "STOP"
            break
        amino_acid = codon_dictionary.get(codon)
        if amino_acid:
            protein += amino_acid + " - "
    if protein.endswith(" - "):
        protein = protein[:-3]
    return protein

# System
while True:
    if proceed in ["Y","YES"]:
        print("---BIOINFORMATICS TOOLKIT---")
        print("Which feature you want to use:")
        print("1. DNA Operations")
        print("2. DNA Transformation")
        print("3. RNA Operations")
        print("4. Protein Operations")
        print("5. Exit")
        option = input("Select an option: ")
        if not option.isdigit():
            print("Enter a valid number!")
            continue
        if option == "1":
            print("---DNA Operations---")
            input1 = input("Enter DNA sequence :").upper()
            clean1 = dna_cleaner(input1)
            print("1. Clean DNA")
            print("2. Validate DNA")
            print("3. DNA Length")
            print("4. Count Nucleotide")
            print("5. GC Content(%)")
            print("6. Find DNA Pattern")
            print("7. Check DNA Palindrome")
            print("8. Detect DNA Mutation")
            print("9. Exit")
            choice1 = input("Select an option: ")
            if not choice1.isdigit():
                print("Enter a valid number!")
                continue
            if choice1 == "1":
                print(f"Clean DNA : {clean1}")
            elif choice1 == "2":
                print(dna_validator(input1,clean1))
            elif choice1 == "3":
                print(f"Length of DNA : {len(clean1)}")
            elif choice1 == "4":
                print(f"{dna_nucleotide_count(clean1)}")
            elif choice1 == "5":
                print(f"GC Content : {gc_content_calc(clean1)}%")
            elif choice1 == "6":
                pattern = input("Enter your pattern : ").upper()
                print(f"Pattern find : {dna_pattern_find(clean1,pattern)}")
            elif choice1 == "7":
                if clean1 == dna_reverse_complement(clean1):
                    print("This DNA sequence is a palindrome")
                else:
                    print("This DNA sequence is NOT a palindrome")
            elif choice1 == "8":
                input_to_detect = input("Enter a DNA sequence to check mutation :").upper()
                mutations = dna_mutation_detect(clean1,dna_cleaner(input_to_detect))
                for m in mutations:
                    print(m)
            elif choice1 == "9":
                print("Bye Bye")
                break
            else:
                print("Invalid option! Try again")
        elif option == "2":
            print("---DNA Transformation---")
            input2 = input("Enter DNA sequence :").upper()
            clean2 = dna_cleaner(input2)
            print("1. Reverse DNA")
            print("2. DNA to RNA(Transcription)")
            print("3. DNA Complement")
            print("4. DNA Reverse Complement")
            print("5. Exit")
            choice2 = input("Select an option: ")
            if not choice2.isdigit():
                print("Enter a valid number!")
                continue
            if choice2 == "1":
                print(f"Reversed DNA : {clean2[::-1]}")
            elif choice2 == "2":
                print(f"RNA sequence : {dna_to_rna(clean2)}")
            elif choice2 == "3":
                print(f"DNA complement : {dna_complement(clean2)}")
            elif choice2 == "4":
                print(f"DNA reverse complement : {dna_reverse_complement(clean2)}")
            elif choice2 == "5":
                print("Bye Bye")
                break
            else:
                print("Invalid option! Try again")
        elif option == "3":
            print("---RNA Operations---")
            rna_input1 = input("Enter RNA sequence :").upper()
            rna_clean1 = rna_cleaner(rna_input1)
            print("1. RNA Cleaner")
            print("2. Count RNA Nucleotide")
            print("3. RNA Codon Frequency")
            print("4. Exit")
            choice3 = input("Select an option: ")
            if not choice3.isdigit():
                print("Enter a valid number!")
                continue
            if choice3 == "1":
                print(f"Clean RNA : {rna_clean1}")
            elif choice3 == "2":
                print(rna_nucleotide_count(rna_clean1))
            elif choice3 == "3":
                print(rna_codon_frequency(rna_clean1))
            elif choice3 == "4":
                print("Bye Bye")
                break
            else:
                print("Invalid option! Try again")
        elif option == "4":
            print("---Protein Operations---")
            rna_input2 = input("Enter RNA sequence :").upper()
            rna_clean2 = rna_cleaner(rna_input2)
            print("1. RNA to Protein(Translation)")
            print("2. Exit")
            choice4 = input("Select an option: ")
            if not choice4.isdigit():
                print("Enter a valid number!")
                continue
            if choice4 == "1":
                print(f"Protein sequence :\n{rna_to_protein(rna_clean2)}")
            elif choice4 == "2":
                print("Bye Bye")
                break
            else:
                print("Invalid option! Try again")
    elif proceed in ["N","NO"]:
        print("OK Thanks!")
        break
    else:
        print("Invalid option! Try again")
