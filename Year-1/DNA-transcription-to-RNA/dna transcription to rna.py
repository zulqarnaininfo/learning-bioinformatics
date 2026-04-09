# DNA Transcription to RNA

# let's say
dna_seq = "ATGCGTACGTTAGCCT"
rna_seq = ""
for base in dna_seq:
    if base == "A":
        rna_seq += "A"
    elif base == "T":
        rna_seq += "U"
    elif base == "G":
        rna_seq += "G"
    elif base == "C":
        rna_seq += "C"
print(f"DNA sequence :{dna_seq}")
print(f"RNA sequence :{rna_seq}")