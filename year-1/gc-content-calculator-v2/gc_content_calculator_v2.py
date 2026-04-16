# GC Content Calculator V2 (functions Upgrade)

dna_input = input("Enter DNA sequence : ").upper()

# Functions
def dna_cleaner(dirty_dna):
    clean = ""
    for base in dirty_dna:
        if base in ["A","T","G","C"]:
            clean += base
    return clean
def gc_content_calc(dna_sequence):
    countG = dna_sequence.count("G")
    countC = dna_sequence.count("C")
    gc_count = countG + countC
    gc_percent = ((gc_count/len(dna_sequence))*100).__round__(2)
    return gc_percent

dna_seq = dna_cleaner(dna_input)
print(f"DNA sequence : {dna_seq}")
gc_content = gc_content_calc(dna_seq)
print(f"GC Content : {gc_content}%")
