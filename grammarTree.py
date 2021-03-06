from antlr4 import *
from antlr4.tree.Trees import Trees

import customVisitor

from antlr_py3.Pam_v2Lexer import Pam_v2Lexer
from antlr_py3.Pam_v2Parser import Pam_v2Parser
import nltk

def prepTree(argv, returnVal):
    """
    Reads the user specified text document and formats its contents to a stringTree variable.
    :param returnVal: what the function should return
    :param argv: user specified text documents
    :return: stringTree of the inputFile text document
    """
    inputFile = FileStream(argv[1])
    dataFile = open(argv[2])
    num = 0
    for line in dataFile:
        for char in line:
            if char != ",":
                num = 10 * num + int(char)
            else:
                customVisitor.CustomVisitor.dataList.append(num)
                num = 0
    customVisitor.CustomVisitor.dataList.append(num)

    lexer = Pam_v2Lexer(inputFile)
    stream = CommonTokenStream(lexer)
    parser = Pam_v2Parser(stream)
    tree = parser.progr()   # progr - start rule
    treeString = Trees.toStringTree(tree, None, parser)
    treeString = treeString.replace("( ", "")
    treeString = treeString.replace(" )", "")

    # Visitor rules
    visitor = customVisitor.CustomVisitor()
    result = visitor.visit(tree)

    if returnVal == "treeString":
        return treeString
    elif returnVal == "tree":
        return tree
    else:
        return "hey - unspecified return value"

def printGrammarTree(argv):
    """
    Prints a stringTree object to terminal and creates a visual representation in a pop-up window
    :param argv: user specified text document
    :return: null
    """
    treeString = prepTree(argv, "treeString")
    # Lai izvadītu koka String konsolē:
    print(treeString)
    # Lai izvadītu koka zīmējumu izlecošā logā:
    nltk.Tree.draw(nltk.Tree.fromstring(treeString))
