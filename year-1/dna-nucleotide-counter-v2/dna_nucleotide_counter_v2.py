# DNA Nucleotide Counter V2 (Functions Upgrade)

dna_input = input("Enter DNA sequence : ").upper()

# Functions
def dna_cleaner(dirty_dna):
    clean = ""
    for base in dirty_dna:
        if base in ["A","T","G","C"]:
            clean += base
    return clean
def nucleotide_counter(dna_sequence):
    countA = dna_sequence.count("A")
    countT = dna_sequence.count("T")
    countG = dna_sequence.count("G")
    countC = dna_sequence.count("C")
    return countA, countT, countG, countC

dna_seq = dna_cleaner(dna_input)
countA, countT, countG, countC = nucleotide_counter(dna_seq)
print(f"DNA sequence : {dna_seq}")
print(f"A : {countA}")
print(f"T : {countT}")
print(f"G : {countG}")
print(f"C : {countC}")
