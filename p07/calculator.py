
while True:
    print('\n'*2, "calculator [+ - * / ^] Exit: 'x'  ")
    action = input('action')
    if action == 'x':
        break
    elif  action not in ('+', '-', '*', '/', '^'):
        continue

    result = 0
    n1 = float(input('number 1:'))
    n2 = float(input('number 2:'))

    if action == '+':
        result = n1 + n2

    elif action == '-':
        result = n1 - n2

    elif action == '*':
        result = n1 * n2

    elif action == '/':
        if n2 == 0:
            print("You cant't do that")
        result = n1 / n2

    elif action == '^':
        result = n1 ** n2
    else:
        print("unknown command")

    print('Result =', result)

