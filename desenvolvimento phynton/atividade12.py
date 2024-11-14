 ano = int(input("informe o ano atual "))
nascimento = int(input("informe o ano do nascimento "))
idade = ano - nascimento
if idade < 18 :
    print("Faltam",18-idade, " anos para você fazer o alistamento")
else :
    print("Você ja tem", idade-18, "anos que fez o alistamento")
