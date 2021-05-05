
import re
seq = 'ATGCGACTACGATCGAGGGCC'

# record genetic code
code = {
    "TTT":'F', "TTC":'F', "TTA":'L', "TTG":'L',
    "TCT":'S', "TCC":'S', "TCA":'S', "TCG":'S',
    "TAT":'Y', "TAC":'Y', "TAA":'O', "TAG":'U',
    "TGT":'C', "TGC":'C', "TGA":'X', "TGG":'W',
    "CTT":'L', "CTC":'L', "CTA":'L', "CTG":'L',
    "CCT":'P', "CCC":'P', "CCA":'P', "CCG":'P',
    "CAT":'H', "CAC":'H', "CAA":'Q', "CAG":'Z',
    "CGT":'R', "CGC":'R', "CGA":'R', "CGG":'R',
    "ATT":'I', "ATC":'I', "ATA":'J', "ATG":'M',
    "ACT":'T', "ACC":'T', "ACA":'T', "ACG":'T',
    "AAT":'N', "AAC":'B', "AAA":'K', "AAG":'K',
    "AGT":'S', "AGC":'S', "AGA":'R', "AGG":'R',
    "GTT":'V', "GTC":'V', "GTA":'V', "GTG":'V',
    "GCT":'A', "GCC":'A', "GCA":'A', "GCG":'A',
    "GAT":'D', "GAC":'D', "GAA":'E', "GAG":'E',
    "GGT":'G', "GGC":'G', "GGA":'G', "GGG":'G',
     }

#The codon in the sequence is extracted in units of 3
seq1 = re.findall(r'...', seq)

#translate the sequence into protein
peptide = ''
for i in range(len(seq1)):
    peptide = peptide + code[seq1[i]]
print(peptide)
