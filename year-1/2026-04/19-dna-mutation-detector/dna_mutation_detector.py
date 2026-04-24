# DNA Mutation Detector (For Same Length of Sequence)

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

if len(dna_seq1) != len(dna_seq2):
    print("DNA sequences are not the same length!")
else:
    mutation_found = False
    for i in range(len(dna_seq1)):
        if dna_seq1[i] != dna_seq2[i]:
            print(f"Mutation at position {i}: {dna_seq1[i]} -> {dna_seq2[i]}")
            mutation_found = True
    if not mutation_found:
        print("No mutation detected. DNA sequences are identical.")
