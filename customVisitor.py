import Pam_v2_gen_py3.Pam_v2Visitor
from Pam_v2_gen_py3.Pam_v2Parser import Pam_v2Parser

class CustomVisitor(Pam_v2_gen_py3.Pam_v2Visitor.Pam_v2Visitor):
    varList = {}

    def visitAssign_stmt(self, ctx: Pam_v2Parser.Assign_stmtContext):
        # print("ASSIGN - Children: " + str(ctx.getChildCount()))
        # print("Child 1: " + str(ctx.getChild(0)))
        # print("Child 2: " + str(ctx.getChild(1)))
        # print("Child 3: " + str(ctx.getChild(2)))

        if ctx.expr() is not None:
            value = self.visitExpr(ctx.getChild(2))
        elif ctx.log_expr() is not None:
            value = self.visitLog_expr(ctx.getChild(2))
        else:
            return None

        CustomVisitor.varList[str(ctx.getChild(0))] = value
        return CustomVisitor.varList

    def visitExpr(self, ctx: Pam_v2Parser.ExprContext):
        # print("ExprChildren: " + str(ctx.getChildCount()))
        # print("--1EXPR: " + str(ctx.getChild(0)))
        # print("--2EXPR: " + str(ctx.getChild(1)))
        # print("--3EXPR: " + str(ctx.getChild(2)))

        if str(ctx.getChildCount()) == "1":
            return str(self.visitTerm(ctx.getChild(0)))
        else:
            if str(ctx.getChild(1)) == "+":
                childVal0 = str(self.visitTerm(ctx.getChild(0)))
                childVal2 = str(self.visitTerm(ctx.getChild(2)))
                return float(childVal0) + float(childVal2)
            else:
                childVal0 = str(self.visitTerm(ctx.getChild(0)))
                childVal2 = str(self.visitTerm(ctx.getChild(2)))
                return float(childVal0) - float(childVal2)

    def visitTerm(self, ctx: Pam_v2Parser.TermContext):
        # print("TermChildren: " + str(ctx.getChildCount()))
        # print("----1TERM: " + str(ctx.getChild(0)))
        # print("----2TERM: " + str(ctx.getChild(1)))
        # print("----3TERM: " + str(ctx.getChild(2)))

        if str(ctx.getChildCount()) == "1":
            return str(self.visitElem(ctx.getChild(0)))
        else:
            if str(ctx.getChild(1)) == "*":
                childVal0 = self.visitElem(ctx.getChild(0))
                childVal2 = self.visitElem(ctx.getChild(2))
                return float(str(childVal0)) * float(str(childVal2))
            else:
                childVal0 = self.visitElem(ctx.getChild(0))
                childVal2 = self.visitElem(ctx.getChild(2))
                return float(str(childVal0)) / float(str(childVal2))

    def visitElem(self, ctx: Pam_v2Parser.ElemContext):
        # print("ElemChildren: " + str(ctx.getChildCount()))
        # print("----1ELEM: " + str(ctx.getChild(0)))
        # print("----2ELEM: " + str(ctx.getChild(1)))
        # print("----3ELEM: " + str(ctx.getChild(2)))

        if str(ctx.getChildCount()) == "1":     # NUMBER | VARNAME | BOOL
            return str(ctx.getChild(0))
        else:                                   # LPARENTHESIS expr RPARENTHESIS
            # print("whyyyyyyyy")
            return self.visitExpr(ctx.getChild(1))

    def visitLog_expr(self, ctx: Pam_v2Parser.Log_exprContext):
        # print("LogExprChildren: " + str(ctx.getChildCount()))
        # print("----1EXPR: " + str(ctx.getChild(0)))
        # print("----2EXPR: " + str(ctx.getChild(1)))
        # print("----3EXPR: " + str(ctx.getChild(2)))
        if str(ctx.getChildCount()) == "1":
            return str(self.visitLog_term(ctx.getChild(0)))
        else:
            childVal0 = False
            childVal2 = False
            if str(self.visitLog_term(ctx.getChild(0))) == "True":
                childVal0 = True
            if str(self.visitLog_term(ctx.getChild(2))) == "True":
                childVal2 = True
            # print(str(childVal0) + " or " + str(childVal2))
            return childVal0 or childVal2

    def visitLog_term(self, ctx: Pam_v2Parser.Log_termContext):
        # print("LogTermChildren: " + str(ctx.getChildCount()))
        # print("----1TERM: " + str(ctx.getChild(0)))
        # print("----2TERM: " + str(ctx.getChild(1)))
        # print("----3TERM: " + str(ctx.getChild(2)))
        if str(ctx.getChildCount()) == "1":
            return str(self.visitLog_elem(ctx.getChild(0)))
        else:
            childVal0 = False
            childVal2 = False
            if str(self.visitLog_elem(ctx.getChild(0))) == "True":
                childVal0 = True
            if str(self.visitLog_elem(ctx.getChild(2))) == "True":
                childVal2 = True
            # print(str(childVal0) + " and " + str(childVal2))
            return childVal0 and childVal2

    def visitLog_elem(self, ctx: Pam_v2Parser.Log_elemContext):
        # print("LogElemChildren: " + str(ctx.getChildCount()))
        # print("----1ELEM: " + str(ctx.getChild(0)))
        # print("----2ELEM: " + str(ctx.getChild(1)))
        # print("----3ELEM: " + str(ctx.getChild(2)))
        if str(ctx.getChildCount()) == "1":     # BOOL | NOT BOOL | condition
            if str(ctx.getChild(0)) == "True":
                return True
            else:
                return False
        else:                                   # LPARENTHESIS log_expr RPARENTHESIS
            return self.visitLog_expr(ctx.getChild(1))
