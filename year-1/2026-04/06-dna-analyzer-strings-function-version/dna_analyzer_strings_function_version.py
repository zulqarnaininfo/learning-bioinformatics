# DNA Analyzer
# using string functions

dna_seq ="ATGCGATACGTTAGC"
# Counting Nucleotides
count_A = dna_seq.count("A")
count_T = dna_seq.count("T")
count_G = dna_seq.count("G")
count_C = dna_seq.count("C")
print(f"DNA Sequence :{dna_seq}")
print("Nucleotide Count :")
print(f"A :{count_A}")
print(f"T :{count_T}")
print(f"G :{count_G}")
print(f"C :{count_C}")

# Convert to RNA
rna_seq = dna_seq.replace("T","U")
print(f"RNA Sequence :{rna_seq}")

# Position of a Codon "ATG"
position = dna_seq.find("ATG")
if position != -1:
    print(f"Codon 'ATG' Found at Position :{position}")
else:
    print("Codon 'ATG' not found.")
