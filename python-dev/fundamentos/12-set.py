filmsSet = {'Matrix','Batman','Simpsons',
              'Palmeiras','Chaves'}

print (type(filmsSet))

# 1 - Buscar o tamanho do set
print (len(filmsSet))

# 2 - Adicionar item de outro set


exampleset = {'Teste'}
filmsSet.update (exampleset)
print (filmsSet)

# 3 - Removr item do set

filmsSet.remove ('Teste')
print (filmsSet)