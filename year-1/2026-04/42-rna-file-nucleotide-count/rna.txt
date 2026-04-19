# Counting Nucleotides of RNA from a file 

def rna_cleaner(rna_sequence):
    clean = ""
    for base in rna_sequence:
        if base in ["A","U","G","C"]:
            clean += base
    return clean
def rna_nucleotide_count(rna_sequence):
    countA = rna_sequence.count("A")
    countU = rna_sequence.count("U")
    countG = rna_sequence.count("G")
    countC = rna_sequence.count("C")
    return {"A":countA,"U":countU,"G":countG,"C":countC}
with open("rna.txt","r") as f:
    for line in f:
        line = line.strip().upper()
        clean_rna = rna_cleaner(line)
        nucleotides = rna_nucleotide_count(clean_rna)
        print(f"Original : {line}")
        print(f"Cleaned : {clean_rna}")
        print(f"Nucleotide count : {nucleotides}\n")
