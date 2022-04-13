# Generated from C:/Users/anitr/OneDrive/Documents/__University/6sem/PVSUS/antlr_interpretor\Pam_v2.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Pam_v2Parser import Pam_v2Parser
else:
    from Pam_v2Parser import Pam_v2Parser

# This class defines a complete generic visitor for a parse tree produced by Pam_v2Parser.

class Pam_v2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Pam_v2Parser#progr.
    def visitProgr(self, ctx:Pam_v2Parser.ProgrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#series.
    def visitSeries(self, ctx:Pam_v2Parser.SeriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#stmt.
    def visitStmt(self, ctx:Pam_v2Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:Pam_v2Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#input_stmt.
    def visitInput_stmt(self, ctx:Pam_v2Parser.Input_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#output_stmt.
    def visitOutput_stmt(self, ctx:Pam_v2Parser.Output_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#varlist.
    def visitVarlist(self, ctx:Pam_v2Parser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#cond_stmt.
    def visitCond_stmt(self, ctx:Pam_v2Parser.Cond_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#loop.
    def visitLoop(self, ctx:Pam_v2Parser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#log_expr.
    def visitLog_expr(self, ctx:Pam_v2Parser.Log_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#log_term.
    def visitLog_term(self, ctx:Pam_v2Parser.Log_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#log_elem.
    def visitLog_elem(self, ctx:Pam_v2Parser.Log_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#condition.
    def visitCondition(self, ctx:Pam_v2Parser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#expr.
    def visitExpr(self, ctx:Pam_v2Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#term.
    def visitTerm(self, ctx:Pam_v2Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Pam_v2Parser#elem.
    def visitElem(self, ctx:Pam_v2Parser.ElemContext):
        return self.visitChildren(ctx)



del Pam_v2Parser