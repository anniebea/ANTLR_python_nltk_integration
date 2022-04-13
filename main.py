import sys

from grammarTree import *


def main(argv):
    # printGrammarTree(argv)
    prepTree(argv, "node")


if __name__ == "__main__":
    main(sys.argv)

"""
(progr 
    (series 
        (stmt 
            (cond_stmt if 
                (log_expr 
                    (log_term 
                        (log_elem True)
                    )
                ) 
                then 
                (series 
                    (stmt 
                        (assign_stmt x := 
                            (expr 
                                (term 
                                    (elem 12)
                                )
                            )
                        )
                    )
                ) 
                else 
                (series 
                    (stmt 
                        (assign_stmt x := 
                            (expr 
                                (term 
                                    (elem 11)
                                )
                            )
                        )
                    )
                ) 
                fi
            )
        ) 
        ; 
        (stmt 
            (cond_stmt if 
                (log_expr 
                    (log_term 
                        (log_elem not 
                            (condition 
                                (expr 
                                    (term 
                                        (elem x)
                                    )
                                ) 
                                > 
                                (expr 
                                    (term 
                                        (elem 10)
                                    )
                                )
                            )
                        )
                    )
                ) 
                then 
                (series 
                    (stmt 
                        (assign_stmt y := 
                            (log_expr 
                                (log_term 
                                    (log_elem False)
                                )
                            )
                        )
                    )
                ) 
                else 
                (series 
                    (stmt 
                        (assign_stmt y := 
                            (log_expr 
                                (log_term 
                                    (log_elem True)
                                )
                            )
                        )
                    ) 
                    ; 
                    (stmt 
                        (assign_stmt z := 
                            (log_expr 
                                (log_term 
                                    (log_elem False)
                                )
                            )
                        )
                    )
                ) 
                fi
            )
        )
    )
)
"""