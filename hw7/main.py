class Transcript:
    gene_dict = {}  # class variable that stores the gene id and instances of transcripts

    def __init__(self, transcriptID, chrNumber, exonNumber, strand, geneName, exonStarts, exonEnds):
        self.transcriptID = transcriptID
        self.chrNumber = chrNumber
        self.exonNumber = int(exonNumber)
        self.strand = strand
        self.geneName = geneName
        self.exonStarts = list(map(int, exonStarts.split(",")[:-1]))  # turns every element in the list to integer
        self.exonEnds = list(map(int, exonEnds.split(",")[:-1]))
        self.exonPairs = []

        # if the current gene is not in the dictionary, creates a list for the gene and appends the current instance
        if geneName not in Transcript.gene_dict:
            Transcript.gene_dict[geneName] = []
            Transcript.gene_dict[geneName].append(self)
        else:
            Transcript.gene_dict[geneName].append(self)

    # creates a list of exon end and exon start pairs as tuples
    def exonPairsCreator(self):
        for exon_starts, exon_ends in zip(self.exonStarts, self.exonEnds):
            exon_pairs = (exon_starts, exon_ends)
            self.exonPairs.append(exon_pairs)
        return self.exonPairs

    # calculates the transcript length for the current instance
    def txLength(self):
        total_tx_length = 0
        for exon in self.exonPairs:
            tx_length = exon[1] - exon[0] + 1
            total_tx_length += tx_length
        return total_tx_length

    # creates a list of transcripts for a given gene
    def txList(self):
        transcript_list = []
        for trans in Transcript.gene_dict[self.geneName]:
            transcript_list.append(trans.transcriptID)
        return transcript_list


def objectCreator(file_path):
    """
    Reads a line in the file that provided, and creates an instance for each transcript.
    :param file_path: file directory as string
    :return: Returns the class variable gene_dict dictionary that consists of key as gene and value as transcript instances
    """
    with open(file_path) as infh:
        for line in infh:
            if line.startswith("#"):
                continue
            boluk = line.strip().split("\t")
            Transcript(boluk[1], boluk[2], boluk[8], boluk[3], boluk[12], boluk[9], boluk[10])
        return Transcript.gene_dict


def outputCreator(transcript_id: str, gene_and_transcript_dict: dict, operation: str, input_file: str):
    """
    Creates output about the transcript that is taken from the user. Uses gene_dict dictionary to get the information about the transcripts.
    Based on user preference (operation parameter), it prints the output to the terminal or to a new file.
    """
    counter = 0  # counter to capture if the transcript from user is found in the dictionary
    for gene in gene_and_transcript_dict:
        for instance in gene_and_transcript_dict[gene]:
            if counter != 0:  # if the transcript from the user corresponds to the transcript from the dictionary, breaks the loop in order to not iterate unnecessarily
                break
            elif transcript_id == instance.transcriptID:
                counter = 1
                instance.exonPairsCreator()
                output = f"""Input File            : {input_file}
Transcript ID         : {instance.transcriptID}
Chromosome Number     : {instance.chrNumber}
Exon Number           : {instance.exonNumber}
Transcript Length     : {instance.txLength()}
Gene Name             : {instance.geneName}
Cousin Transcript IDs : {", ".join(instance.txList())}"""
                if operation.lower() == "file":
                    with open(f"{transcript_id}_summary.txt", "w") as f:
                        f.write(output)
                elif operation.lower() == "terminal":
                    print(output)
            else:
                continue


def main():
    my_user = input("Please provide me a file path: ")
    collection = objectCreator(my_user)
    trans_id = input("Please provide me the Transcript ID: ")
    while True:
        transcript_valid = False
        for gene, trans_list in collection.items():
            for trans in trans_list:
                if trans.transcriptID == trans_id:
                    transcript_valid = True
                    break
            if transcript_valid:
                break

        if transcript_valid:
            file_or_terminal = input("""If you want to print to output to terminal write 'terminal', or to a new file write 'file'.
Write 'exit' if you want to terminate the program: """)
            if file_or_terminal.lower() == "exit":
                exit()
            else:
                outputCreator(trans_id, collection, file_or_terminal, my_user)
                exit()
        else:
            trans_id = input("Transcript ID not found. Please provide another transcript: ")


main()
