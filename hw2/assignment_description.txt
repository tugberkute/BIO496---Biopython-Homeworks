"""
--- PART 1 --- (0.25 pts)
In this assignment you will take a DNA sequence from the user and print if the sequence is a valid sequence or not
on the screen in the following format. Provide the user with the invalid character and its position for user's convenience.
If there are several invalid bases, display all of them.
---Ex for valid sequence:
Please type a DNA sequence: TGTGAGTATGCTAGC
This is a valid DNA sequence

---Ex for invalid sequence:
Please type a DNA sequence: TXGTCTYGACGGAC
X (base 2) is not a valid base.
Y (base 7) is not a valid base.
This is not a valid DNA sequence

Remember you can loop through strings in python as you do through a list. Check input's characters one by one.
You will be using 'for loop', 'if statement(s) and 'user input' for this assignment.
Always assume that user will make mistakes. They may not give you uppercase letters.
What can you do to make sure you handle lowercase letters? Implement a solution to your code.



--- PART 2 --- (0.75 pts)
You are going to write a program that contains at least four functions. You will take a DNA sequence from the user and
ask if he/she wants to calculate the reverse, complement or reverse-complement. You will print the answer on the screen.
Detailed explanation and requirements:
1- Ask the user for a DNA sequence. Check the validity of the sequence. Use your function in part 1.
   a) If the sequence is invalid. Print the invalid base/bases with their positions and ask no more.
   b) If the sequence is valid, the program will continue with the following.

2- Ask the user if s/he wants to print:
       1) Reverse-complement
       2) Complement
       3) Reverse
       Find a clever way to take the user input for this which would mitigate or completely avoid wrong inputs
       (asking the user to type "reverse-complement" without a typo is too optimistic.
       Instead ask them to type 1 (one) for reverse-complement, 2 for complement and 3 for reverse.
       You are going to write three functions: one to find the reverse of the given sequence,
       one to find the complement of the given sequence and one that uses your two functions together to find the
       reverse-complement of the given sequence. All of your functions should be 'fruitful'.
       Your code should work with lowercase letters and uppercase letters.
       Clearly state user's choice on the screen as well as the created sequence.
       All of your functions should have a docstring which clearly but briefly explains what the function does,
       information about the input(s) and the output(s). Google 'docstring' for more information.
       If the user gives an invalid input, give a warning message and do not calculate the anything.

ex:
DNA sequence: tcgactagc
Select the operation. Type:
1 for reverse-complement
2 for reverse
3 for complement
1
Reverse complement:
GCTAGTCGA


DNA sequence: tcgactagc
Select the operation. Type:
1 for reverse-complement
2 for reverse
3 for complement
2
Reverse:
CGATCAGCT

DNA sequence: tcgactagc
Select the operation. Type:
1 for reverse-complement
2 for reverse
3 for complement
3
Complement:
AGCTGATCG

DNA sequence: tcgactagcf
F (base 10) is not a valid base.
This is not a valid DNA sequence
"""
