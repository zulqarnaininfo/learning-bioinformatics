# DNA Sequence Validator v2

dna_input = str(input("Enter DNA sequence :")).upper()
dna_seq = ""
for base in dna_input:
    if base in ["A","T","G","C"]:
        dna_seq += base

if dna_input == dna_seq:
    print("DNA sequence is valid")
else:
    invalid_count = 0
    for base in dna_input:
        if base not in ["A","T","G","C"]:
            invalid_count += 1
    print("DNA is invalid")
    print(f"Invalid characters removed :{invalid_count}")
    print(f"Clean DNA: {dna_seq}")
