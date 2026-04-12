# DNA Sequence Analysis Toolkit

A Python-based bioinformatics toolkit that performs multiple analyses on a DNA sequence. It includes cleaning, transcription, nucleotide counting, GC content calculation, and sequence pattern detection.

## Features

- Removes invalid characters from DNA sequence  
- Converts DNA to RNA (T → U)  
- Calculates sequence length  
- Counts nucleotides (A, T, G, C)  
- Computes GC content percentage  
- Generates complement and reverse complement sequences  
- Detects start codon ("ATG") position  

## Example Output

Original DNA: ATGXCGAATIOGZC
Cleaned DNA: ATGCGAATGC
RNA Sequence: AUGCGAAUGC
Length of DNA sequence: 10
Nucleotide Count:
A: 3
T: 2
G: 2
C: 3
GC Content: 50.0%
Complement: TACGCTTACG
Reverse Complement: GCATTAGCAT
Codon 'ATG' found at position: 0

## What I Learned

- String manipulation in Python
- Using loops for sequence processing
- Using built-in functions like .count(), .replace(), and .find()
- Building a step-by-step bioinformatics pipeline
- Understanding DNA sequence analysis basics
