# Cleaning RNA from a file 

def rna_cleaner(rna_sequence):
    clean = ""
    for base in rna_sequence:
        if base in ["A","U","G","C"]:
            clean += base
    return clean

with open("rna.txt","r") as f:
    for line in f:
        line = line.strip().upper()
        clean_rna = rna_cleaner(line)
        print(f"Original : {line}")
        print(f"Cleaned : {clean_rna}\n")
