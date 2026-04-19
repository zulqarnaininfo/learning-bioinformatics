# RNA codon frequency from a file 

def rna_cleaner(rna_sequence):
    clean = ""
    for base in rna_sequence:
        if base in ["A","U","G","C"]:
            clean += base
    return clean
def rna_codon_frequency(rna_sequence):
    codon_count = {}
    for i in range(0,len(rna_sequence),3):
        codon = rna_sequence[i:i+3]
        if len(codon) < 3:
            break
        if codon in codon_count:
            codon_count[codon] += 1
        else:
            codon_count[codon] = 1
    return codon_count
with open("rna.txt","r") as f:
    for line in f:
        line = line.strip().upper()
        clean_rna = rna_cleaner(line)
        frequency = rna_codon_frequency(clean_rna)
        print(f"Original : {line}")
        print(f"Cleaned : {clean_rna}")
        print(f"Codon frequency : {frequency}\n")
