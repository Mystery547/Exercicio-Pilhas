from stack import Stack
from queue import Queues

def optionA():
    mainStack = Stack()
    mainList = []
    addtionalStack = Stack()

    print("Forneça cinco valores")

    for i in range(5):
        values = input(f"Insira o valor {i+1}: ")
        mainStack.push(values)

    for i in range(len(mainStack.getStack())):
        mainList.append(mainStack.pop())

    for i in range(len(mainList)):
        addtionalStack.push(mainList.pop())

    print(f"Valores adcionados em uma pilha adcional: {addtionalStack.getStack()}")

def optionB():
    mainStack = Stack()
    mainList = []
    mainQueue = Queues()

    print("Forneça cinco valores")

    for i in range(5):
        values = input(f"Insira o valor {i+1}: ")
        mainStack.push(values)

    for i in range(len(mainStack.getStack())):
        mainList.append(mainStack.pop())

    for i in range(len(mainList)):
        mainQueue.enterData(mainList.pop())

    print(f"Valores adcionados sem uma pilha adcional: {mainQueue.getQueue()}")

def main():
    option = input("Escolha a opção para organizar a pilha\n"
                   "Digite 'A' para organizar com uma pilha adcional\n"
                   "Digite 'B' para organizar sem uma pilha adcional\n"
                   "Digite o comando desejado: ")

    if option == 'A' or option == 'a':
        optionA()
        print("FIM DO PROGRAMA")
    elif option == 'B' or option == 'b':
        optionB()
        print("FIM DO PROGRAMA")
    else:
        print("Escolha um comando válido")
        main()

main()
