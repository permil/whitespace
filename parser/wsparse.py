from ply import *
import wslex

tokens = wslex.tokens

precedence = ()

def p_program(p):
    '''program : program statement
               | statement'''

    if len(p) == 2 and p[1]:
      p[0] = [p[1]]
    elif len(p) ==3:
      p[0] = p[1]
      if not p[0]: p[0] = []
      if p[2]:
        p[0].append(p[2])

def p_program_error(p):
    '''program : error'''
    p[0] = None
    p.parser.error = 1

#### Format of all Whitespace statements.

def p_statement(p):
  '''statement : push num
               | dup
               | copy num
               | swap
               | pop
               | slide num
               | add
               | sub
               | mul
               | div
               | rem
               | store
               | retrieve
               | label string
               | gosub string
               | goto string
               | ifzero string
               | ifnegative string
               | return
               | end
               | printc
               | print
               | inputc
               | input'''
  if len(p) == 2:
    p[0] = (p[1],)
  else:
    p[0] = (p[1], p[2])

### commands ###
def p_command_push(p):
  '''push : SPACE SPACE'''
  p[0] = 'PUSH'

def p_command_dup(p):
  '''dup : SPACE LF SPACE'''
  p[0] = 'DUP'

def p_command_copy(p):
  '''copy : SPACE TAB SPACE'''
  p[0] = 'COPY'

def p_command_swap(p):
  '''swap : SPACE LF TAB'''
  p[0] = 'SWAP'

def p_command_pop(p):
  '''pop : SPACE LF LF'''
  p[0] = 'POP'

def p_command_slide(p):
  '''slide : SPACE TAB LF'''
  p[0] = 'SLIDE'

def p_command_add(p):
  '''add : TAB SPACE SPACE SPACE'''
  p[0] = 'ADD'

def p_command_sub(p):
  '''sub : TAB SPACE SPACE TAB'''
  p[0] = 'SUB'

def p_command_mul(p):
  '''mul : TAB SPACE SPACE LF'''
  p[0] = 'MUL'

def p_command_div(p):
  '''div : TAB SPACE TAB SPACE'''
  p[0] = 'DIV'

def p_command_rem(p):
  '''rem : TAB SPACE TAB TAB'''
  p[0] = 'REM'

def p_command_store(p):
  '''store : TAB TAB SPACE'''
  p[0] = 'STORE'

def p_command_retrieve(p):
  '''retrieve : TAB TAB TAB'''
  p[0] = 'RETRIEVE'

def p_command_label(p):
  '''label : LF SPACE SPACE'''
  p[0] = 'LABEL'

def p_command_gosub(p):
  '''gosub : LF SPACE TAB'''
  p[0] = 'GOSUB'

def p_command_goto(p):
  '''goto : LF SPACE LF'''
  p[0] = 'GOTO'

def p_command_ifzero(p):
  '''ifzero : LF TAB SPACE'''
  p[0] = 'IFZERO'

def p_command_ifnegative(p):
  '''ifnegative : LF TAB TAB'''
  p[0] = 'IFNEGATIVE'

def p_command_return(p):
  '''return : LF TAB LF'''
  p[0] = 'RETURNE'

def p_command_end(p):
  '''end : LF LF LF'''
  p[0] = 'END'

def p_command_printc(p):
  '''printc : TAB LF SPACE SPACE'''
  p[0] = 'PRINTC'

def p_command_print(p):
  '''print : TAB LF SPACE TAB'''
  p[0] = 'PRINT'

def p_command_inputc(p):
  '''inputc : TAB LF TAB SPACE'''
  p[0] = 'INPUTC'

def p_command_input(p):
  '''input : TAB LF TAB TAB'''
  p[0] = 'INPUT'

### for numbers and labels ###
def p_num(p):
  '''num : digits LF'''
  p[0] = p[1]

def p_digits(p):
  '''digits : digits SPACE
            | digits TAB
            |'''
  if len(p)==1:
    p[0] = 0
  elif len(p)==3:
    p[0] = p[1] * 2 if p[2] == ' ' else p[1] * 2 + 1

def p_string(p):
  '''string : chars LF'''
  p[0] = p[1]

def p_chars(p):
  '''chars : chars SPACE
           | chars TAB
           |'''
  if len(p)==1:
    p[0] = ''
  elif len(p)==3:
    if p[2] == ' ':
      p[0] = p[1] + '0'
    else:
      p[0] = p[1] + '1'

#### Catastrophic error handler
def p_error(p):
    if not p:
        print("SYNTAX ERROR AT EOF")

wsparser = yacc.yacc()

def parse(data,debug=0):
    wsparser.error = 0
    p = wsparser.parse(data,debug=debug)
    if wsparser.error: return None
    return p














