# nome = input('Digite o nome do filme: \n')
# ano = int(input ('Digite o ano do lançamento: \n'))
# nota = float(input ('Digite a nota do filme: \n'))

# 1 - Verifica se o filme é recomendado

# if nota > 8.0 and ano > 2015:
#     print (f'O filme {nome} é muito bom! Recomendo assisti-lo')
# else:
#     print (f'Procure outro filme, esse tem a nota {nota}. E o ano é de {ano}. Ou seja, não recomendo!')

num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
operacao = input('Digite a operacao a ser realizada:(+ - * / \n)')
result = float()

if operacao == '+':
    result = num1 + num2
elif operacao == '-':
    result = num1 - num2
elif    operacao == '*':
    result = num1 * num2
elif operacao == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print ('Erro divisão por Zero')
        result = 0
else:
    print ('Operação inválida')
    result = 0
print (f'Resultado da operação é: {result:.2f}')