import sys

from grammarTree import *


def processProgr(argv, mode):
    prepTree(argv, mode)


def main(argv):
    # printGrammarTree(argv)
    processProgr(argv, "node")

if __name__ == "__main__":
    main(sys.argv)

"""
(progr (series (stmt (assign_stmt y := (expr (term (elem 3)) + (term (elem 4) * (elem ( (expr (term (elem 5)) - (term (elem ( (expr (term (elem 3)) + (term (elem 2)) - (term (elem 1))) )))) ))))))))


(progr 
    (series 
        (stmt 
            (assign_stmt y := 
                (expr 
                    (term 
                        (elem 3)
                    ) 
                    + 
                    (term 
                        (elem 4) 
                        * 
                        (elem 
                            ( 
                                (expr 
                                    (term 
                                        (elem 5)
                                    ) 
                                    - 
                                    (term 
                                        (elem 
                                            ( 
                                                (expr 
                                                    (term 
                                                        (elem 3)
                                                    ) 
                                                    + 
                                                    (term 
                                                        (elem 2)
                                                    ) 
                                                    - 
                                                    (term 
                                                        (elem 1)
                                                    )
                                                )
                                             )
                                        )
                                    )
                                )
                             )
                        )
                    )
                )
            )
        )
    )
)
"""