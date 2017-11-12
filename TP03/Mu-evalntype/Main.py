from MuLexer import MuLexer
from MuParser import MuParser
from MyMuVisitor import MyMuVisitor, MuRuntimeError, MuSyntaxError
from MyMuTypingVisitor import MyMuTypingVisitor, MuTypeError

import argparse
import antlr4

# Main file for Lab3, MIF08, nov 2017

enable_typing = True


def main():
    # command line
    parser = argparse.ArgumentParser(description='Exec/Type mu files.')
    parser.add_argument('path', type=str,
                        help='file to exec and type')
    args = parser.parse_args()

    # lex and parse
    input_s = antlr4.FileStream(args.path, encoding='utf8')
    lexer = MuLexer(input_s)
    stream = antlr4.CommonTokenStream(lexer)
    parser = MuParser(stream)
    tree = parser.prog()

    # typing Visitor - This is given to you
    if enable_typing:
        visitor1 = MyMuTypingVisitor()
        try:
            visitor1.visit(tree)
        except MuTypeError as e:
            print(e.args[0])
            exit(1)

    # eval Visitor - You have some TODOS in this file!
    visitor2 = MyMuVisitor()
    try:
        visitor2.visit(tree)
    except (MuRuntimeError, MuSyntaxError) as e:
        print(e.args[0])
        exit(1)

if __name__ == '__main__':
    main()
