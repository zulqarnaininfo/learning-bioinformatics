# RNA Cleaner V2 (Functions Upgrade)

rna_input = input("Enter RNA sequence : ").upper()

# Functions
def rna_cleaner(dirty_rna):
    clean = ""
    invalid_count = 0
    for base in dirty_rna:
        if base in ["A","U","G","C"]:
            clean += base
        else:
            invalid_count += 1
    return clean, invalid_count

rna_seq, removed_chr = rna_cleaner(rna_input)
print(f"Clean RNA : {rna_seq}")
print(f"Number of invalid characters : {removed_chr}")
