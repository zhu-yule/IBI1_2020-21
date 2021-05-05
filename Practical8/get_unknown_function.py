# read the file
import re
original = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')

# create a file called 'unknown_function.fa'
fhand = open('unknown_function.fa', 'w')

# handle file
line = next(original, '-1')
while True:
    if line.startswith('>'):
        if re.search(r'unknown function', line):     # extract all the genes of unknown function
            name = re.findall('gene:(\S+)', line)    # store gene name
            s = ''                                   # store gene sequence
            while True:
                line = next(original, '-1')
                if line.startswith('>') or (line == '-1'):   # if the line is about description, then quit
                    break
                line1 = line.replace('\n', '')       # if the line is gene sequence, then store.
                s = s + line1
            f = '>>' + name[0]
            fhand.write(f'{f:14}')           # output gene name
            fhand.write(str(int(len(s))))    # output gene length
            fhand.write('\n')
            fhand.write(s)
            fhand.write('\n')
        else:
            line = next(original, '-1')
    else:
        line = next(original, '-1')
    if line == '-1':
        break
print('unknown_function.fa')
original.close()
fhand.close()



