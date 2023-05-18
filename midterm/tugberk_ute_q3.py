def file_parser():  # parses the file with one name every line, returns the list of names.
    with open("names.txt") as infh:
        names_list = [line.strip("\n") for line in infh]
        return names_list


def name_counter(user_name: str, name_list: list):  # returns the number of occurrences of given input in the name list.
    return name_list.count(user_name)


def main():
    user_input = input("Please enter a name. We will search name in our file: ")
    match = name_counter(user_input, file_parser())
    print(f"There are {match} {user_input} in my file.")


main()
