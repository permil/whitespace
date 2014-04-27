import sys
import os

def makenum(num):
    ret = ' ' if num >= 0 else '\t'
    ret += format(abs(num), 'b').replace('0',' ').replace('1','\t')
    return ret

filename = raw_input('input file name > ')

f = open('out.ws', 'w')
for i,line in enumerate(open(os.path.join('src',filename), 'r')):
    out = ''
    commands = line.split()
    if len(commands) == 0: continue
    com = commands[0]
    if len(commands) > 1: num = makenum(int(commands[1]))

    if   com == 'PUSH': f.write('  ' + num + '\n')
    elif com == 'COPY': f.write(' \n ')
    elif com == 'SWAP': f.write(' \n\t')
    elif com == 'POP': f.write(' \n\n')
    elif com == 'ADD': f.write('\t   ')
    elif com == 'SUB': f.write('\t  \t')
    elif com == 'MUL': f.write('\t  \n')
    elif com == 'DIV': f.write('\t \t ')
    elif com == 'REM': f.write('\t \t\t')
    elif com == 'STORE': f.write('\t\t ')
    elif com == 'RETRIEVE': f.write('\t\t\t')
    elif com == 'LABEL': f.write('\n  ' + num[1:] + '\n')
    elif com == 'GOSUB': f.write('\n \t' + num[1:] + '\n')
    elif com == 'GOTO': f.write('\n \n' + num[1:] + '\n')
    elif com == 'IFZERO': f.write('\n\t ' + num[1:] + '\n')
    elif com == 'IFNEGATIVE': f.write('\n\t\t' + num[1:] + '\n')
    elif com == 'RETURN': f.write('\n\t\n')
    elif com == 'END': f.write('\n\n\n')
    elif com == 'PRINTC': f.write('\t\n  ')
    elif com == 'PRINT': f.write('\t\n \t')
    elif com == 'INPUTC': f.write('\t\n\t ')
    elif com == 'INPUT': f.write('\t\n\t\n')
    else: print("ERROR: Unknown statement '%s' in line %d" % (line, i))

