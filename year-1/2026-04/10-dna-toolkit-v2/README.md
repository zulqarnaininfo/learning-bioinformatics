# DNA Sequence Analysis Toolkit

A Python-based bioinformatics toolkit that performs multiple analyses on DNA sequences. This project started as a simple script and evolved into an interactive menu-based tool.

## Features

- Cleans DNA sequence by removing invalid characters  
- Converts DNA to RNA (T → U)  
- Calculates sequence length  
- Counts nucleotides (A, T, G, C)  
- Computes GC content percentage  
- Generates complement and reverse complement sequences  
- Detects start codon "ATG" position  
- Interactive menu-based system with continuous user input (v2)  

## Versions

- **v1**: Basic DNA analysis pipeline (runs all steps together)  
- **v2**: Interactive menu-driven toolkit using loop 'while True' and 'break' for continuous execution

## Example Output (v2)

```
--- DNA TOOLKIT ---
1. Clean DNA
2. Convert to RNA
3. Length
4. Count Nucleotides
5. GC Content
6. Complement and Reverse Complement
7. Find Codon 'ATG'
8. Exit

Choose an option: 1
Cleaned DNA: ATGCGTA

Choose an option: 3
Length: 7

Choose an option: 8
Bye Bye
```
## What I Learned

- String manipulation in Python
- Using loops and conditions for sequence processing
- Using built-in string methods like .count(), .replace(), and .find()
- Designing a step-by-step bioinformatics pipeline
- Building an interactive menu-based program
- Using while True and break to create continuous execution

## Development Journey

- Started with small individual scripts (nucleotide counting, GC content, transcription)
- Combined scripts into a single pipeline (v1)
- Initially added a "Full Analysis" option to run all features together
- As the code became larger and less efficient, improved the design
- Replaced full analysis with a loop-based system (while True) for better control and usability
- Final result is an interactive toolkit where users can perform operations repeatedly without restarting the program

## Date
12 April 2026
