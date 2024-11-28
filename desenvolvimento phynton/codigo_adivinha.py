import random

def jogar():
    # O computador sorteia um número entre 1 e 100
    numero_sorteado = random.randint(1, 100)
    
    # Inicializa o contador de tentativas
    tentativas = 1
    
    # Solicita ao jogador que adivinhe o número
    print("Tente adivinhar o número sorteado entre 1 e 100")
    
    while tentativas < 10:  # Limita o número de tentativas a 10
        try:
            # Leitura da tentativa do jogador
            palpite = int(input("Digite o seu palpite (1 a 100): "))
            
            # Verificação se o palpite está dentro do intervalo permitido
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue
            
            # Incrementa o número de tentativas
            tentativas += 10
            
            # Identifica se o número digitado é maior que o numero sorteado
            if palpite > numero_sorteado:
                print("O número é maior que o sorteado.")
            
            # Identifica se o número digitado é menor que o numero sorteado
            elif palpite < numero_sorteado:
                print("O número é menor que o sorteado.")
            
            # Verifica se o palpite está correto
            if palpite == numero_sorteado:
                print(f"Você acertou o número em {tentativas} tentativas!")
                break
        except ValueError:
            print("Por favor, digite um número válido.")
    
    if palpite != numero_sorteado:
        print("Você não acertou o número em 10 tentativas. O número sorteado era:", numero_sorteado)

# Função principal para controlar o jogo
def main():
    print("Bem-vindo ao jogo de Adivinhação!")
    
    while True:
        jogar()
        
        # Pergunta se o jogador quer jogar novamente
        continuar = input("\nDeseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por jogar! Até logo!")
            break
        else:
            print("O jogo poderá terminar quando você acertar o número ou quando for feita 10 tentativas.")

# Inicia o jogo
if __name__ == "__main__":
    main()
