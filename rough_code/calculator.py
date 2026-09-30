def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations = {"+": add,"-": sub,"*": mult,"/": div}

def cal():
    should_do=True
    n1 = float(input("No. 1:"))

    while should_do:
        for symbols in operations:
            print(symbols)

        operation_symbol = (input("Which operation:"))

        n2 = float(input("No. 2:"))

        Answer = operations[operation_symbol](n1, n2)

        print(Answer)

        choose= input(f"move forward with same value {Answer} press 'y' or start over by pressing 'n' ")



        if choose== 'y' :
            n1=Answer

        else:
            should_do = False
            print("\n"*20)

            cal()
cal()




