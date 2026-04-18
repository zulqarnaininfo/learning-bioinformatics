# GC Content of DNA from a file 

def dna_cleaner(dna_sequence):
    clean = ""
    for base in dna_sequence:
        if base in ["A","T","G","C"]:
            clean += base
    return clean
def gc_content_calc(dna_sequence):
    if len(dna_sequence) == 0:
        return 0
    countG = dna_sequence.count("G")
    countC = dna_sequence.count("C")
    gc_count = countG + countC
    gc_percent = ((gc_count/len(dna_sequence))*100).__round__(2)
    return gc_percent
with open("dna.txt","r") as f:
    for line in f:
        line = line.strip().upper()
        clean_dna = dna_cleaner(line)
        gc_content = gc_content_calc(clean_dna)
        print(f"Original : {line}")
        print(f"Cleaned : {clean_dna}")
        print(f"GC Content : {gc_content}%\n")
