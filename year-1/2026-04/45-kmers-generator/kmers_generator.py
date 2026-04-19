# K mers of DNA

dna = input("Enter DNA Sequence : ").upper()
k = int(input("Enter k : "))

def dna_cleaner(dna_sequence):
    clean = ""
    for base in dna_sequence:
        if base in ["A","T","G","C"]:
            clean += base
    return clean
valid_dna = dna_cleaner(dna)
kmer_list = []
for i in range((len(valid_dna)-k)+1):
    kmers = valid_dna[i:i+k]
    kmer_list.append(kmers)
print(kmer_list)
