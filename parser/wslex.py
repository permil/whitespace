from ply import *

keywords = (
)

tokens = keywords + (
    'SPACE','TAB','LF'
)

t_ignore = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.1234567890' #TODO:

t_SPACE   = r'\s'
t_TAB     = r'\t'
t_LF      = r'\n'

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

lex.lex(debug=0)

















