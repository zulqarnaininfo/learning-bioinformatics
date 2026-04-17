# Codon Frequency Analyzer

rna_input = str(input("Enter RNA sequence :")).upper()
rna_seq = ""
for base in rna_input:
    if base in ["A","U","G","C"]:
        rna_seq += base

codon_count = {}
for i in range(0,len(rna_seq),3):
    codon = rna_seq[i:i+3]
    if len(codon) < 3:
        break
    if codon in codon_count:
        codon_count[codon] += 1
    else:
        codon_count[codon] = 1
print("Codon frequency :")
for codon, count in codon_count.items():
    print(f"{codon}: {count}")
