def file_parser(file_name):
    chromosome_dict = {}

    with open(file_name) as infh:
        for line in infh:
            if line.startswith("#"):
                continue
            line_list = line.strip().split("\t")
            transcript_name = line_list[1]
            chr_num = line_list[2][3:]
            exon_count = line_list[8]
            exon_ends = list(map(int, line_list[10].split(",")[:-1]))
            exon_starts = list(map(int, line_list[9].split(",")[:-1]))
            transcript_dict = {f"{transcript_name}": {"Exon_count": exon_count,
                                                      "Exon_ends": exon_ends,
                                                      "Exon_starts": exon_starts}}
            if f"Chromosome {chr_num}" not in chromosome_dict:
                chromosome_dict[f"Chromosome {chr_num}"] = transcript_dict
            else:
                chromosome_dict[f"Chromosome {chr_num}"].update(transcript_dict)

    return chromosome_dict


def calculate_exon_lengths(chromosome, chr_dictionary):
    exon_lengths_dict = {}

    for transcript in chr_dictionary[f"Chromosome {chromosome}"].keys():
        exon_lengths = [e1 - e2 for (e1, e2) in zip(chr_dictionary[f"Chromosome {chromosome}"][transcript]["Exon_ends"],
                                                    chr_dictionary[f"Chromosome {chromosome}"][transcript][
                                                        "Exon_starts"])]

        exon_lengths_dict[f"{transcript}"] = exon_lengths
    return exon_lengths_dict


def find_above_threshold_in_chromosome(exon_len_dict, threshold):
    longer_count = 0
    longer_transcripts = {}
    for transcript in exon_len_dict.keys():
        for exon_len in exon_len_dict[transcript]:
            if exon_len > threshold:
                longer_count += 1
                average = sum(exon_len_dict[transcript]) // len(exon_len_dict[transcript])
                longer_transcripts[f"{transcript}"] = average
                continue
            else:
                continue
    return longer_transcripts


def main():
    chr_from_user = input("Please enter chromosome number: ")
    threshold = int(input("Please enter threshold value: "))
    longer_trans = find_above_threshold_in_chromosome(calculate_exon_lengths(chr_from_user.upper(), file_parser("ensembl_hg19.txt.")),
                                                            threshold)
    print(f"Chromosome {chr_from_user} has {len(longer_trans.keys())} transcripts at least one exon longer than 1200 bases.")
    for transcript in longer_trans.keys():
        print(f"{transcript} average exon length is: {longer_trans[transcript]} bases")


main()
