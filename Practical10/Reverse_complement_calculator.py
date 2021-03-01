
seq1 = input('please input the DNA sequence:')
# an example: 'AgcttTACG'

# Convert lowercase letters to uppercase letters
seq2 = seq1.upper()

# convert to reverse complement
s = ''
for i in range(len(seq2)):
    if seq2[i] == 'A':
        s = 'T' + s
    elif seq2[i] == 'G':
        s = 'C' + s
    elif seq2[i] == 'C':
        s = 'G' + s
    elif seq2[i] == 'T':
        s = 'A' + s
    else:
        print('This is an invalid sequence')
        break
print(s)