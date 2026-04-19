# DNA Mutation Detection from a File

This project reads two DNA sequences from a text file, cleans invalid characters, and compares them to detect mutations.

## What I Learned

- How to read data from files using `open()`
- Difference between `.readlines()` and `.read().splitlines()`
- How to handle DNA cleaning before analysis
- String comparison for mutation detection
- Importance of file structure in bioinformatics data
- Debugging file input issues

### ❌ Issue

Initially, the code used:  
```py
with open("dna.txt", "r") as f:
    lines = f.readlines()
```
But `print(lines)` showed only one line or unexpected behavior. Even though the file was correct, Python was not splitting it properly in the expected way.
```py
print(f"DNA1 : {clean_dna1}")
print(f"DNA2 : {clean_dna2}")
print(f"Mutation : {mutation}")
print(lines)
print(len(lines))
# OUTPUT
"""
DNA1 : A
DNA2 : T
Mutation : Mutation detected.
ATGCGTAXXCG

12
"""
```

✅ Final Working Solution
```py
with open("dna.txt", "r") as f:
    lines = f.read().splitlines()
```
`.read()` reads the entire file as a single string
`.splitlines()` properly splits it into a list of lines  
***It Shows***  
File handling is not just about reading data — it also depends on:
- File formatting
- Hidden newline characters
- Choosing the correct reading method for the task
```py
print(f"DNA1 : {clean_dna1}")
print(f"DNA2 : {clean_dna2}")
print(f"Mutation : {mutation}")
print(lines)
print(len(lines))
# OUTPUT
"""
DNA1 : ATGCGTACG
DNA2 : ATGAGTACG
Mutation : Mutation detected.
['ATGCGTAXXCG', 'vaTGAGTACG']
2
"""
```

## Date
19 April 2026
