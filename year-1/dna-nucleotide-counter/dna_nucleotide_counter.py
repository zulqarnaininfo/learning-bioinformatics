# DNA Nucleotide Counter
# dna seq example
dna = "ATGCGTACGTTAGCTAGGCTAATCGGATCGTACGATGCTAGCTAGGCTA"
count_A = 0
count_T = 0
count_G = 0
count_C = 0
for base in dna:
    if base == "A":
        count_A += 1
    elif base == "T":
        count_T += 1
    elif base == "G":
        count_G += 1
    elif base == "C":
        count_C += 1

print(f"Total length :{len(dna)}")
print(f"A :{count_A}")
print(f"T :{count_T}")
print(f"G :{count_G}")
print(f"C :{count_C}")
