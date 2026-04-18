# # Bioinformatics Toolkit (CLI Tool)

This project is a menu-driven Bioinformatics Toolkit built using Python. It combines multiple smaller bioinformatics scripts into a single unified tool. This toolkit allows users to perform analysis on DNA, RNA, and Protein sequences through an interactive command-line interface.

## Features

- **DNA Operations**  
DNA cleaning, DNA validation, Length calculation, Nucleotide counting, GC content calculation, Pattern finding, Palindrome checking, and Mutation detection  
- **DNA Transformation**  
Reverse DNA, DNA → RNA (Transcription), Complement, and Reverse Complement  
- **RNA Operations**  
RNA cleaning, RNA nucleotide counting, and Codon frequency analysis
- **Protein Operations**  
RNA → Protein translation with Start codon (AUG) detection and Stop codon handling

## Example Output

```
Welcome! This is a Bioinformatics tool, do you wish to continue?
Y/N : Y

---BIOINFORMATICS TOOLKIT---
Which feature you want to use:
1. DNA Operations
2. DNA Transformation
3. RNA Operations
4. Protein Operations
5. Exit
Select an option: 1

---DNA Operations---
Enter DNA sequence : ATGCGTAXXTGC

1. Clean DNA
2. Validate DNA
3. DNA Length
4. Count Nucleotide
5. GC Content(%)
6. Find DNA Pattern
7. Check DNA Palindrome
8. Detect DNA Mutation
9. Exit
Select an option: 2

DNA is invalid. Invalid characters removed :2
```

## What I Learned

- How to build and organize large Python programs
- Proper use of functions (def, return)
- Difference between printing vs returning values
- Handling user input safely
- Debugging logical mistakes
- Writing reusable and modular code
- Using dictionaries (codon mapping)
- Designing a menu-driven CLI tool
- Improving code step-by-step instead of rewriting everything

## Problems I Faced & Fixes

❌ Problem 1: Mutation detector stopped earlier  
🔴 Original Code
```py
def dna_mutation_detect(dna_seq1, dna_seq2):
    for i in range(len(dna_seq1)):
        if dna_seq1[i] != dna_seq2[i]:
            print(f"Mutation at {i}")
            return 0
```
✅ Fixed Code
```py
def dna_mutation_detect(dna_seq1, dna_seq2):
    if len(dna_seq1) != len(dna_seq2):
        return ["DNA sequences are not the same length!"]
    mutations = []
    for i in range(len(dna_seq1)):
        if dna_seq1[i] != dna_seq2[i]:
            mutations.append(f"Position {i}: {dna_seq1[i]} -> {dna_seq2[i]}")
    if not mutations:
        return ["No mutation detected."]
    return mutations
```
❌ Problem 2: Function returning None  
🔴 Original Code
```py
def dna_mutation_detect(...):
    print("Mutation found")
print(dna_mutation_detect(seq1, seq2))
```
✅ Fixed Code
```py
mutations = dna_mutation_detect(seq1, seq2)
for m in mutations:
    print(m)
```

## Development Journey

- Started with very small scripts
- Practiced each concept separately
- Converted scripts into function-based versions
- Built multiple mini-tools
- Combined everything into one toolkit
- Fixed issues step-by-step
- Improved structure and usability

## Learning Goals

- Store DNA once and reuse across operations
- Learn about FASTA format
- Improve UI design
- ORF (Open Reading Frame) detection
- Optimize using advanced Python techniques
- Calculate molecular weight of protein

## Notes

This project shows my transition from: 
- beginner scripts → structured bioinformatics tool  
- It focuses on learning, experimentation, and improvement before using advanced libraries like Biopython.

## Date
18 April 2026
