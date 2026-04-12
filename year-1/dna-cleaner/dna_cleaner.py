# DNA Cleaner for invalid base
dna_seq = str(input()).upper()
clean_dna = ""
for base in dna_seq:
    if base in ["A","T","G","C"]:
        clean_dna += base
print(f"Original DNA sequence :\n{dna_seq}")
print(f"Clean DNA :\n{clean_dna}")
