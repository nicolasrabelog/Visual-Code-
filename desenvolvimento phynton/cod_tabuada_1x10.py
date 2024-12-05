# Função para exibir a tabuada de um número
def exibir_tabuada(numero):
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar ao usuário um número para exibir a tabuada
while True:
    try:
        numero = int(input("Digite um número para ver a tabuada (1 a 10) ou 0 para sair: "))
        if numero == 0:
            print("Saindo...")
            break
        elif 1 <= numero <= 10:
            exibir_tabuada(numero)
        else:
            print("Por favor, digite um número entre 1 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
