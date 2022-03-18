import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from Pam_v2_gen_py3.Pam_v2Lexer import Pam_v2Lexer
from Pam_v2_gen_py3.Pam_v2Parser import Pam_v2Parser
import nltk


def main(argv):
    input = FileStream(argv[1])
    lexer = Pam_v2Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Pam_v2Parser(stream)
    tree = parser.progr()
    treeString = Trees.toStringTree(tree, None, parser)
    # Lai izvadītu koka String konsolē:
    print(treeString)
    # Lai izvadītu koka zīmējumu izlecošā logā:
    nltk.Tree.draw(nltk.Tree.fromstring(treeString))


if __name__ == "__main__":
    main(sys.argv)