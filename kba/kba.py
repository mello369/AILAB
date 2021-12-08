combinations = [(True,True,True),(True,True,False),(True,False,False),(False,False,False),(False,False,True),(False,True,True)]
variables = {'p':0,'q':1,'r':2}
def main() :
    kb = input("Enter the rule")
    q = input("Enter the query")
    if entailment(kb,q) :
        print("Rule entails the query")
    else :
        print("Rule does not entail the query")

def entailment(kb,q) :
    print("Truth Table : ")
    print("Rule  Query")
    for comb in combinations :
        rule = evaluatePostfix(toPostfix(kb),comb)
        query = evaluatePostfix(toPostfix(q),comb)
        print(rule,query)
        if rule and not query :
            return False
    return True

def toPostfix(expr) :
    
def evaluatePostfix(expr,comb) :
    
