# GC Content Comparison

dna_input1 = str(input("Enter 1st DNA sequence :")).upper()
dna_input2 = str(input("Enter 2nd DNA sequence :")).upper()
dna_seq1 = ""
for base in dna_input1:
    if base in ["A","T","G","C"]:
        dna_seq1 += base
dna_seq2 = ""
for base in dna_input2:
    if base in ["A","T","G","C"]:
        dna_seq2 += base

if len(dna_seq1) == 0 or len(dna_seq2) == 0:
    print("One of the DNA sequence is empty after cleaning!")
else:
    gc_count1 = dna_seq1.count("G")+dna_seq1.count("C")
    gc_count2 = dna_seq2.count("G")+dna_seq2.count("C")
    gc_percent1 = ((gc_count1/len(dna_seq1))*100).__round__(2)
    gc_percent2 = ((gc_count2/len(dna_seq2))*100).__round__(2)
    print(f"GC content DNA 1 :{gc_percent1}%")
    print(f"GC content DNA 2 :{gc_percent2}%")
    if gc_percent1 > gc_percent2:
        print("DNA 1 has higher GC content")
    elif gc_percent1 == gc_percent2:
        print("GC content of both DNA are same")
    else:
        print("DNA 2 has higher GC content")
