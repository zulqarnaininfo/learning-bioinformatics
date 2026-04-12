# DNA Sequence Analysis Toolkit v2

# Input DNA
dna_input = str(input()).upper()
# Clean DNA
dna_seq = ""
for base in dna_input:
     if base in ["A","T","G","C"]:
          dna_seq += base
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
    print("7. Find Codon'ATG'")
    print("8. Exit")
    choice = input("Choose an option :")
# 1. Cleaning of DNA sequence
    if choice == "1":
        print(f"Original DNA : {dna_input}")
        print(f"Cleaned DNA : {dna_seq}")
# 2. RNA conversion
    elif choice == "2":
        rna_seq = dna_seq.replace("T","U")
        print(f"RNA Sequence : {rna_seq}")
# 3. Length of DNA sequence
    elif choice == "3":
        length_dna = len(dna_seq)
        print(f"Length of DNA sequence : {length_dna}")
# 4. Counting Nucleotides
    elif choice == "4":
        count_A = dna_seq.count("A")
        count_T = dna_seq.count("T")
        count_G = dna_seq.count("G")
        count_C = dna_seq.count("C")
        print("Nucleotide Count :")
        print(f"A : {count_A}")
        print(f"T : {count_T}")
        print(f"G : {count_G}")
        print(f"C : {count_C}")
# 5. GC Content
    elif choice == "5":
        gc_count = count_G+count_C
        if gc_count > 0:
            gc_content = (gc_count/length_dna)*100
            print(f"GC Content : {gc_content}%")
        else:
            print("GC Content 0%")
# 6. Complement and Reverse Complement
    elif choice == "6":
        complement_dna = ""
        for base in dna_seq:
            if base == "A":
                complement_dna += "T"
            elif base == "T":
                complement_dna += "A"
            elif base == "G":
                complement_dna += "C"
            elif base == "C":
                complement_dna += "G"
        reverse_complement = complement_dna[::-1]
        print(f"Complement : {complement_dna}")
        print(f"Reverse Complement : {reverse_complement}")
# 7. Finding Codon "ATG"
    elif choice == "7":
        codon_atg = dna_seq.find("ATG")
        if codon_atg != -1:
            print(f"Codon 'ATG' found at position : {codon_atg}")
        else:
            print("Codon 'ATG' not found.")
# 8. Exit
    elif choice == "8":
        print("Bye Bye")
        break
# Invalid input
    else:
        print("Invalid Choice!")
