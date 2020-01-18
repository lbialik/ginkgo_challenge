import sys
# import Bio
# from Bio.Seq import Seq

def align(argv):
    proteins = ['abc', 'cde', 'efghijkabc']
    sequence = argv[1]
    for protein in proteins:
        index = protein.find(sequence)
        if index > -1:
            return protein, index
    return None, -1

if __name__ == "__main__":
    print(align(sys.argv))