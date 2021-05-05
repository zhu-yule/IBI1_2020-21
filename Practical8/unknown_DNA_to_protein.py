import re

# ask the user to input a filename as the new fasta file to be written to
name = input('Please input the file name: ')

# input the dictionary
table = {
    "TTT":'F',"TTC":'F',"TTA":'L',"TTG":'L',
    "TCT":'S',"TCC":'S',"TCA":'S',"TCG":'S',
    "TAT":'Y',"TAC":'Y',"TAA":'O',"TAG":'U',
    "TGT":'C',"TGC":'C',"TGA":'X',"TGG":'W',
    "CTT":'L',"CTC":'L',"CTA":'L',"CTG":'L',
    "CCT":'P',"CCC":'P',"CCA":'P',"CCG":'P',
    "CAT":'H',"CAC":'H',"CAA":'Q',"CAG":'Z',
    "CGT":'R',"CGC":'R',"CGA":'R',"CGG":'R',
    "ATT":'I',"ATC":'I',"ATA":'J',"ATG":'M',
    "ACT":'T',"ACC":'T',"ACA":'T',"ACG":'T',
    "AAT":'N',"AAC":'B',"AAA":'K',"AAG":'K',
    "AGT":'S',"AGC":'S',"AGA":'R',"AGG":'R',
    "GTT":'V',"GTC":'V',"GTA":'V',"GTG":'V',
    "GCT":'A',"GCC":'A',"GCA":'A',"GCG":'A',
    "GAT":'D',"GAC":'D',"GAA":'E',"GAG":'E',
    "GGT":'G',"GGC":'G',"GGA":'G',"GGG":'G',
     }

# define a function to translate the code into amino acid.
def translation(seq):
    a1 = re.findall(r'...', seq)
    amino = ''
    for i in range(len(a1)):
        a2 = table[a1[i]]
        amino += a2
    return amino

#create a new file
origin = open('unknown_function.fa', 'r')
fhand = open(name, 'w')
line = next(origin, '-1')
while True:
    if line.startswith('>>'):
        m = line
        line = next(origin, '-1')
        s = line.replace('\n', '')
        context = m[0:14] + str(int(len(s)/3))
        fhand.write(context)
        fhand.write('\n')
        fhand.write(translation(s))
        fhand.write('\n')
    if line == '-1':
        break
    line = next(origin, '0')
origin.close()
fhand.close()

