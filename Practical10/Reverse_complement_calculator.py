
seq1 = input('please input the DNA sequence:')
# an example: 'AgcttTACG'

# Convert lowercase letters to uppercase letters
seq2 = seq1.upper()

# convert to reverse complement
s = ''
for i in range(len(seq2)):
    if seq2[i] == 'A':
        s += 'T'
    elif seq2[i] == 'G':
        s += 'C'
    elif seq2[i] == 'C':
        s += 'G' 
    elif seq2[i] == 'T':
        s += 'A' 
    else:
        print('This is an invalid sequence')
        break
print(s)
