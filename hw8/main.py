import urllib.request

amino_acids = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '', 'TAG': '',
        'TGC': 'C', 'TGT': 'C', 'TGA': '', 'TGG': 'W'
    }
mtfs = {"BCL6": "[TA].CTTTC.AGG[AG]AT", "SP1": "[GT]GGGCGG[GA][GA][CT]",
        "AP1": "TGA[GC]TCA", "NF-I": "TTGGC.{5}GCCAA"}


def get_dna_seq(chrom, start, end):
    mystr = 'http://togows.org/api/ucsc/hg19/{}:{}-{}'.format(chrom, start, end)
    with urllib.request.urlopen(mystr) as response:
        html = response.read().decode("utf-8")
    return str(html)


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


class Transcript:
    gene_dict = {}  # class variable that stores the gene id and instances of transcripts

    def __init__(self, transcriptID, chrNumber, exonNumber, strand, geneName, exonStarts, exonEnds, txStart, txEnd, cdsStart, cdsEnd):
        self.transcriptID = transcriptID
        self.chrNumber = chrNumber
        self.exonNumber = int(exonNumber)
        self.strand = strand
        self.geneName = geneName
        self.exonStarts = list(map(int, exonStarts.split(",")[:-1]))  # turns every element in the list to integer
        self.exonEnds = list(map(int, exonEnds.split(",")[:-1]))
        self.exonPairs = []
        self.txStart = int(txStart)
        self.txEnd = int(txEnd)
        self.cdsStart = int(cdsStart)
        self.cdsEnd = int(cdsEnd)
        self.promoterSeq = ""
        self.CodingSeq = ""
        self.ProteinSeq = ""

        # if the current gene is not in the dictionary, creates a list for the gene and appends the current instance
        if geneName not in Transcript.gene_dict:
            Transcript.gene_dict[geneName] = []
            Transcript.gene_dict[geneName].append(self)
        else:
            Transcript.gene_dict[geneName].append(self)

    def exonPairsCreator(self):
        for exon_starts, exon_ends in zip(self.exonStarts, self.exonEnds):
            exon_pairs = (exon_starts, exon_ends)
            self.exonPairs.append(exon_pairs)
        return self.exonPairs

    def promoterSequenceFetcher(self):
        if self.strand == "+":
            self.promoterSeq = get_dna_seq(self.chrNumber, int(self.txStart) - 5000, self.txStart)
        else:
            self.promoterSeq = reverse_complement(get_dna_seq(self.chrNumber, int(self.txEnd), int(self.txEnd) + 5000))

    def codingSequenceFetcher(self):
        utr_found = False

        for exon_start, exon_end in self.exonPairs:
            if self.cdsStart == self.cdsEnd:
                self.CodingSeq = ""
            elif exon_start <= self.cdsStart < exon_end:
                utr_found = True
                self.CodingSeq += get_dna_seq(self.chrNumber, self.cdsStart + 1, exon_end)
                continue
            elif exon_start < self.cdsEnd <= exon_end:
                self.CodingSeq += get_dna_seq(self.chrNumber, exon_start + 1, self.cdsEnd)
                continue
            elif utr_found:
                self.CodingSeq += get_dna_seq(self.chrNumber, exon_start + 1, exon_end)
            else:
                continue
        if self.strand == "-":
            self.CodingSeq = reverse_complement(self.CodingSeq)

    def proteinSequence(self):
        codons = []
        for i in range(0, len(self.CodingSeq), 3):
            codon = self.CodingSeq[i:i + 3]
            codons.append(codon)
        for bases in codons:
            self.ProteinSeq += amino_acids[bases]


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
            Transcript(boluk[1], boluk[2], boluk[8], boluk[3], boluk[12], boluk[9], boluk[10], boluk[4], boluk[5], boluk[6], boluk[7])
        return Transcript.gene_dict


def outputCreator(args, gene_and_transcript_dict: dict,):
    """
    Creates output about the transcript that is taken from the user. Uses gene_dict dictionary to get the information about the transcripts.
    Based on given parameters, it prints protein sequence (str) or the given promoter is in the transcript or not (T or F), to the terminal.
    """
    transID = args.id
    tfName = args.promoter
    protein = args.protein
    counter = 0  # counter to capture if the transcript from user is found in the dictionary
    for gene in gene_and_transcript_dict:
        for instance in gene_and_transcript_dict[gene]:
            if counter != 0:  # if the transcript from the user corresponds to the transcript from the dictionary, breaks the loop in order to not iterate unnecessarily
                break
            elif transID == instance.transcriptID:
                counter += 1
                instance.exonPairsCreator()
                if protein:
                    instance.codingSequenceFetcher()
                    instance.proteinSequence()
                    return instance.ProteinSeq
                if tfName is not None:
                    import re
                    instance.promoterSequenceFetcher()
                    prom_seq = instance.promoterSeq
                    match_object = re.search(mtfs[tfName], prom_seq)
                    print(instance.promoterSeq)
                    if match_object is not None: return True
                    else: return False
            else:
                continue

    if counter == 0:
        return "Transcript not found!"


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-id', help='Transcript ID', type=str)
    parser.add_argument("-promoter", help="Whether given promoter is found in transcript or not", type=str)
    parser.add_argument("-protein", help="Gives the protein sequence", action="store_true")
    args = parser.parse_args()
    dictionary = objectCreator("ensembl_kisa.txt")

    print(outputCreator(args, dictionary))


main()
