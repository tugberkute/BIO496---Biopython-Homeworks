dna_seq = "ATGCGTACCGTAATGCTAGCTAGCTAGCTAGTGATAATTTGA"
start = "ATG"
stop = ["TAA", "TGA", "TAG"]
print([i for i in range(len(dna_seq)) if dna_seq.startswith(start, i)])
print([i for i in range(len(dna_seq)) if dna_seq.startswith(stop, i)])
codons = []
for i in range(0, len(dna_seq), 3):
    codon = dna_seq[i:i+3]
    codons.append(codon)
start_codons = []
stop_codons = []
counter = -1
for i in codons:
    counter += 1
    if i == "ATG":
        start_codons.append(counter)
    elif i in ["TAA", "TGA", "TAG"]:
        stop_codons.append(counter)