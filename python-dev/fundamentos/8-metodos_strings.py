movieName =  'Top Gun'
movieDescription = '''
Top Gun Maverick é um filme
ante petista!
'''

print (movieName.upper()) # tudo maiusculo
print (movieName.lower()) # tudo minusculo
print (movieName.capitalize()) # deixar a primeira letra em maiscula
print (movieName.title()) # deixar a primeira de cada palavra como maiuscula
print (movieName.center(9, '-')) # retorna string centralizada com caractere de preencimento.
print (movieName.find ('u')) # retorna a posicao de um determinado caractere
print (movieName.find('n')) # ele conta a quantidade de um caractere
print (movieName.replace('Top','Matrix')) #altera caracteres
print (movieName.split(','))


####

# ex1
nVar1 = str(input('Escreva um nome:\n'))
nVar2 = str(input('Escreva a segunda variavel:\n'))

nomeFormatado = f'{nVar2} {nVar1}'
print (nomeFormatado)


# ex2
texto = 'Diego desenvolvedor de python'
palavras = texto.split()
textoInvertido = ' '.join(palavras[::-1])
print (textoInvertido)

# ex3

texto1 = 'arara'
texto2 = 'python'

formatado1 = texto1.lower().replace(' ',' ')
formatado2 = texto2.lower().replace(' ',' ')

# verifica se o texto original é  igual ao seu reverso

palindromo1 = formatado1 == texto1 [::-1]
palindromo2 = formatado2 == texto2 [::-1]

print (palindromo1, '\n', palindromo2)