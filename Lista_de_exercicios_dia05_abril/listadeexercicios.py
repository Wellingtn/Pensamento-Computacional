# ===Lista de exercicios===
#   Pensamento Computacional
#   Aluno:Wellington Juan
#   Semestre: 1º

# ===================================
# ===========Exercicio 1=============
# ===================================
graus_celsius = float(input('Digite a temperatura atual(em celsius): '))
fahrenheit = ((graus_celsius * 9)+160)/5
print(f'A temperatura em Fahrenheit é {fahrenheit}')

# ===================================
# ===========Exercicio 2=============
# ===================================
medida_pes = float(input('Digite a medida(pés): '))
metros = medida_pes * 0.304
centimetros = metros *100
print(f'a temperatura em metros é {metros:.2f} e em centimetros é {centimetros:.2f}')

# ===================================
# ===========Exercicio 3=============
# ===================================
red = '\033[31m'
green = '\033[32m'
yellow = '\033[7;49;33m'
reset = '\033[m'
def multiplo(a, b):
    if a % b ==0 or b % a ==0:
        return print(f'Os numeros digitados {green}são{reset} multiplos.')
    else:
        return print(f'Os numeros digitados {red}não{reset} são multiplos.')
print(f'''{'='*40}
        {yellow}Verificador de Multiplo{reset}
{'='*40}''')
a = int(input(f'Digite um valor inteiro:{green} '))
b = int(input(f'{reset}Digite outro valor inteiro:{green} '))
print(f'{reset}{'='*40}')
multiplo(a, b)

# ===================================
# ===========Exercicio 4=============
# ===================================
numero = float(input('Digite um numero : '))
if numero > 0:
    print('Esse numero é positivo.')
elif numero < 0:
    print('Esse numero é negativo.')
elif numero == 0:
    print('Esse número é nulo')

# ===================================
# ===========Exercicio 5=============
# ===================================
numero = int(input('Digite um numero inteiro: '))
if numero > 0:
    print(f'o inverso de {numero} é 1/{numero}(ou {1/numero:.4f})')
else:
    print(f'o absoluto de {numero} é {numero*-1}')

# ===================================
# ===========Exercicio 6=============
# ===================================
red = '\033[31m'
green = '\033[32m'
yellow = '\033[7;49;33m'
reset = '\033[m'
numero = int(input('Digite um numero inteiro: '))

if numero % 3 == 0 and numero % 7 ==0:
    print('O numero digitado é divisivel por 3 e por 7.')
else: 
    print('O numero não é divisivel por 3 e 7...')
print('===Extra===')
print('Os numeros divisiveis por 3 e 7 estao em verde...')

for cont in range(0,101):
    if cont % 3 ==0 and cont % 7 ==0:
        print(f'{green}{cont}{reset}', end=' ')
    else:
        print(f'{red}{cont}{reset}', end=' ')

# ===================================
# ===========Exercicio 7=============
# ===================================
numero = int(input('Digite um numero inteiro: '))
numero2 = int(input('Digite outro numero inteiro: '))
menor = 'o primeiro numero é menor' if numero < numero2 else 'o segundo numero é menor'
print(menor)

# ===================================
# ===========Exercicio 8=============
# ===================================
from time import sleep
red = '\033[31m'
green = '\033[32m'
reset = '\033[m'
numero = int(input('Digite um numero inteiro: '))
numero2 = int(input('Digite outro numero inteiro: '))
while True:
    escolha = int(input(f'''{'='*45}
    Escolha a Expressão aritmetica:
    [1]Soma
    [2]Subtração
    [3]Multiplicação
    [4]Divisão
    [5]Novos Valores
    [6]Sair
    Sua escolha: '''))

    match escolha:
        case 1:
            soma = numero + numero2
            print(f'{green}{numero} + {numero2} = {soma}{reset}')
        case 2:
            subtracao = numero - numero2
            print(f'{green}{numero} - {numero2} = {subtracao}{reset}')
        case 3:
            multi = numero * numero2
            print(f'{green}{numero} x {numero2} = {multi}{reset}')
        case 4:
            if numero2 == 0:
                print(f'{red}Impossivel dividir por 0!{green}')
            else:
                div = numero/numero2
                print(f'{green}{numero} / {numero2} = {div}{reset}')
        case 5:
            numero = int(input('Digite um novo primeiro numero:'))
            numero2 = int(input('Digite um novo segundo numero:'))
        case 6:
            break
print('ok, fechando o programa...')
for cont in range(3,-1,-1):
    sleep(0.5)
    print(cont)

# ===================================
# ===========Exercicio 9=============
# ===================================
a =int(input('Digite um valor qualquer: '))
b =int(input('Digite um valor qualquer: '))
c =int(input('Digite um valor qualquer: '))
abc = [a, b, c]
i =int(input(f'''Digite um dos valores abaixo:
[1] colocar a lista em ordem crescente
[2] colocar a lista em ordem decrescente
[3] colocar o maior numero no meio
{'='*45}
Digite aqui: '''))
match i:
    case 1:
        print(sorted(abc))
    case 2:
        print(sorted(abc, reverse = True))
    case 3:
        if b > a and b > c:
            print(a, b, c)
        elif a > b and a > c:
            print(b, a, c)
        elif c > a and c >b:
            print(a, c, b)
print('='*45)

# ===================================
# ===========Exercicio 10============
# ===================================
from math import sqrt
a = int(input('Qual o valor de a: '))
b = int(input('Qual o valor de b: '))
c = int(input('Qual o valor de c: '))
delta = (b**2) - 4*a*c
print('o delta é', delta)
if delta >= 0:
    if a > 0:
        print(f'({a})x^2 + ({b})x + ({c}) = 0')
        primeirox = (-(b)+ sqrt(delta))/(2*a)
        segundox = (-(b)- sqrt(delta))/(2*a)
        print(f'x1 = {primeirox:.2f} e x2 = {segundox:.2f}')
    elif a == 0:
        print(f'{b}x + {c} = 0')
        x = (c*-1)/b
        print(f'o valor de x é {x}')
else:
    print('o delta ou a variavel a é negativo, tente novamente...')

# ===================================
# ===========Exercicio 11============
# ===================================
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
#seleção simples
if x == 0:
    print('o ponto está sobre o eixo x.')
elif y == 0:
    print('o ponto está sobre o eixo y.')
elif x == 0 and y == 0:
    print('o ponto está sobre a origem.')
elif x > 0 and y > 0:
    print('o ponto está o primeiro quadrante.')
elif x < 0 and y > 0:
    print('o ponto está o segundo quadrante.')
elif x < 0 and y < 0:
    print('o ponto está o terceiro quadrante.')
elif x > 0 and y < 0:
    print('o ponto está o quarto quadrante.')

#seleçao aninhada
if x == 0:
    print('o ponto está sobre o eixo x.')
elif y == 0:
    print('o ponto está sobre o eixo y.')
elif x == 0 and y == 0:
    print('o ponto está sobre a origem.')
else:
    if x > 0 and y > 0:
        print('o ponto está o primeiro quadrante.')
    elif x < 0 and y > 0:
        print('o ponto está o segundo quadrante.')
    elif x < 0 and y < 0:
        print('o ponto está o terceiro quadrante.')
    elif x > 0 and y < 0:
        print('o ponto está o quarto quadrante.')

# ===================================
# ===========Exercicio 12============
# ===================================
if (condição1):
    if (condição2):
        if (condição3):
            comando1;
    else:
        comando2;
else:
    comando3;
