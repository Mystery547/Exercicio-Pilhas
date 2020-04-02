from stack import Stack

def hexadecimal(num):
    values = ['A', 'B', 'C', 'D', 'E', 'F']
    if num == 10:
        num = values[0]
    elif num == 11:
        num = values[1]
    elif num == 12:
        num = values[2]
    elif num == 13:
        num = values[3]
    elif num == 14:
        num = values[4]
    elif num == 15:
        num = values[5]
    return num

def main():
    number = int(input("Forneça um número: "))
    mainStack = Stack()
    copyStack = Stack()
    hexaStack = Stack()

    if number >= 2 and number <= 9:
        while number > 0:
            newNum = number // 2
            mainStack.push(number % 2)
            number = newNum
    elif number >= 11 and number <= 27:
        while number > 0:
            newNum = number // 16
            mainStack.push(hexadecimal(number % 16))
            copyStack.push(hexadecimal(number % 16))
            number = newNum

    for i in range(len(copyStack.getStack())):
        hexaStack.push(copyStack.pop())

    if len(hexaStack.getStack()) > 0:
        print(hexaStack.getStack())
    else:
        print(mainStack.getStack())

main()
