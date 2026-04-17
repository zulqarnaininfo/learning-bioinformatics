# DNA Sequence Analysis Toolkit v2 (Functions Version)

# Input DNA
dna_input = input("Enter DNA sequence :").upper()

# Functions
def dna_cleaner(dirty_dna):
    clean = ""
    for base in dirty_dna:
        if base in ["A","T","G","C"]:
            clean += base
    return clean
def rna_converter(dna_sequence):
    rna_sequence = dna_sequence.replace("T","U")
    return rna_sequence
def length_calc(dna_sequence):
    length = len(dna_sequence)
    return length
def nucleotide_counter(dna_sequence):
    count_A = dna_sequence.count("A")
    count_T = dna_sequence.count("T")
    count_G = dna_sequence.count("G")
    count_C = dna_sequence.count("C")
    return {"A":count_A,"T":count_T,"G":count_G,"C":count_C}
def gc_content_calc(dna_sequence):
    if len(dna_sequence) == 0:
        return None
    gc_count = dna_sequence.count("G")+dna_sequence.count("C")
    gc_percent = ((gc_count/len(dna_sequence))*100).__round__(2)
    return gc_percent
def get_complement(dna_sequence):
    complement_dna = ""
    for base in dna_sequence:
        if base == "A":
            complement_dna += "T"
        elif base == "T":
            complement_dna += "A"
        elif base == "G":
            complement_dna += "C"
        elif base == "C":
            complement_dna += "G"
    return complement_dna
def get_reverse_complement(dna_sequence):
    reversed_dna = reversed(dna_sequence)
    reverse_complement = ""
    for base in reversed_dna:
        if base == "A":
            reverse_complement += "T"
        elif base == "T":
            reverse_complement += "A"
        elif base == "G":
            reverse_complement += "C"
        elif base == "C":
            reverse_complement += "G"
    return reverse_complement
def codon_atg_finder(dna_sequence):
    codon_atg = dna_sequence.find("ATG")
    return codon_atg

# DNA sequence
dna_seq = dna_cleaner(dna_input)

# Menu
run = True
while run:
    print("--->DNA TOOLKIT<---")
    print("1. Clean DNA")
    print("2. Convert to RNA")
    print("3. Calculate Length of DNA")
    print("4. Count Nucleotides")
    print("5. GC Content")
    print("6. Complement and Reverse Complement")
    print("7. Find Codon 'ATG'")
    print("8. Exit")
    choice = input("Choose an option :")

# Choices
    if choice == "1":
        print(f"Original DNA : {dna_input}")
        print(f"Clean DNA : {dna_seq}")
    elif choice == "2":
        print(f"RNA Sequence : {rna_converter(dna_seq)}")
    elif choice == "3":
        print(f"Length of DNA sequence : {length_calc(dna_seq)}")
    elif choice == "4":
        print(f"Nucleotide Count : {nucleotide_counter(dna_seq)}")
    elif choice == "5":
        gc_content = gc_content_calc(dna_seq)
        if gc_content is not None:
            print(f"GC Content : {gc_content}%")
        else:
            print("Length of cleaned DNA is zero!")
    elif choice == "6":
        print(f"Complement : {get_complement(dna_seq)}")
        print(f"Reverse Complement : {get_reverse_complement(dna_seq)}")
    elif choice == "7":
        atg_codon = codon_atg_finder(dna_seq)
        if atg_codon != -1:
            print(f"Codon 'ATG' found at position : {atg_codon}")
        else:
            print("Codon 'ATG' not found.")
    elif choice == "8":
        print("Bye Bye")
        break
    else:
        print("Invalid choice! choose again")
