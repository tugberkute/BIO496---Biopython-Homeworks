"""

--- PART I ---

Write a 'guessing game'. Write a code to create a random number between 1 and 100.
Ask the user to guess a number between 1 and 100.
If the user's guest is lower than the previously created random number
tell the user 'go lower', or 'go higher' if it is higher than the random number.
Keep asking the user until the user
makes a correct guess, in which case print
'Congratulations, it took you XX guesses to find it!' on the screen and exit
the program.


Example (random number is 42 for this example):

I have picked a number between 1 and 100. Make a guess: 50
Go lower: 25
Go higher: 40
Go higher: 45
Go lower: 42
Congratulations! It took you 5 guesses to find it!

Requirement: write at least 1 function in your code.

You can use the following code to generate the random number:

import random
rand_int = random.randint(1,101)



--- PART II ---

For the following assignment use the ensmbl_hg19.txt file.

Ask the user to enter the chromosome number and a threshold.
Calculate the number of transcripts on the given chromosome
with at least one exon whose length is greater than the
threshold as well as the average exon lengths of these

As an output, print the number you have calculated on the screen.

Example input:

Please enter chromosome number: 2
Please enter threshold value: 1200

Example output:

Chromosome 2 has 2 transcripts with at least one exon longer than 1200 bases.
ENST0000011111 average exon length is: YYYYY bases
ENST0000022222 average exon length is: ZZZZZ bases


Requirements:
1- Use at least one function that reads the file and
returns a dictionary with relevant information
2- Your script needs to work for X and Y chromosomes as well
3- If user gives you invalid input warn the user and ask again
    ex:
    Please enter chromosome number: Z
    Invalid entry. Please enter a valid chromosome number (1-22,X,Y):

    ex2:
    Please enter treshold value: nekibuki
    Invalid entry. Please enter an integer:

Hints:
1- Make sure your script works for small and capital letters (x, y, X and Y should work as inputs).
2- You can use enumerate function to navigate within two or more lists at the same time. Check karalama and the web
for examples.
3- Use the short ensmbl file (ensmbl_kisa.txt) to test your script first to save time.

"""