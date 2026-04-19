# Detecting Mutation of DNA from a file

def dna_cleaner(dna_sequence):
    clean = ""
    for base in dna_sequence:
        if base in {"A","T","G","C"}:
            clean += base
    return clean
def mutation_detector(dna_seq1,dna_seq2):
    if dna_seq1 == dna_seq2:
        return "No mutation detected."
    else:
        return "Mutation detected."
with open("dna.txt","r") as f:
        lines = f.read().splitlines()
        line1 = lines[0].strip().upper()
        line2 = lines[1].strip().upper()
        clean_dna1 = dna_cleaner(line1)
        clean_dna2 = dna_cleaner(line2)
        mutation = mutation_detector(clean_dna1,clean_dna2)
        print(f"DNA1 : {clean_dna1}")
        print(f"DNA2 : {clean_dna2}")
        print(f"Mutation : {mutation}")
        print(lines)
        print(len(lines))
