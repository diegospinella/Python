filmsList = ['Matrix','Batman','Simpsons',
              'Palmeiras','Chaves','Cavaleiro dos Zodíacos']

# 1 - Tamanho da lista

print (len(filmsList))

#2 - Recuperar um item da lista pelo nome

print (filmsList.index('Chaves'))

#3 - Adicionar um item ao final da lista

filmsList.append('Senhor dos Anéis')
print (filmsList)
print(filmsList.index('Senhor dos Anéis'))


#4 - Ordenar a lista

filmsList.sort()
print (filmsList)

#5 - Copiar itens de uma lista para outra

filmsListCopy = filmsList.copy()
print(filmsListCopy)

#6 - Se eu quiser remover um item de uma lista

filmsListCopy.remove('Cavaleiro dos Zodíacos')
print(filmsListCopy)

#6 - Remove todos os itens da lista

filmsListCopy.clear()
print (filmsListCopy)