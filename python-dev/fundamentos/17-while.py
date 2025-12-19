movelist = ['Chaves','Kiko','Chiquinha','Nhonho']

#1 - Iterando valores de uma lita de filmes usando while

index = 0

# print (len(movelist))

# while index < len(movelist):
#     print (movelist[index])
#     index += 1

#2 - Quando a condição for atendida, o loop será encerrado

while index < len(movelist):
    if movelist[index] == 'Chiquinha':
        break
    print (movelist[index])
    index += 1
               
#2 - Quando a condição for atendida, o loop vai para a próxima iteração.

while index < len(movelist):
    if movelist[index] == 'Chiquinha':
        index += 1
        continue
    print (movelist[index])
    index +=1

#3 - Avalição do filme:

movieName = input ('Digite o nome do filme:\n')
movieRating = int(input('Digite quantas avaliações deseja fazer:\n'))

total = 0
count = 0

while count < movieRating:
    note = float(input('Digite a nota do filme:\n'))
    total += note
    count += 1

    if movieRating > 0:
        avarage = total / movieRating
    else:
        avarage = 0

print(f'Média de avaliação do filme {movieName} é: {avarage:.2f}')

