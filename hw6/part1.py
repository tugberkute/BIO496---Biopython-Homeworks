import re

mtfs = {"BCL6": "[TA].CTTTC.AGG[AG]AT", "SP1": "[GT]GGGCGG[GA][GA][CT]",
        "AP1": "TGA[GC]TCA", "NF-I": "TTGGC.{5}GCCAA"}

with open("prom_seqs.txt") as infh:
    with open("Hw5_TuğberkÜte_output.txt", "w") as infile:
        infile.write("TF_name\tTranscriptID\t#recog_sites\tseq_recog_site\tstart\tend\n")  # opens a new Hw5_TuğberkÜte_output.txt file and prints the headlines in the first line
        for line in infh:
            transcript_name, sequence = line.strip("\t").split("\t")  # gets trancripts IDs and their sequences from splitted list in prom_seqs.txt
            for motif in mtfs.keys():
                match_object = re.search(mtfs[motif], sequence)
                if match_object is not None:  # if there is no match, match_object returns None and following code raises an error, so in order to solve this: if/else
                    start, end = match_object.span()
                    seq_recog_site = match_object.group()
                    number_of_rec_sites = len(re.findall(mtfs[motif], sequence))
                    print(f"{motif}\t{transcript_name}\t{number_of_rec_sites}\t{seq_recog_site}\t{start}\t{end}\n", end="", file=infile)  # prints the matched sequence information on Hw5_TuğberkÜte_output.txt file
                else:
                    continue
