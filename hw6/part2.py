genelist = ['GPR139 ', 'YAP1', 'RASGEF1B', 'PAH', 'PLCB2', 'GAPDH', 'SST']
lengthlist = [1613, 2393, 2277, 4122, 4616, 1875, 618]

"""wanted_dictionary_format = {'GPR139' : 1613, 'YAP1' : 2393, 'RASGEF1B' : 2277, 'PAH' : 4122, 
                               'PLCB2' : 4616, 'GAPDH' : 1875, 'SST' : 618}"""

my_dict = {}
for index in range(len(genelist)):
    my_dict[genelist[index]] = lengthlist[index]

while True:
    user_input = input("Please give a threshold number to find the genes whose length is greater than the threshold"
                       " (type 'exit' to terminate program): ")
    print()  # prints newline
    if user_input.lower() == "exit":
        exit()
    else:
        threshold = int(user_input)
        longer_genes = {}  # new dictionary with genes and their lengths longer than the user threshold
        for genes in my_dict.keys():
            if int(my_dict[genes]) > threshold:
                longer_genes[genes] = my_dict[genes]
            else:
                continue
        print(f"Genes whose length is greater than {threshold} are:")
        for gene in longer_genes:
            print(gene)
        print("Sum of their lengths:")
        print(sum(longer_genes.values()))
        print()  # prints newline
