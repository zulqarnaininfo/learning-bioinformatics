# Complement and Reverse Complement (Functions Upgrade)

dna_input = input("Enter DNA sequence : ").upper()

# Functions
def dna_cleaner(dirty_dna):
    clean = ""
    for base in dirty_dna:
        if base in ["A","T","G","C"]:
            clean += base
    return clean
def dna_complement(dna_seq):
    complement = ""
    for base in dna_seq:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
    return complement
def dna_reverse_complement(complement):
    reverse_complement = complement[::-1]
    return reverse_complement

dna_seq = dna_cleaner(dna_input)
print(f"DNA sequence : {dna_seq}")
complement = dna_complement(dna_seq)
print(f"Complement : {complement}")
reverse_complement = dna_reverse_complement(complement)
print(f"Reverse complement : {reverse_complement}")
