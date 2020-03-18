from stack import Stack

def bubbleSort(values):
    for i in range(len(values)-1,0,-1):
        for j in range(i):
            if values[j] > values[j+1]:
                previous = values[j]
                values[j] = values[j+1]
                values[j+1] = previous

def main():
    mainStack = Stack()
    orderValues = []

    for i in range(5):
        values = int(input(f"Informe o valor {i + 1}: "))
        mainStack.push(values)

    for i in range((len(mainStack.getStack()))):
        orderValues.append(mainStack.pop())

    bubbleSort(orderValues)

    for i in range(len(orderValues)):
        mainStack.push(orderValues[i])


    print(f"Pilha ordenada: {mainStack.getStack()}")

main()