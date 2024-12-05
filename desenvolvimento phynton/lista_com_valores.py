lista =[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

#Exibir a lista
print("Lista:", lista)

#Exibir a lista na ordem inversa
print("Lista na ordem inversa:", lista[::-1])

#Exibir o menor numero da lista
print("Menor numero da lista:", min(lista))

#Exibir o numero maximo de numeros da lista
print("Maior numero da lista:", max(lista))

#Exibir o total de numeros da lista
print("Total de numeros da lista:", len(lista))

#Exibir a soma dos numeros da lista
print("Soma dos numeros da lista:", sum(lista))

#Exibir a media dos numeros da lista
media = sum(lista) / len(lista)
print("Media dos numeros da lista:", media)

#Exibir quantas vezes o numero -20 aparece na lista
print("Numero -20 aparece", lista.count(-20), "vezes")
