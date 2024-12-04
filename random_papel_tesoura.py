import random
jogo=["PEDRA", "PAPEL", "TESOURA"]
meus_pontos = 0
computador_pontos = 0
while true:
    print("Escolha uma das opções ( Pedra / Papel / Tesoura)")
opcao = input("Escolha uma das opções ").upper()
computador = random.choice(jogo)
if opcao == computador :
    print("Empate ")
    print("Voce escolheu ", opcao)
    print("Computador escolheu ", computador)
    
    elif opcao == "Pedra" :
        if computador == "Tesoura"
        meus_pontos = meus_pontos + 1
        print ("Voce ganhou ")
        print("Voce escolheu ", opcao)
        print("computador escolheu",computador)
    else :
         elif opcao == "Tesoura" :
        if computador == "Papel" :
        meus_pontos = meus_pontos + 1
        print ("Voce ganhou ")
        print("Voce escolheu ", opcao)
        print("computador escolheu",computador)
    else :
        computador_pontos = computador_pontos + 1
        print("Computador ganhou ")
        print("Voce Escolheu", opcao)
        print("Computador Escolheu",computador)
    else :
        
    resposta = input("Deseja jogar novamente (S/N)?").upper()
    if resposta != "S" :
        break
    
    print("Resultado Final ")
    print("Meus pontos..........", meus_pontos, "Pontos ")
    print("Computador pontos.....",computador_pontos, "Pontos ")
