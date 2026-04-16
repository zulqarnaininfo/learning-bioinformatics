# RNA Nucleotide Counter V2 (Functions Upgrade)

rna_input = input("Enter RNA sequence : ").upper()

# Functions
def rna_cleaner(dirty_rna):
    clean = ""
    for base in dirty_rna:
        if base in ["A","U","G","C"]:
            clean += base
    return clean
def nucleotide_counter(rna_sequence):
    countA = rna_sequence.count("A")
    countU = rna_sequence.count("U")
    countG = rna_sequence.count("G")
    countC = rna_sequence.count("C")
    return countA, countU, countG, countC

rna_seq = rna_cleaner(rna_input)
countA, countU, countG, countC = nucleotide_counter(rna_seq)
print(f"RNA sequence : {rna_seq}")
print(f"A : {countA}")
print(f"U : {countU}")
print(f"G : {countG}")
print(f"C : {countC}")
