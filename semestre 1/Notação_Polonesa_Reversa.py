def calculo(oper, lista, lista2, i):
    global contador
    if not lista2:
        lista2.insert(0, f'{lista[i - 2]} {oper} {lista[i - 1]})')
        contador += 1
    else:
        lista2.append(f'{oper} {lista[i-2]})')
        contador += 1
    calcular(oper, lista, i)

def calcular(oper, lista, i):
    if oper == '+':
        soma = int(lista[i - 2]) + int(lista[i - 1])
        lista[i] = soma
        del lista[i - 1]
        del lista[i - 2]
    elif oper == '-':
        subt = int(lista[i - 2]) - int(lista[i - 1])
        lista[i] = subt
        del lista[i - 1]
        del lista[i - 2]
    elif oper == '*':
        mul = int(lista[i - 2]) * int(lista[i - 1])
        lista[i] = mul
        del lista[i - 1]
        del lista[i - 2]
    elif oper == '/':
        div = int(lista[i - 2]) / int(lista[i - 1])
        lista[i] = div
        del lista[i - 1]
        del lista[i - 2]

def operacao(lista, lista2):
    while len(lista) != 1:
        for i in range(len(lista)):
            if lista[i] == '+':
                oper = '+'
                calculo(oper, lista, lista2, i)
                break
            elif lista[i] == '-':
                oper = '-'
                calculo(oper, lista, lista2, i)
                break
            elif lista[i] == '*':
                oper = '*'
                calculo(oper, lista, lista2, i)
                break
            elif lista[i] == '/':
                oper = '/'
                calculo(oper, lista, lista2, i)
                break


def main():
    global contador
    lista = ['2', '1', '+', '9', '*']
    lista2 = []
    print(lista, end=' -> ')
    operacao(lista, lista2)
    print('(' * contador, end='')
    print(lista2[0], lista2[1], end=' ')
    print('=', lista[0])


#programa principal
contador = 0
main()