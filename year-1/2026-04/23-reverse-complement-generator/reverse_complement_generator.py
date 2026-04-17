# Reverse Complement Generator (Without Making Complement)

dna_input = str(input("Enter DNA sequence :")).upper()
dna_seq = ""
for base in dna_input:
    if base in ["A","T","G","C"]:
        dna_seq += base

reverse_complement = ""
for base in reversed(dna_seq):
    if base == "A":
        reverse_complement += "T"
    elif base == "T":
        reverse_complement += "A"
    elif base == "G":
        reverse_complement += "C"
    elif base == "C":
        reverse_complement += "G"

print(f"DNA : {dna_seq}\nReverse complement : {reverse_complement}")
