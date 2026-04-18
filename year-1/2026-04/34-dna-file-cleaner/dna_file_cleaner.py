# Cleaning DNA from a file 

def dna_cleaner(dna_sequence):
    clean = ""
    for base in dna_sequence:
        if base in ["A","T","G","C"]:
            clean += base
    return clean

with open("dna.txt","r") as f:
    for line in f:
        line = line.strip().upper()
        clean_dna = dna_cleaner(line)
        print(f"Original : {line}")
        print(f"Cleaned : {clean_dna}\n")
