from antlr4 import InputStream
from antlr4 import CommonTokenStream

# include to use the generated lexer and parser
from wfLexer import wfLexer
from wfParser import wfParser

import sys


def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = wfLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = wfParser(stream)
    parser.r()
    print("Finished")

# warns pb if py file is included in others
if __name__ == '__main__':
    main()
