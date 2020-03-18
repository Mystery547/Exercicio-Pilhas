from stack import Stack

def main():
    play = True
    editor = Stack()

    print('-'*60)
    print('digite (fim) para encerrar o programa')
    print('digite # para apagar o último caracter digitado')
    print('digite @ para apagar tudo')
    print('-'*60)

    while play == True:

        character = input('Insira um caracter: ')
        command = input('#/@/fim: ')
        editor.push(character)

        if command == '@':
            editor.emptyStack()
        elif command == '#':
            editor.pop()
        elif command == 'fim':
            play = False

        print(editor.getStack())

main()