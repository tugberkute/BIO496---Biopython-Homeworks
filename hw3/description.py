"""--- PART 1 --- (0.5 pts)
We are trying to write a program that translates given gene DNA sequence into a protein sequence.
You are going to write at least 4 new functions and your program is going to use them.

Functions of the program:
Please follow the instructions below and name your functions EXACTLY as I named:
1- DNA_validation(): Checks the DNA sequence for invalid bases. You can use your old function. It should return True or False.
2- start_codon_finder(): Looks for a start codon. It should return the position of the start codon in the sequence.
3- stop_codon_finder(): Looks for a stop codon. It should return the position of the stop codon in the sequence.
4- orf_finder(): Looks for the longest open reading frame. It should consider the + and - strands. It should look for all 3 frames.
It should return the frame value and boundries of longest ORF. You can use your old function for reverse-complemant.
5- translate(): Translates codons into amino acids. Returns aa sequence.

Structure of the program:
1- Take DNA sequence as user input. Ask user until s/he gives a valid one. Cover uppercase and lowercase sequences.
2- Check the length of the DNA sequence. Ask user until s/he gives a sequence longer than 300 bases.
3- If seq passes, give it into the orf_finder(), It will use your start_codon_finder and stop_codon_finder and searches
for all frames and +/- strands. If there is no start codon or no stop codon, program should give proper messages and exit.
4- If your seq passes that step, translate() functions converts your longest orf into the protein sequence and
prints the message.

--- PART 2 --- (0.25 pts)
Read a file given. It is a tab separated file that contains gene name and its DNA sequence.
Create a dictionary, put the information into a dictionary.
Construct the structure as follows:
my_dictionary = {"gene1": {"name": "Gene_name1",
                           "DNA_sequence": "ATGAATTATA....",
                           "DNA_sequence_length": 400,
                           "protein_sequence": "M...",
                           "protein_sequence_length": 105},
                 "gene2": {"name": "Gene_name2",
                           "DNA_sequence": "ATGAATTATA....",
                           "DNA_sequence_length": 400,
                           "protein_sequence": "M...",
                           "protein_sequence_length": 105},...}
Important Notes:
You are NOT allowed to create the template dictionary on your own.
Your code should create new key if it does not exist.
Your code does not have to check the validity of the DNA sequence. It will be tested with correct ones.

--- PART 3 --- (0.25 pts)
You are going to write a function called base_frequency_calculator().
This function takes a DNA sequence as input and retuns a dictionary containing the total numbers of each base in your sequence.
Bases should be keys and values are the numbers calculated by your code.
base_dictionary = {"A": value, "T": value, "C": value, "G": value}
You need to construct your code as follows:
Iterate through your sequence, add the key if it does not exist.
If there is already, update the value of that key.
Your code does not have to check the validity of the DNA sequence. It will be tested with correct ones. """