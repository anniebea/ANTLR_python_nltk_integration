import Pam_v2_gen_py3.Pam_v2Listener
from Properties import *


class Interpreter(Pam_v2_gen_py3.Pam_v2Listener.Pam_v2Listener):
    propsObj = PropertyLoader()
    varsObj = VariableLoader()

    def printAllProps(self):
        # print all stored props
        print("ALL STORED PROPS:")
        print(Interpreter.propsObj.props)
        print("-----------------")

    def updateProp(self, key, value):
        Interpreter.propsObj.props[key] = value

    # Listener functions

    def enterProgr(self, ctx):
        print("In progr")

    def exitProgr(self, ctx):
        print("Out progr")

    def enterSeries(self, ctx):
        print("In series")

    def exitSeries(self, ctx):
        print("Out series")

    def enterStmt(self, ctx):
        print("In Stmt")

    def exitStmt(self, ctx):
        print("Out series")

    def enterAssign_stmt(self, ctx):
        print("In Assign_stmt")

    def exitAssign_stmt(self, ctx):
        if ctx.getChildCount() == 3:
            print("========================")
            left = ctx.getChild(0)
            right = ctx.getChild(2)
            print(str(right))
        print("Out Assign_stmt")

    def enterInput_stmt(self, ctx):
        print("In Input_stmt")

    def exitInput_stmt(self, ctx):
        print("Out Input_stmt")

    def enterOutput_stmt(self, ctx):
        print("In Output_stmt")

    def exitOutput_stmt(self, ctx):
        print("Out Output_stmt")

    def enterVarlist(self, ctx):
        print("In VarList")

    def exitVarlist(self, ctx):
        print("Out VarList")

    def enterCond_stmt(self, ctx):
        print("In Cond_stmt")

    def exitCond_stmt(self, ctx):
        print("Out Cond_stmt")

    def enterLoop(self, ctx):
        print("In loop")

    def exitLoop(self, ctx):
        print("Out loop")

    def enterLog_expr(self, ctx):
        print("In Log_expr")

    def exitLog_expr(self, ctx):
        print("Out Log_expr")

    def enterLog_term(self, ctx):
        print("In Log_term")

    def exitLog_term(self, ctx):
        print("Out Log_term")

    def enterLog_elem(self, ctx):
        print("In Log_elem")

    def exitLog_elem(self, ctx):
        print("Out Log_elem")

    def enterCondition(self, ctx):
        print("In Condition")

    def exitCondition(self, ctx):
        print("Out Condition")

    def enterNeg_condition(self, ctx):
        print("In Neg_condition")

    def exitNeg_condition(self, ctx):
        print("Out Neg_condition")

    def enterPos_condition(self, ctx):
        print("In Pos_condition")

    def exitPos_condition(self, ctx):
        print("Out Pos_condition")

    def enterExpr(self, ctx):
        print("In Expr")

    def exitExpr(self, ctx):
        print("Out Expr")

    def enterTerm(self, ctx):
        print("In Term")

    def exitTerm(self, ctx):
        print("Out Term")

    def enterElem(self, ctx):
        print("In Elem")

    def exitElem(self, ctx):
        print("Out Elem")
