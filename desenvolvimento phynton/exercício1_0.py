Ex10
ano_atual = int (input("Digite o ano atual "))
nascimento = int(input("Digite o ano do nascimento "))
idade = ano_atual - nascimento 
if idade >= 16 :
    print("Pode votar sua idade e ", idade, "anos ")
else :
    print("Nao pode votar sua idade e ",idade, "anos ")
