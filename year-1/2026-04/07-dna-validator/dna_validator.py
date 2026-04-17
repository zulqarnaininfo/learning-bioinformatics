# DNA Validator
dna_seq = str(input())
dna_seq = dna_seq.upper()

# flag variable
is_valid = True
for base in dna_seq:
    if base not in ["A","T","G","C"]:
        is_valid = False
        break
if is_valid:
    print(f"DNA Sequence :{dna_seq}")
else:
    print("DNA sequence is not valid.")
