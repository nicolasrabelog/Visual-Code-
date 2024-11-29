import random

numero_sorteado = random.randint(1, 100)
tentativas = 0

print("Tente adivinhar o  número entre 1 e 100,")

while tentativas <10:
    chute = int(input("Digite seu número"))
    tentativas += 1 
    
    if chute == numero_sorteado:
        print ("voce acertou o número!")
        break
    elif chute < numero_sorteado:
        print("O numero é maior")
    else:
        print("O número é menor")

if chute != numero_sorteado:
    print ("Você atingiu um número de tentativas")
    
