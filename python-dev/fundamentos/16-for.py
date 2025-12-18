listaFilmes = ['Chaves','Kiko','Chiquinha','Nhonho']

#1 - Interando os valores de uma lista

for filme in listaFilmes:
    print(filme)

#2 - Quando a condição for atendida, o loop será encerrado

for filme in listaFilmes:
    if filme == 'Chiquinha':
        break
    print (filme)

#3 - Quando a condição for atendida, o loop vai para a próxima iteração (pulou a Chiquinha)

for filme in listaFilmes:
    if filme == 'Chiquinha':
        continue
    print (filme)

#4 - Avaliação do filme

filme = input ('Digite o nome do filme:\n')
notaFilme = int(input('Digite quantas avaliações deseja fazer:\n'))
total = 0

for i in range(notaFilme):
     nota = float(input('Digite a nota para o filme:\n'))
     total += nota

if notaFilme > 0:
    media = total / notaFilme
else:
    media = 0

print(f'Média de avaliação do filme {filme} é: {media:.2f}')



