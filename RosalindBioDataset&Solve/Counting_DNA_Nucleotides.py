Dnafile = open('rosalind_dna.txt', 'r')
DNA = Dnafile.readline()
Dnafile.close()

print(DNA.count("A"))
print(DNA.count("C"))
print(DNA.count("G"))
print(DNA.count("T"))