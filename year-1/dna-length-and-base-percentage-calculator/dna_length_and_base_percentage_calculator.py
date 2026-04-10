# DNA Lenght and Base Percentage Calculator

# let's say
dna = "ATGCGATCGATCG"
lenght_dna = len(dna)
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
percent_A = (count_A/lenght_dna)*100
percent_T = (count_T/lenght_dna)*100
percent_G = (count_G/lenght_dna)*100
percent_C = (count_C/lenght_dna)*100
print(f"DNA seq :{dna}")
print(f"Lenght :{lenght_dna}")
print(f"A :{count_A}({percent_A}%)")
print(f"T :{count_T}({percent_T}%)")
print(f"G :{count_G}({percent_G}%)")
print(f"C :{count_C}({percent_C}%)")