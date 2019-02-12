RNAfile = open('rosalind_rna.txt', 'r')
RNA = RNAfile.readline()
RNAfile.close()

print(RNA.replace('T','U'))