# Complement of DNA
# let's say DNA sequence is
dna = "ATGCCGATGCGATCGTAGCTAGCTAGCTAG"
complement_dna = ""

for base in dna:
    if base == "A":
        complement_dna += "T"
    elif base == "T":
        complement_dna += "A"
    elif base == "G":
        complement_dna += "C"
    elif base == "C":
        complement_dna += "G"
print(f"Orignal :{dna}")
print(f"Complement :{complement_dna}")

# Reverse Complement of DNA
reverse_complement = complement_dna[::-1]
print(f"Reverse Complement :{reverse_complement}")