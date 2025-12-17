dicionario = {
    'titulo':'Batman',
    'anoLancamento':2025,
    'nota': 8.3,
    'genero':['Ação','Drama','Suspense','Comédia']
}

print (dicionario)
print (len(dicionario))
print (type(dicionario))

# 1 - Recupera um elemento do dicionario

print (dicionario['genero'])
print (dicionario.get('nota'))

# 2 - Buscar apenas as chaves do dicionario

print (dicionario.keys())

# 3 - Buscar apenas os valores do dicionario

print (dicionario.values())

# 4 - Buscar itens do dicionario com chaves e valores

print (dicionario.items())

# 5 - Adicionar itens no dicionario

dicionario['diretor'] = 'Diego Spinella'
dicionario['titulo'] = 'Coringa'
print (dicionario)

# 6 - Atualizar itens no dicionario

dicionario.update({'titulo': 'Coringa'})