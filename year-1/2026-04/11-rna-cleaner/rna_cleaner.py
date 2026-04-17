# RNA Cleaner and RNA to DNA Converter

rna_input = str(input()).upper()
rna_seq = ""
for base in rna_input:
    if base in ["A","U","G","C"]:
        rna_seq += base
print(f"Original RNA : {rna_input}")
print(f"Clean RNA : {rna_seq}")

dna_seq = rna_seq.replace("U","T")
print(f"DNA sequence : {dna_seq}")
