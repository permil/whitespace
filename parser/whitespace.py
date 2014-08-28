import wsparse

filename = raw_input('input file name > ')
data = open(filename).read()
prog = wsparse.parse(data)
for line in prog:
  statement = line[0]
  if len(line) == 2:
    statement = statement + ' ' + str(line[1])
  print(statement)
