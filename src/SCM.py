import os
from libs.ply import lex
from libs.ply import yacc

Lexical = None
Parser = None

from config.reserved_words import reserved_words as reserved
from config.tokens_final import *
from config.tokens_re_final import *
from config.grammars_final import * 

class SCMCompiler:
    data = None
    lexer = None
    parser = None

    def __init__(self, src=None, print_tokens=False):
        self.src = src
        self.print_tokens = print_tokens

    def compile(self):
        if not self.eval_lexer():
            print "\n[ERROR]Analisis lexico con terminado con ERROR"
        else:
            print "\nAnalisis lexico terminado"
        if not self.eval_parser():
            print "Esto fallo"
        else:
            print "\nAnalisis Sintactico terminado"

    def eval_parser(self):
        if self.data:
            try:
                self.parser = yacc.yacc()
                global Parser
                Parser = self.parser
                self.parser.parse(self.data, tracking=True)
                return True
            except Exception, e:
                print "[ERROR]", e
                return False

    def eval_lexer(self):
        if not self.src:
            self.printer("Sin archivo de codigo")
            return False
        if not os.path.isfile(self.src):
            print "IOError: No existe el archivo: '{}'".format(self.src)
            return False
        f = open(self.src, 'r')
        self.data = f.read()
        f.close()
        self.lexer = lex.lex()
        self.lexer.input(self.data)
        while True:
            try:
                t = self.lexer.token()
                if not t:
                    self.printer("\n\tFinalizo. no mas tokens")
                    break
                self.printer("\tTipo: {}\t\ttoken: {}\tlinea {}\tposicion {}".format(t.type, t.value, t.lineno, t.lexpos))
            except Exception, e:
                print "[ERROR]:", e
                return False
        self.lexer.lineno = 1
        global Lexical
        Lexical = self.lexer
        return True

    def printer(self, text):
        if self.print_tokens:
            print text