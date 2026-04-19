# DNA to RNA from a file

def dna_cleaner(dna_sequence):
    clean = ""
    for base in dna_sequence:
        if base in {"A","T","G","C"}:
            clean += base
    return clean
def rna_converter(dna_sequence):
    rna = dna_sequence.replace("T","U")
    return rna
with open("dna.txt","r") as f:
    for line in f:
        line = line.strip().upper()
        clean_dna = dna_cleaner(line)
        rna_seq = rna_converter(clean_dna)
        print(f"Original : {line}")
        print(f"Cleaned : {clean_dna}")
        print(f"RNA sequence : {rna_seq}\n")
