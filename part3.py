def base_frequency_calculator(dna_sequence: str):
    base_dictionary = {}
    for base in dna_sequence:
        if len(base_dictionary.keys()) == 4:
            break
        elif base in base_dictionary.keys():
            continue
        elif base not in base_dictionary.keys():
            base_dictionary[base] = dna_sequence.count(base)
    return base_dictionary

print(base_frequency_calculator(input()))