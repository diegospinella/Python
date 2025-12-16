name = input('Digite o nome do filme:\n')
yearLaunch = int(input('Digite o ano de lancamento:\n'))
noteMovie = float(input('Digite a nota do filme:\n'))


#alternativa1
#print ('Dados do filme')
#print ('==========================')
#print (type('Nome do filme:', name))
#print (type('Ano do filme:', yearLaunch))
#print (type('Nota do filme:', noteMovie))

#alternativa2

print ('Dados do filme2')
print ('==========================')
print ('Nome do filme:', name, '\nAno do flme:', yearLaunch, '\nNota do filme:', noteMovie)

#alternativa3

print ('Dados do filme2')
print ('==========================')
print (f'Nome do jogo: {name}\n'
       f'Ano do filme: {yearLaunch}\n'
       f'Nota do filme: {noteMovie}\n'
       )
