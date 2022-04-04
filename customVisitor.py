import Pam_v2_gen_py3.Pam_v2Visitor
from Pam_v2_gen_py3.Pam_v2Parser import Pam_v2Parser


class CustomVisitor(Pam_v2_gen_py3.Pam_v2Visitor.Pam_v2Visitor):
    varList = {}

    def visitAssign_stmt(self, ctx: Pam_v2Parser.Assign_stmtContext):
        # print("ASSIGN - Children: " + str(ctx.getChildCount()))
        # print("Child 1: " + str(ctx.getChild(0)))
        # print("Child 2: " + str(ctx.getChild(1)))
        # print("Child 3: " + str(ctx.getChild(2)))
        value = 0

        if ctx.log_expr() is not None:
            value = self.visitLog_expr(ctx.getChild(2))

        if ctx.expr() is not None:
            value = self.visitExpr(ctx.getChild(2))

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

                if childVal0 in CustomVisitor.varList:
                    childVal0 = CustomVisitor.varList[childVal0]
                if childVal0 in CustomVisitor.varList:
                    childVal2 = CustomVisitor.varList[childVal2]

                return float(childVal0) + float(childVal2)
            else:
                childVal0 = str(self.visitTerm(ctx.getChild(0)))
                childVal2 = str(self.visitTerm(ctx.getChild(2)))

                if childVal0 in CustomVisitor.varList:
                    childVal0 = CustomVisitor.varList[childVal0]
                if childVal0 in CustomVisitor.varList:
                    childVal2 = CustomVisitor.varList[childVal2]

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

                if childVal0 in CustomVisitor.varList:
                    childVal0 = CustomVisitor.varList[childVal0]
                if childVal0 in CustomVisitor.varList:
                    childVal2 = CustomVisitor.varList[childVal2]

                return float(str(childVal0)) * float(str(childVal2))
            else:
                childVal0 = self.visitElem(ctx.getChild(0))
                childVal2 = self.visitElem(ctx.getChild(2))

                if childVal0 in CustomVisitor.varList:
                    childVal0 = CustomVisitor.varList[childVal0]
                if childVal0 in CustomVisitor.varList:
                    childVal2 = CustomVisitor.varList[childVal2]

                return float(str(childVal0)) / float(str(childVal2))

    def visitElem(self, ctx: Pam_v2Parser.ElemContext):
        # print("ElemChildren: " + str(ctx.getChildCount()))
        # print("----1ELEM: " + str(ctx.getChild(0)))
        # print("----2ELEM: " + str(ctx.getChild(1)))
        # print("----3ELEM: " + str(ctx.getChild(2)))

        if str(ctx.getChildCount()) == "1":     # NUMBER | VARNAME | BOOL
            return str(ctx.getChild(0))
        else:                                   # LPARENTHESIS expr RPARENTHESIS
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

            if str(self.visitLog_term(ctx.getChild(0))) in CustomVisitor.varList:
                childVal0 = str(CustomVisitor.varList[childVal0])
                if childVal0 == "True":
                    childVal0 = True
                else:
                    childVal0 = False
            elif str(self.visitLog_term(ctx.getChild(0))) == "True":
                childVal0 = True

            if str(self.visitLog_term(ctx.getChild(2))) in CustomVisitor.varList:
                childVal2 = str(CustomVisitor.varList[childVal2])
                if childVal2 == "True":
                    childVal2 = True
                else:
                    childVal2 = False
            elif str(self.visitLog_term(ctx.getChild(2))) == "True":
                childVal2 = True

            # print(str(childVal0) + " and " + str(childVal2))
            return childVal0 or childVal2

    def visitLog_term(self, ctx: Pam_v2Parser.Log_termContext):
        # print("LogTermChildren: " + str(ctx.getChildCount()))
        # print("----1TERM: " + str(self.visitLog_elem(ctx.getChild(0))))
        # print("----2TERM: " + str(self.visitLog_elem(ctx.getChild(1))))
        # print("----3TERM: " + str(self.visitLog_elem(ctx.getChild(2))))
        if str(ctx.getChildCount()) == "1":
            return str(self.visitLog_elem(ctx.getChild(0)))
        else:
            childVal0 = False
            childVal2 = False

            if str(self.visitLog_elem(ctx.getChild(0))) in CustomVisitor.varList:
                childVal0 = str(CustomVisitor.varList[str(self.visitLog_elem(ctx.getChild(0)))])
                if childVal0 == "True":
                    childVal0 = True
                else:
                    childVal0 = False
            elif str(self.visitLog_elem(ctx.getChild(0))) == "True":
                childVal0 = True

            if str(self.visitLog_elem(ctx.getChild(2))) in CustomVisitor.varList:
                childVal2 = str(CustomVisitor.varList[str(self.visitLog_elem(ctx.getChild(2)))])
                if childVal2 == "True":
                    childVal2 = True
                else:
                    childVal2 = False
            elif str(self.visitLog_elem(ctx.getChild(2))) == "True":
                childVal2 = True

            # print(str(childVal0) + " and " + str(childVal2))
            return childVal0 and childVal2

    def visitLog_elem(self, ctx: Pam_v2Parser.Log_elemContext):
        # print("LogElemChildren: " + str(ctx.getChildCount()))
        # print("----1LOGELEM: " + str(ctx.getChild(0)))
        # print("----2LOGELEM: " + str(ctx.getChild(1)))
        # print("----3LOGELEM: " + str(ctx.getChild(2)))
        # print("----4LOGELEM: " + str(ctx.getChild(3)))
        result = None
        if str(ctx.getChildCount()) == "1":     # BOOL | condition | VARNAME
            if ctx.condition() is not None:
                result = self.visitCondition(ctx.getChild(0))
            else:
                if str(ctx.getChild(0)) == "True":
                    result = True
                elif str(ctx.getChild(0)) == "False":
                    result = False
                else:
                    result = float(CustomVisitor.varList[ctx.getChild(0)])
        elif str(ctx.getChildCount()) == "2":   # NOT ( BOOL | condition | VARNAME )
            if ctx.condition() is not None:
                if str(self.visitCondition(ctx.getChild(1))) == "True":
                    result = False
                elif str(self.visitCondition(ctx.getChild(1))) == "False":
                    result = True
            else:
                if str(ctx.getChild(1)) == "True":
                    result = False
                elif str(ctx.getChild(1)) == "False":
                    result = True
                else:
                    result = float(CustomVisitor.varList[ctx.getChild(0)])
        elif str(ctx.getChildCount()) == "3":   # LPARENTHESIS log_expr RPARENTHESIS
            result = self.visitLog_expr(ctx.getChild(1))
        elif str(ctx.getChildCount()) == "4":   # NOT LPARENTHESIS log_expr RPARENTHESIS
            if str(self.visitLog_expr(ctx.getChild(2))) == "True":
                result = False
            else:
                result = True
        return result

    def visitCond_stmt(self, ctx: Pam_v2Parser.Cond_stmtContext):    # IF STATEMENT
        # print("CondChildren: " + str(ctx.getChildCount()))
        # print("----1COND: " + str(ctx.getChild(0)))
        # print("----2COND: " + str(self.visitLog_expr(ctx.getChild(1))))
        # print("----3COND: " + str(ctx.getChild(2)))
        # print("----4COND: " + str(self.visitSeries(ctx.getChild(3))))
        # print("----5COND: " + str(ctx.getChild(4)))
        # print("----6COND: " + str(self.visitSeries(ctx.getChild(5))))
        # print("----7COND: " + str(ctx.getChild(6)))

        ifCond = str(self.visitLog_expr(ctx.getChild(1)))
        if ifCond == "True":
            return self.visitSeries(ctx.getChild(3))
        elif str(ctx.getChildCount()) == "5":       # No "else" statement
            return
        elif str(ctx.getChildCount()) == "7":       # has "else" statement
            return self.visitSeries(ctx.getChild(5))

    def visitCondition(self, ctx: Pam_v2Parser.ConditionContext):   # expr RELATION expr
        # print("ConditionChildren: " + str(ctx.getChildCount()))
        # print("----1CONDIT: " + str(self.visitExpr(ctx.getChild(0))))
        # print("----2CONDIT: " + str(ctx.getChild(1)))
        # print("----3CONDIT: " + str(self.visitExpr(ctx.getChild(0))))

        if str(ctx.getChildCount()) == "0":
            print("ERROR?????????????????")
            print("RELATION: " + str(ctx.getChild(0)) + str(ctx.getChild(1)) + str(ctx.getChild(2)))
            return None

        childVal1 = str(ctx.getChild(1))

        if str(self.visitExpr(ctx.getChild(0))) in CustomVisitor.varList:
            childVal0 = float(CustomVisitor.varList[str(self.visitExpr(ctx.getChild(0)))])
        else:
            childVal0 = float(str(self.visitExpr(ctx.getChild(0))))

        if str(self.visitExpr(ctx.getChild(2))) in CustomVisitor.varList:
            childVal2 = float(CustomVisitor.varList[str(self.visitExpr(ctx.getChild(2)))])
        else:
            childVal2 = float(str(self.visitExpr(ctx.getChild(2))))

        print("RELATION: " + str(childVal0) + str(childVal1) + str(childVal2))

        if childVal1 == "<>":
            if childVal0 != childVal2:
                return True
            else:
                return False
        elif childVal1 == '=<':
            if childVal0 <= childVal2:
                return True
            else:
                return False
        elif childVal1 == '>=':
            if childVal0 >= childVal2:
                return True
            else:
                return False
        elif childVal1 == '=':
            if childVal0 == childVal2:
                return True
            else:
                return False
        elif childVal1 == '<':
            if childVal0 < childVal2:
                return True
            else:
                return False
        elif childVal1 == '>':
            if childVal0 > childVal2:
                return True
            else:
                return False
        else:
            return None
