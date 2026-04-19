# K mers of DNA from a file

k = int(input("Enter k : "))

# functions
def dna_cleaner(dna_sequence):
    clean = ""
    for base in dna_sequence:
        if base in ["A","T","G","C"]:
            clean += base
    return clean
def kmers_generator(dna_sequence,k):
    kmer_list = []
    for i in range((len(dna_sequence)-k)+1):
        kmers = dna_sequence[i:i+k]
        kmer_list.append(kmers)
    return kmer_list

with open("dna.txt","r") as f:
    for line in f:
        line = line.strip().upper()
        valid_dna = dna_cleaner(line)
        kmers = kmers_generator(valid_dna,k)
        print(f"DNA : {valid_dna}")
        print(f"Kmers : {kmers}\n")
