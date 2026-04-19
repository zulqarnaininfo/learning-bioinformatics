# Finding pattern 'ATG' from a file

def dna_cleaner(dna_sequence):
    clean = ""
    for base in dna_sequence:
        if base in {"A","T","G","C"}:
            clean += base
    return clean
def pattern_atg(dna_sequence):
    positions = []
    for i in range(len(dna_sequence)-2):
        if dna_sequence[i:i+3] == "ATG":
            positions.append(i)
    return positions
with open("dna.txt","r") as f:
    for line in f:
        line = line.strip().upper()
        clean_dna = dna_cleaner(line)
        pattern = pattern_atg(clean_dna)
        print(f"Original : {line}")
        print(f"Cleaned : {clean_dna}")
        print(f"Pattern 'ATG' found at position : {pattern}\n")
