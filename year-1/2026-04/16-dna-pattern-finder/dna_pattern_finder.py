# DNA Pattern Finder(Multiple Positions)

dna_seq = str(input("Enter DNA sequence :")).upper()
pattern = str(input("Enter pattern :")).upper()
positions = []
pattern_length = len(pattern)

for i in range(len(dna_seq)-pattern_length+1):
    if dna_seq[i:i+pattern_length] == pattern:
        positions.append(i)
print(f"Pattern found at position(s) :{positions}")
