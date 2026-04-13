# Codon List Generator

dna_seq = "ATGCGATAGCTA"
codons = []
for i in range(0,len(dna_seq),3):
    codon = dna_seq[i:i+3]
    codons.append(codon)
print(f"Original DNA sequence :{dna_seq}")
print(f"List of Codons :{codons}")
