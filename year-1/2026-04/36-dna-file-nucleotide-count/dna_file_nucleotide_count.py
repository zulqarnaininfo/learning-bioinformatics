# Counting Nucleotides of DNA from a file 

def dna_cleaner(dna_sequence):
    clean = ""
    for base in dna_sequence:
        if base in ["A","T","G","C"]:
            clean += base
    return clean
def dna_nucleotide_count(dna_sequence):
    countA = dna_sequence.count("A")
    countT = dna_sequence.count("T")
    countG = dna_sequence.count("G")
    countC = dna_sequence.count("C")
    return {"A":countA,"T":countT,"G":countG,"C":countC}
with open("dna.txt","r") as f:
    for line in f:
        line = line.strip().upper()
        clean_dna = dna_cleaner(line)
        nucleotides = dna_nucleotide_count(clean_dna)
        print(f"Original : {line}")
        print(f"Cleaned : {clean_dna}")
        print(f"Nucleotide count : {nucleotides}\n")
