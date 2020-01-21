import os
import Bio
from Bio import Seq, SeqIO

def get_proteins():
    path = "../ginkgo/data"
    proteins = {}
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        with open(file_path, "r") as sequence_data:
            for index, record in enumerate(SeqIO.parse(sequence_data, "genbank")):
                seq = str(record.seq)
                for feature in record.features:
                    if feature.type == 'CDS':
                        proteins[feature.qualifiers['protein_id'][0]] = seq[feature.location.start:feature.location.end]
    return proteins