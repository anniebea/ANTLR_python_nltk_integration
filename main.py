import sys

from grammarTree import *


def processProgr(argv, mode):
    prepTree(argv, mode)


def main(argv):
    processProgr(argv, "node")
    printGrammarTree(argv)

if __name__ == "__main__":
    main(sys.argv)
