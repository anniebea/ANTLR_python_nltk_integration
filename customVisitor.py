import Pam_v2_gen_py3.Pam_v2Visitor
from Pam_v2_gen_py3.Pam_v2Parser import Pam_v2Parser

class CustomVisitor(Pam_v2_gen_py3.Pam_v2Visitor.Pam_v2Visitor):
    def visitAssign_stmt(self, ctx: Pam_v2Parser.Assign_stmtContext):
        print("Children: " + str(ctx.getChildCount()))
        print("Child 1: " + str(ctx.getChild(0)))
        print("Child 2: " + str(ctx.getChild(1)))
        print("Child 3: " + str(ctx.getChild(2)))

        return self.visitChildren(ctx)

    def visitExpr(self, ctx: Pam_v2Parser.ExprContext):
        print("ExprChildren: " + str(ctx.getChildCount()))
        print("Expr:" + str(self.visitElem(ctx.getChild(0))))
        result = str(self.visitElem(ctx.getChild(0)))
        return self.visitChildren(ctx)

    def visitTerm(self, ctx: Pam_v2Parser.TermContext):
        print("TermChildren: " + str(ctx.getChildCount()))
        print("Term:" + str(self.visitElem(ctx.getChild(0))))
        result = str(self.visitElem(ctx.getChild(0)))
        return result

    def visitElem(self, ctx: Pam_v2Parser.ElemContext):
        print("ElemChildren: " + str(ctx.getChildCount()))
        print("Elem:" + str(ctx.getChild(0)))
        elem = str(ctx.getChild(0))
        return elem
