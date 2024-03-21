
def adicao (x, y):
    return x + y
def subtracao(x, y):
    return x - y
def mutiplicacao (x, y):
    return x * y
def divisao (x, y):
    return x / y

def pedir_entrada():
    num1 = float(input("digite o primeiro número: "))
    num2 = float(input("digite o segundo número: "))
    operacao = input("Digite qual operacao deseja realizar (+, -, *, /): ")
    return num1, num2, operacao

num1, num2, operacao = pedir_entrada()
num1 = int(num1)
num2 = int(num2)
if(operacao == "+"):
    print(num1, " + ", num2,"= " , adicao(num1, num2))
elif (operacao == "-"):
    print(num1, " - ", num2,"= " , subtracao(num1, num2))
elif(operacao == "*"):
    print(num1, " x ", num2,"= " , mutiplicacao(num1, num2))
elif(operacao == "/"):
    print(num1, " / ", num2,"= " , divisao(num1, num2))
else:
    print("Operação Inválida")
