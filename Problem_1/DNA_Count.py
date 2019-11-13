class NucCount (str):
    """
    Counts the amount of nucleotides in the given DNA sequence.
    """
    def parse(self, DNAseq):
        '''Count each nucleotide.'''
        A = DNAseq.count('A')
        C = DNAseq.count('C')
        G = DNAseq.count('G')
        T = DNAseq.count('T')
        print (A, C, G, T)

def main ():
    '''Ask the user for a sequence'''
    DNAseq = input('Input DNA sequence:')
    newSeq = NucCount()
    newSeq.parse(DNAseq)

main()