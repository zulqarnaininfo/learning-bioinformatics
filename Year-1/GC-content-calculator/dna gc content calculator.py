# GC Content Calculator

# let's say
dna_seq = "ATGCGATCCATGACAATGCTGGCCAAGCTA"
count_G = 0
count_C = 0
for base in dna_seq:
    if base == "G":
        count_G += 1
    elif base == "C":
        count_C += 1
gc_count = count_G+count_C
gc_percent = (gc_count/len(dna_seq))*100
print(f"DNA Sequence :{dna_seq}")
print(f"GC Count :{gc_percent}%")