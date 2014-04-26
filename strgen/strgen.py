import sys

line = raw_input('> ')

sys.stdout = open('out.ws', 'w')
for c in line:
    sys.stdout.write('   ' + format(ord(c), 'b').replace('0',' ').replace('1','\t') + '\n\t\n  ')