txt = str(input("Please write a sentence with min. 3 words: "))
not_space = True
splitted_text = []
loop_counter = -1
space_counter = 0
space_locations = []  # gives index for txt
a = ""

for i in txt:
    loop_counter += 1
    if i == " ":
        space_counter += 1
        space_locations.append(loop_counter)
        not_space = False
        splitted_text.append(a)
        a = ""

    else:
        not_space = True

    if not_space:
        a += i

splitted_text.append(a)

word_lengths = []

for i in splitted_text:
    length = len(i)
    word_lengths.append(int(length))

length_word = max(word_lengths)
index_of_longest_word = -1
longest_word = ""

for i in word_lengths:
    index_of_longest_word += 1
    if i == length_word:
        longest_word = splitted_text[index_of_longest_word]

print("The longest word is " + str(longest_word) + ", with the length of " + str(length_word) + " letters")
