def calc(op1, op2, op):
     if op == '+':
        return op1 + op2
     elif op == '-':
        return op1 - op2
     elif op == '*':
        return op1 * op2
     elif op == '/':
        return op1 / op2

cont = 'y'
while cont != 'n':
    print("Enter the first number:")
    num1 = int (input())
    print("Enter the second number:")
    num2 = int (input())
    print("Enter operation:")
    op = raw_input()
    if op == '/' and num2 == 0:
      print("cannot divide by zero.")
      continue
    else:
        print(calc(num1, num2, op))
