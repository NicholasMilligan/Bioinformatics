class DNAtoRNA (str):
    """
    Converts DNA sequence to RNA sequence.
    """
    def transcribe(self, DNAseq):
        '''Convert Thymine to Uracil.'''
        RNAseq = DNAseq.replace('T', 'U')
        print (RNAseq)

def main():
    DNAseq = input('Input DNA sequence:')
    newSeq = DNAtoRNA()
    newSeq.transcribe(DNAseq)

main()