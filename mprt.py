import re
from io import StringIO

import requests

from cons import read_fasta


def get_fasta_from_uniprot(uniprot_id):
    cmd = "https://www.uniprot.org/uniprot/{}.fasta".format(uniprot_id)
    return list(read_fasta(StringIO(requests.get(cmd).text)))[0]


def find_motif(fasta):
    motif = re.compile(r"N[^P][ST][^P]")
    motif_indices = set()
    for i in range(len(fasta)):
        area = fasta[i: i + 4]
        if re.match(motif, area):
            motif_indices.add(i + 1)
    return motif_indices


if __name__ == '__main__':
    with open('C:\\Users\\gvandestee\\Downloads\\rosalind_mprt.txt') as infile, open(
            "C:\\Users\\gvandestee\\Downloads\\rosalind_mprt.txt.output.txt", "w") as outfile:
        for uni in infile:
            uni = uni.strip()
            fasta = get_fasta_from_uniprot(uni)
            motif_positions = find_motif(fasta)
            if motif_positions:
                outfile.write(uni + '\n')
                outfile.write(' '.join(map(str, sorted(motif_positions))) + '\n')
