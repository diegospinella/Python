movieName = 'Top Gun'

'''string [inicio:fim] - índice comeca na posicao 0 | indice final - 1 (ele sempre descarta a ultima posicao.
Coloque sempre 1 a mais)'''

#1 - Buscar toda a string a partir da primeira posicao

print (movieName [0:6]) 

# 2 - Buscar a posicao 0 que é a letra T e vai até o sexto caracter que é a letra U.
print (movieName [:6])

#3 - Buscar a posicao 0 que é a letra T e vai até o sexto caracter que é a letra U.

print (movieName[:7]) #exibe até a última posicao

#4- Busca da terceira até a última posicao

print (movieName [2:])

''''
string [inicio:fim:passo]
índice comeca na posicao 0 | índice final -1 
passo - determina o incremento. Por padrao é o 1
'''

#4 - Muscar toda a string de 2 em 2 caracteres - n passei nem o inicial e nem o final

print (movieName [::2])

#5 - Buscar toda string no indice ímpar

print (movieName [1::2])

#6- inverter uma string de tras para frente
print (movieName [::-1])