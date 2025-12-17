import pprint

dicionario = {
    "batman": {
        "anoLancamento": 2025,
        "nota": 8.3,
        "genero": ["Ação", "Drama", "Suspense", "Comédia"]
    },
    "chaves": {
        "anoLancamento": 1999,
        "nota": 9.6,
        "genero": ["Ação", "Comédia"]
    },
    "coringa": {
        "anoLancamento": 1995,
        "nota": 10.0,
        "genero": ["Suspense", "Drama"]
    }
}


#pp = pprint.PrettyPrinter(depth=4)
#pp.pprint(dicionario)

# 1 - Buscar uma informação dentro de um dicionario aninhado

print (dicionario["chaves"]["genero"])

# 2 Adicionar um novo item

dicionario ["coringa"]["produtor"] = "diego spinella"

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(dicionario)

# 3 - Deletar um filme 

del dicionario["batman"]
pp.pprint (dicionario)