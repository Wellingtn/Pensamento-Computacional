# ==========================================
#    TRABALHO DE PENSAMENTO COMPUTACIONAL
# ==========================================
#   Pensamento Computacional
#   Professor: Rhauani Weber Aita Fazul
#   Aluno: Wellington Juan
#   Semestre: 1º
print(f'''
{'='*47}
      TRABALHO DE PENSAMENTO COMPUTACIONAL
      Professor: Rhauani Weber Aita Fazul
      Aluno: Wellington Juan
      Semestre: 1º
{'='*47}
''')
while True:
    escolha= int(input('''Escolha uma das opções abaixo:
[1]Calculadora de aniversário
[2]Codigo Verificador de Cartão
[3]Calculadora de duração de um jogo
[4]Calculadora de Triangulos
[5]Sair
Digite sua opção aqui: '''))
    match escolha:
        case 1:
            print(f'''
{'='*47}
      Calculadora de aniversário
{'='*47}
''')
            print('Digite o dia do seu aniversário, logo após, o mes do seu aniversário:')
            dia_nasc = int(input('Informe o seu dia de nascimento: '))
            mes_nasc = int(input('Informe o seu mês de nascimento: '))

            print('Digite o dia atual, logo após, o mes atual:')
            dia_atual = int(input('Informe o dia atual: '))
            mes_atual = int(input('Informe o mês atual: '))

            if mes_nasc - mes_atual >= 0:# se a diferença de meses for positiva, então o proximo aniversário é no mesmo ano
                falta_meses = mes_nasc - mes_atual
            else:
                result = mes_nasc - mes_atual #a variavel result é criada só pra essa soma.
                falta_meses = 12 + (result)# se o mes atual > mes nasc, então result é negativo.
            
            if dia_nasc - dia_atual >= 0:# se a diferença de dias for positiva, então o aniversario é no mesmo mês
                falta_dias = dia_nasc - dia_atual
            else:
                falta_dias = ((dia_atual - 30)*-1) + dia_nasc
                falta_meses -= 1

            print(f'''seu aniversario = {dia_nasc}/{mes_nasc}
data atual = {dia_atual}/{mes_atual}
falta {falta_meses} meses e {falta_dias} dias para o seu aniversário''')
            if falta_dias == 0 and falta_dias == 0:

                print('Parabéns, hoje é seu aniversário!!')
                print('='*47)
        case 2:
            print(f'''
{'='*47}
      Codigo Verificador de Cartão
{'='*47}''')
            numero_cartao = int(input('Digite o numero de 4 digitos do cartão: '))

            milhar = numero_cartao // 1000 % 10 #irá dividir por mil, e depois obter o resto de outra divisão por 10
            centena = numero_cartao //100 % 10 
            dezena = numero_cartao //10 % 10
            unidade = numero_cartao //1 % 10
            
            result = (milhar * unidade)+(centena*dezena)
            verificador = result // 7
            print(f'o codigo verificador é {verificador}')
            print('='*47)
        case 3:
            print(f'''
{'='*47}
      Calculadora de duração de um jogo
{'='*47}''')
            hora_inicio_evento = int(input('Digite o horario inicial do evento(h): '))
            min_inicio_evento = int(input('Digite o minuto que irá começar o evento:'))
            hora_final_evento = int(input('Digite o horario final do evento(h): '))
            min_final_evento = int(input('Digite o minuto que irá terminar o evento:'))
            
            if hora_final_evento > hora_inicio_evento:
                duracao_horas= hora_final_evento - hora_inicio_evento
            elif hora_final_evento < hora_inicio_evento:
                result =  24 - hora_inicio_evento 
                duracao_horas = hora_final_evento + result

            if min_inicio_evento < min_final_evento :
                duracao_min = min_final_evento - min_inicio_evento
            elif min_inicio_evento > min_final_evento :
                result = min_inicio_evento - min_final_evento
                duracao_min = 60 - result
                duracao_horas -= 1
            print(f'o evento irá durar {duracao_horas} horas e {duracao_min} minutos')
            print('='*47)
        case 4:
            print(f'''
{'='*47}
      Calculadora de Triangulos
{'='*47}''')
            while True:
                escolha = int(input('''
Escolha entre as opções abaixo:
[1]Calcular a área de um triângulo
[2]Mostrar o tipo do triângulo
[3]Sair
Digite sua opção aqui: '''))
                match escolha:
                    case 1:
                        print(f'''
{'='*47}
      Calculadora de áreas de triângulos
{'='*47}''')
                        base_triangulo = int(input('Digite o valor da base do triângulo: '))
                        altura_triangulo = int(input('Digite a altura do triângulo: '))
                        if base_triangulo > 0 and altura_triangulo > 0:
                            area_triangulo = (base_triangulo*altura_triangulo)/2
                            print(f'A área do triangulo é {area_triangulo}')
                        else:
                            print('zero e numeros negativos são invalidos para calcular a área do triângulo')
                    case 2:
                        print(f'''
{'='*47}
      Tipo do triângulo
{'='*47}''')
                        lado1 = int(input('Digite o primeiro lado do triângulo: '))
                        lado2 = int(input('Digite o segundo lado do triângulo: '))
                        lado3 = int(input('Digite o terceiro lado do triângulo: '))

                        if lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
                            print('os lados digitados não formam um triângulo!')
                        else:
                            if  lado1 == lado2 == lado3:
                                print('esse triangulo é equilatero!')
                            elif lado1 == lado2 or lado2== lado3 or lado3 == lado1:
                                print('esse triangulo é isóceles!')
                            elif lado1 != lado2 != lado3:
                                print('esse triangulo é escaleno!')
                            if lado1 ** 2 == lado2**2 + lado3**2 or lado2 ** 2 == lado1**2 + lado3**2 or lado3 ** 2 == lado1**2 + lado2**2:
                                print('e também é um triângulo retângulo!')
                    case 3:
                        break
                    case _ :
                        print('opção invalida, tente novamente!')
            print('='*47)
        case 5:
            break
        case _:
            print('opção invalida, tente novamente!')
print('ok, fechando o programa...')
