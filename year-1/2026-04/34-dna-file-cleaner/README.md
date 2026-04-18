# DNA File Cleaner (File I/O Practice)

This project reads DNA sequences from a text file, cleans them by removing invalid characters, and prints both the original and cleaned sequences. Each line in the file is treated as a separate DNA sequence. This simulates real-world bioinformatics workflows where sequence data is stored in files instead of being manually entered.

## What I Learned

- How to use File I/O in Python using `open()` and `with`
- Difference between `.read()` and reading line-by-line using `for line in file`
- Understanding file pointer behavior (why reading twice gives empty output)
- Importance of using `.strip()` to clean newline characters
- Importance of returning values from functions
- How to process multiple sequences from a file instead of single input
- Realization that mixing different file reading methods can break logic
- Debugging mistakes related to file handling and fixing them

## Problem I Faced and Fixed

❌ My Original Code
```py
with open("dna.txt","r") as f:
    f.read()
    dna_seq = f.read().upper()
    for line in f:
        line.strip("\n")
    clean_dna = dna_cleaner(dna_seq)
    print(f"Original : {dna_seq}")
    print(f"Cleaned : {clean_dna}")
```
**Problems in This Code**
1. Used `f.read()` twice
First read consumes entire file
Second read returns empty string
2. Mixed `.read()` with `for line in f`
File pointer already at end
3. Did not store `.strip()` in variable
`line.strip()` does nothing without any assignment   
✅ Fixed Code
```py
with open("dna.txt", "r") as f:
    for line in f:
        line = line.strip().upper()
        clean_dna = dna_cleaner(line)
        print(f"Original : {line}")
        print(f"Cleaned  : {clean_dna}\n")
```
## Conclusion

This project helped me understand how real data is handled in bioinformatics. Instead of manually entering sequences, I can now process multiple sequences from a file and clean them efficiently. This is my first step toward working with real biological datasets.

## Date
18 April 2026
