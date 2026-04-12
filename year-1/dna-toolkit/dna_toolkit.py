# DNA Sequence Analysis Toolkit

# Cleaning of DNA sequence
dna_input = str(input()).upper()
dna_seq = ""
for base in dna_input:
    if base in ["A","T","G","C"]:
        dna_seq += base
print(f"Original DNA : {dna_input}")
print(f"Cleaned DNA : {dna_seq}")

# RNA conversion
rna_seq = dna_seq.replace("T","U")
print(f"RNA Sequence : {rna_seq}")

# Length of DNA sequence
length_dna = len(dna_seq)
print(f"Length of DNA sequence : {length_dna}")

# Counting Nucleotides
count_A = dna_seq.count("A")
count_T = dna_seq.count("T")
count_G = dna_seq.count("G")
count_C = dna_seq.count("C")
print("Nucleotide Count :")
print(f"A : {count_A}")
print(f"T : {count_T}")
print(f"G : {count_G}")
print(f"C : {count_C}")

# GC Content
gc_count = count_G+count_C
gc_content = (gc_count/length_dna)*100
print(f"GC Content : {gc_content}%")

# Complement and Reverse Complement
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

# Finding Codon "ATG"
codon_atg = dna_seq.find("ATG")
if codon_atg != -1:
    print(f"Codon 'ATG' found at position : {codon_atg}")
else:
    print("Codon 'ATG' not found.")
