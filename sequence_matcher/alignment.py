import sys
import Bio
from Bio.Seq import Seq
from Bio import Entrez

class Genome():
    def __init__(self, genome_id):
        self.id = genome_id
        self.seq = self.get_annotation()
        self.proteins = self.find_proteins()

    def get_annotation(self):
        request = Entrez.epost("genome", id = self.id)
        print(self.id)
        try:
            result = Entrez.read(request)
        except RuntimeError as e:
            print("An error occurred while retrieving the annotations.")
            print("The error returned was ", e)
            # sys.exit(-1)
            return Seq('ATGCTGACTGTA')
        webEnv = result["WebEnv"]
        queryKey = result["QueryKey"]
        data = Entrez.esummary(db="nucleotide", webenv=webEnv, query_key = queryKey)
        annotation = Entrez.read(data)
        print(annotation)
        return data

    def find_proteins(self):
        # rna = self.seq.transcribe()
        return [Seq('TGCTG'), Seq('ATCGTTCGA'), Seq('ACCTCACTT')]

def align(sequence):
    genome_ids = ['NC_000852', 'NC_007346', 'NC_008724', 'NC_009899', 'NC_014637', 'NC_020104', 'NC_023423', 
                'NC_023640', 'NC_023719', 'NC_027867'] if len(sys.argv) < 3 else sys.argv[2:]
    # sequence = sys.argv[1]
    Entrez.email = "liza.bialik@gmail.com"
    genomes = [Genome(genome_id) for genome_id in genome_ids]
    for genome in genomes:
        for protein in genome.proteins:
            index = protein.find(sequence)
            if index > -1:
                return protein, index
    return '', -1

if __name__ == "__main__":
    genome_ids = ['NC_000852', 'NC_007346', 'NC_008724', 'NC_009899', 'NC_014637', 'NC_020104', 'NC_023423', 
                'NC_023640', 'NC_023719', 'NC_027867'] if len(sys.argv) < 3 else sys.argv[2:]
    sequence = sys.argv[1]
    Entrez.email = "liza.bialik@gmail.com"
    align(genome_ids, sequence)