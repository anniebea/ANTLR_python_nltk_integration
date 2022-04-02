import Pam_v2_gen_py3.Pam_v2Visitor
from Pam_v2_gen_py3.Pam_v2Parser import Pam_v2Parser

class CustomVisitor(Pam_v2_gen_py3.Pam_v2Visitor.Pam_v2Visitor):
    def visitAssign_stmt(self, ctx: Pam_v2Parser.Assign_stmtContext):
        # print("ASSIGN - Children: " + str(ctx.getChildCount()))
        # print("Child 1: " + str(ctx.getChild(0)))
        # print("Child 2: " + str(ctx.getChild(1)))
        # print("Child 3: " + str(ctx.getChild(2)))

        return self.visitExpr(ctx.getChild(2))

    def visitExpr(self, ctx: Pam_v2Parser.ExprContext):
        # print("ExprChildren: " + str(ctx.getChildCount()))
        # print("--1EXPR: " + str(ctx.getChild(0)))
        # print("--2EXPR: " + str(ctx.getChild(1)))
        # print("--3EXPR: " + str(ctx.getChild(2)))

        if str(ctx.getChildCount()) == "1":     # 'NUMBER | VARNAME | BOOL
            return str(self.visitTerm(ctx.getChild(0)))
        else:                                   # term (WEAKOP term)*;
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

        if str(ctx.getChildCount()) == "1":     # 'NUMBER | VARNAME | BOOL
            return str(self.visitElem(ctx.getChild(0)))
        else:                                   # elem (STRONGOP elem)*;
            if str(ctx.getChild(1)) == "*":
                childVal0 = self.visitElem(ctx.getChild(0))
                childVal2 = self.visitElem(ctx.getChild(2))
                return float(str(childVal0)) * float(str(childVal2))
            else:
                childVal0 = self.visitElem(ctx.getChild(0))
                childVal2 = self.visitElem(ctx.getChild(2))
                return float(str(childVal0)) / float(str(childVal2))

    def visitElem(self, ctx: Pam_v2Parser.ElemContext):     # Iet divus līmeņus dziļāk ,ja ir iekavas. Paskaidrojums ir šīs datnes apakšā
        # print("ElemChildren: " + str(ctx.getChildCount()))
        # print("----1ELEM: " + str(ctx.getChild(0)))
        # print("----2ELEM: " + str(ctx.getChild(1)))
        # print("----3ELEM: " + str(ctx.getChild(2)))

        if str(ctx.getChildCount()) == "1":     # 'NUMBER | VARNAME | BOOL
            return str(ctx.getChild(0))
        else:                                   # LPARENTHESIS expr RPARENTHESIS
            # print("whyyyyyyyy")
            return self.visitExpr(ctx.getChild(1))
