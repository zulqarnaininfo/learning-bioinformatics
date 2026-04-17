# DNA to Protein Bioinformatics Tool

This project is a Python-based bioinformatics tool that simulates the central biological process of gene expression. It takes a DNA sequence as input, cleans it, converts it into RNA (transcription), and then translates it into a protein sequence using the genetic code.
The program also provides an interactive menu that allows the user to perform different operations such as viewing cleaned DNA, RNA sequence, and protein sequence.

## Features

- DNA sequence cleaning (removal of invalid characters)
- DNA to RNA transcription
- RNA to Protein translation using codon mapping
- Start codon (AUG) based translation
- Stop codon (UAA, UAG, UGA) termination
- Interactive menu system
- Continuous execution until user exits

## Biological Concepts Used

- DNA (Deoxyribonucleic Acid)
- RNA (Ribonucleic Acid)
- Transcription (DNA → RNA)
- Translation (RNA → Protein)
- Codons (triplets of nucleotides)
- Start Codon (AUG - Methionine)
- Stop Codons (UAA, UAG, UGA)

## How It Works

1. The user inputs a DNA sequence  
2. The program cleans the sequence (keeps only A, T, G, C)  
3. DNA is converted into RNA by replacing T with U  
4. RNA is read in codons (groups of 3)  
5. Translation starts only when AUG is found  
6. Each codon is mapped to an amino acid using a dictionary made from codon table
7. Translation stops when a stop codon appears  
8. The final protein sequence is displayed  

## What I Learned

- How biological processes can be simulated using Python  
- How to use dictionaries for real-world data mapping  
- How to process sequences using loops and slicing  
- How start and stop codons control translation  
- How to build an interactive menu using loops  
- How to structure a program like a real tool instead of a script  

## Future Improvements

- Support for full genetic code (already partially implemented)  
- Input validation with error handling  
- Reading sequences from files (FASTA format)  
- Converting protein back to possible DNA sequences  
- Adding mutation detection features  

## Conclusion

This project represents a step forward from simple scripts to building structured bioinformatics tools. It combines programming logic with biological understanding and serves as a foundation for more advanced bioinformatics applications.

## Date
14 April 2026
