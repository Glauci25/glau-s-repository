# 1 - Faça um programa em linguagem Python que converta metros para centímetros.
n = int(input('Escreva um número em metros para conversão em centímetros: '))
cent = n*100
print(n, ' metros equivale a ', cent, ' centímetros.')

# 2 - Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.
valor = int(input('Digite um valor para ver a tabuada: '))
i = 0
while (i <= 9):
    i += 1
    print(valor, ' x ', i,' = ', valor*i)
    
# Faça um algoritmo em linguagem Python que receba duas notas, calcule a média aritmética e mostre o resultado.
n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
media = (n1 + n2)/2
print ('A média é: ', media)

#Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário reajustado de acordo com a tabela abaixo: 
# Abaixo de 500 --> 15% / De 500 até 1000 --> 10% / Acima de 1000 --> 5%
salario_atual = int(input('Qual o seu salário atual (R$)? '))
if salario_atual < 500:
    salario_novo = salario_atual*1.15
    print('Seu salário novo é R$', salario_novo, '.')
elif (salario_atual >= 500) and (salario_atual <= 1000):
    salario_novo = salario_atual*1.10
    print('Seu salário novo é R$', salario_novo, '.')
else:
    salario_novo = salario_atual * 1.05
    print('Seu salário novo é R$', salario_novo, '.')

# Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência.
i = 5
while (i <= 100):
    i += 1
    
    if (i % 7 == 0) and (i != 35) and (i != 70):
        print(i)
 
#Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.
n = int(input('Digite um número: '))
if n > 0:
    print("Número positivo.")
elif n == 0:
    print('Número neutro.')
else:
    print('Número negativo.')
 
#Crie um algoritmo que receba um número, conte o número total de dígitos e mostre o resultado. Por exemplo, se o número é 2021 , então a saída deve ser 4. 
n = input('Digite um número: ')
print(len(n))
