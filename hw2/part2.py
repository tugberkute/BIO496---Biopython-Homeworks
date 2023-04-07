def validity_of_seq(dna_seq):
    """
    Takes a DNA sequence from the user. Checks if the given sequence is valid or not. If it is valid, program continues.
    If it is not, it prints a warning message and informs the user which base at what position is invalid.

    :param dna_seq: A DNA sequence from user.
    :return: If it is not valid, it prints a warning message.
    """
    capital_dna_seq = dna_seq.upper()
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


def complement(dna_seq):
    """
    Calculates the complementary base according to DNA sequence that is taken from the user. It gives the complement as
    a capitalized string.

    :param dna_seq: A DNA sequence from user.
    :return: Complement of the sequence
    """
    capital_seq = dna_seq.upper()
    complement = ""
    for base in capital_seq:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
    return complement


def reverse(dna_seq):
    """
    Reverses the DNA sequence that is taken from the user. It gives the reverse as a capitalized string.

    :param dna_seq: A DNA sequence from user.
    :return: Reverse of the sequence
    """
    capital_seq = dna_seq.upper()
    reverse = ""

    for base in range(-1, -len(capital_seq) - 1, -1):
        reverse += capital_seq[base]
    return reverse


def reverse_complement(dna_seq):
    """
    Calculates the complement of the reversed DNA sequence that is taken from the user. This function first calculates
    the reverse of the sequence, then takes its complement by using previous two functions. It gives the
    reverse-complement as a capitalized string.

    :param dna_seq: A DNA sequence from user.
    :return:Reverse-complement of the sequence
    """
    return complement(reverse(dna_seq))


def main():
    dna_sequence = str(input("Please enter a DNA sequence: "))
    validity_of_seq(dna_sequence)

    if len(invalid_bases) == 0:
        operation = input("Select for the operation: Type: \n1 for reverse-complement \n2 for reverse \n3 for complement\n")
        if operation == "3":
            print(complement(dna_sequence))
        elif operation == "2":
            print(reverse(dna_sequence))
        elif operation == "1":
            print(reverse_complement(dna_sequence))


invalid_bases = []
main()
