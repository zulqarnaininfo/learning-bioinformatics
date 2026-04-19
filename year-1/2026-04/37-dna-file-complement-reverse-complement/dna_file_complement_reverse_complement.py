# Complement and Reverse Complement of DNA from a file

def dna_cleaner(dna_sequence):
    clean = ""
    for base in dna_sequence:
        if base in {"A","T","G","C"}:
            clean += base
    return clean
def complement_dna(dna_sequence):
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
def reverse_complement_dna(dna_sequence):
    reverse_complement = complement_dna(dna_sequence)[::-1]
    return reverse_complement
with open("dna.txt","r") as f:
    for line in f:
        line = line.strip().upper()
        clean_dna = dna_cleaner(line)
        complement = complement_dna(clean_dna)
        reverse_complement = reverse_complement_dna(clean_dna)
        print(f"Original : {line}")
        print(f"Cleaned : {clean_dna}")
        print(f"complement : {complement}")
        print(f"Reverse complement : {reverse_complement}\n")
