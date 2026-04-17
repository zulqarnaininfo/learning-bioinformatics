# Counting Nucleotides in RNA

# let's say
dna = "ATGCGTACGTTAGCCT"
rna = ""
for base in dna:
    if base == "T":
        rna += "U"
    else:
        rna += base
count_A = 0
count_U = 0
count_G = 0
count_C = 0
for base in rna:
    if base == "A":
        count_A += 1
    elif base == "U":
        count_U += 1
    elif base == "G":
        count_G += 1
    elif base == "C":
        count_C += 1
print(f"RNA Sequence :{rna}")
print(f"A :{count_A}")
print(f"U :{count_U}")
print(f"G :{count_G}")
print(f"C :{count_C}")
