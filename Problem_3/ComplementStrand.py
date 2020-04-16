class ComplementStrand (str):
    """
    Creates the complement strand of a DNA string.
    """
    def complement(self, DNAstr):
        '''Reverse the string and complement the nucleotides.'''
        #AAAACCCGGT
        #ACCGGGTTTT
        comp = ""
        for i in DNAstr[::-1]:
            if i == 'A':
                comp+='T'
            elif i == 'T':
                comp+='A'
            elif i == 'C':
                comp+='G'
            elif i == 'G':
                comp+='C'
        print (comp)


def main():
    DNASeq = input('Input DNA Sequence: ')
    newComp= ComplementStrand()
    newComp.complement(DNASeq)

main()