# DNA Cleaner V2 (Function Upgrade)

input_dna = str(input("Enter DNA sequence : ")).upper()

# DNA cleaner function
def dna_cleaner(dirty_dna):
    clean = ""
    invalid_count = 0
    for base in dirty_dna:
        if base in ["A","T","G","C"]:
            clean += base
        else:
            invalid_count += 1
    return clean, invalid_count

dna_seq, removed_chr = dna_cleaner(input_dna)
print(f"Clean DNA : {dna_seq}")
print(f"Number of invalid characters : {removed_chr}")
