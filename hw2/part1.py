dna_seq = str(input("Please enter a DNA sequence: "))
capital_dna_seq = dna_seq.upper()
invalid_bases = []
invalid_base_position = []
base_counter = 0

for base in capital_dna_seq:
    base_counter += 1
    if base not in ["A", "T", "C", "G"]:
        invalid_bases.append(base)
        invalid_base_position.append(base_counter)

if len(invalid_bases) >= 1:
    print("This is not a valid DNA sequence")
    for wrong_base in range(len(invalid_bases)):
        print(f"{invalid_bases[wrong_base]} (base {invalid_base_position[wrong_base]}) is not a valid base.")

else:
    print("This is a valid DNA sequence")
