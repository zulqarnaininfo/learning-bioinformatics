# DNA Sequence Analysis Toolkit v3

This project is a Python-based bioinformatics toolkit designed to perform common DNA sequence analysis tasks. It allows users to input a DNA sequence, clean it, and perform multiple operations such as transcription, nucleotide counting, GC content calculation, and more. The toolkit demonstrates how basic biological concepts can be implemented using programming and how code can evolve from simple scripts into a structured, interactive tool.

## Features

- DNA sequence cleaning (removes invalid characters)
- DNA → RNA transcription
- DNA length calculation
- Nucleotide counting (A, T, G, C)
- GC content calculation (percentage)
- DNA complement generation
- Reverse complement generation
- Codon (ATG) detection
- Interactive menu system for repeated usage

## Versions

- v1: Basic DNA analysis pipeline (runs all steps together)
- v2: Interactive menu-driven toolkit using loop "while True" and "break" for continuous execution
- v3: Function-based modular toolkit with improved structure, reusable functions, and error handling (e.g., safe GC content calculation)

## Example Output (v3)
```
Enter DNA sequence: ATGXTCGAZ

--->DNA TOOLKIT<---
1. Clean DNA
2. Convert to RNA
3. Calculate Length of DNA
4. Count Nucleotides
5. GC Content
6. Complement and Reverse Complement
7. Find Codon 'ATG'
8. Exit

Choose an option: 1
Original DNA : ATGXTCGAZ
Clean DNA : ATTCGA

Choose an option: 5
GC Content : 50.0%

Choose an option: 6
Complement : TAAGCT
Reverse Complement : TCGATT
```

## What I Learned

- How to create and use functions for modular programming
- Importance of reusable and independent functions
- How to pass data between functions
- How to return single and multiple values from functions
- How to use dictionaries for structured output
- How to design an interactive menu using "while True"
- How "break" and conditional logic control program flow
- How to debug common errors (e.g., NoneType, variable scope)
- How to handle edge cases (e.g., empty DNA sequence in GC calculation)

## Development Journey

- Started with small individual scripts (nucleotide counting, GC content, transcription)
- Combined scripts into a single pipeline (v1)
- Initially added a "Full Analysis" option to run all features together
- As the code became larger and less efficient, improved the design
- Replaced full analysis with a loop-based system ("while True") for better control and usability
- Introduced functions to make the code reusable and modular
- Added error handling and improved data flow (cleaned DNA used across all functions)
- Final result is an interactive toolkit where users can perform operations repeatedly without restarting the program
