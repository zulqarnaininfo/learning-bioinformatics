# DNA Palindrome

# A DNA sequence is a palindrome if it is equal to its reverse complement.

dna_input = str(input("Enter DNA sequence :")).upper()
dna_seq = ""
for base in dna_input:
    if base in ["A","T","G","C"]:
        dna_seq += base

complement_dna = ""
for base in dna_seq:
    if base == "A":
        complement_dna += "T"
    elif base == "T":
        complement_dna += "A"
    elif base == "G":
        complement_dna += "C"
    elif base == "C":
        complement_dna += "G"
reverse_complement = complement_dna[::-1]
if reverse_complement == dna_seq:
    print("This DNA sequence is a palindrome.")
else:
    print("This DNA sequence is NOT a palindrome.")
