"""
Universidade Federal de Mato Grosso - UFMT

Thales dos Santos Domingues
<ts.tkd2@gmail.com>

"""

from sintatico import Sintatico
from sys import argv

if __name__== "__main__":

    #nome = input("Entre com o nome do arquivo: ")
    nome = argv[1]
    parser = Sintatico(True)
    parser.interprete(nome)

    for i in range(len(argv)):
        if (argv[i] == '-t'):
            arquivo = open(argv[i+1], 'wt')
            tokens = []
            for token in parser.tokens:
                tokens.append(token.msg)
            arquivo.write(str(tokens))
