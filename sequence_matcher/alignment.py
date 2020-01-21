import sys
import Bio
from Bio.Seq import Seq
from .data_processing import get_proteins

def align(sequence):
    proteins = get_proteins()
    for protein in proteins:
        index = proteins[protein].find(sequence)
        if index > -1:
            return protein, index
    return '', -1