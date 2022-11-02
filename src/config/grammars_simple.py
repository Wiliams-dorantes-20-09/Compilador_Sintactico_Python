def p_select_statement(p):
    '''select_statement : SELECT ID PLUS ID PYC'''
    pass

def p_error(p):
    print p
    if p:
        print("error de sintaxis en '%s'" % p.value)
    else:
        print("error de sintaxis en EOF")
