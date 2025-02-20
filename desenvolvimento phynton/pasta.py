1) 
# Exibe a mensagem na tela
print("Olá, Mundo!")

2) 
# Exibe a mensagem de boas-vindas
print(f"Olá {nome}, é um prazer te conhecer!")

3)
# Solicita o nome e o salário do funcionário
nome = input("Nome do Funcionário: ")
salario = float(input("Salário: "))
# Exibe a mensagem formatada
print(f"O funcionário {nome} tem um salário de R${salario:.2f} em Junho.")

4) 3.
# Solicita dois números inteiros ao usuário
numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite outro valor: "))
# Calcula a soma
soma = numero1 + numero2
# Exibe o resultado
print(f"A soma entre {numero1} e {numero2} é igual a {soma}.")

5) 
# Solicita as duas notas ao usuário
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
# Calcula a média
media = (nota1 + nota2) / 2
# Exibe o resultado
print(f"A média entre {nota1} e {nota2} é igual a {media:.1f}")

6) 
# Solicita um número inteiro ao usuário
numero = int(input("Digite um número: "))
# Calcula o antecessor e o sucessor
antecessor = numero - 1
sucessor = numero + 1
# Exibe os resultados
print(f"O antecessor de {numero} é {antecessor}")
print(f"O sucessor de {numero} é {sucessor}")

7) 
# Solicita um número real ao usuário
numero = float(input("Digite um número: "))
# Calcula o dobro e a terça parte
dobro = numero * 2
terca_parte = numero / 3
# Exibe os resultados
print(f"O dobro de {numero} é {dobro}")
print(f"A terça parte de {numero} é {terca_parte:.5f}")

8) 
# Solicita a distância em metros ao usuário
metros = float(input("Digite uma distância em metros: "))
# Calcula as conversões
km = metros / 1000           # Quilômetros
hm = metros / 100            # Hectômetros
dam = metros / 10            # Decâmetros
dm = metros * 10             # Decímetros
cm = metros * 100            # Centímetros
mm = metros * 1000           # Milímetros
# Exibe os resultados
print(f"A distância de {metros}m corresponde a:")
print(f"{km}Km")
print(f"{hm}Hm")
print(f"{dam}Dam")
print(f"{dm}dm")
print(f"{cm}cm")
print(f"{mm}mm")

9) 
# Solicita a quantidade de dinheiro em reais ao usuário
reais = float(input("Quanto dinheiro você tem na carteira (em R$): "))
# Conversão para dólares
dolares = reais / 3.45
# Exibe o resultado
print(f"Com R${reais:.2f}, você pode comprar US${dolares:.2f}.")

10) 
# Solicita a largura e a altura da parede
largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))
# Calcula a área da parede
area = largura * altura
# Calcula a quantidade de tinta necessária (1 litro cobre 2 m²)
quantidade_tinta = area / 2

# Exibe os resultados
print(f"A área a ser pintada é {area} m².")
print(f"A quantidade de tinta necessária é {quantidade_tinta} litros.")
print("será necessario ", quant_litros, "litros")

11)
# Solicita os coeficientes A, B e C da equação do segundo grau
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
# Calcula o valor de Delta
delta = (B ** 2) - (4 * A * C)
# Exibe o resultado
print(f"O valor de Delta é {delta}.")

12) 
# Solicita o preço do produto
preco = float(input("Digite o preço do produto: "))
# Calcula o preço promocional com 5% de desconto
desconto = preco * 0.05
preco_promocional = preco - desconto
# Exibe o resultado
print(f"O preço promocional é R${preco_promocional:.2f}.")

13) 
# Solicita o salário do funcionário
salario = float(input("Digite o salário do funcionário: "))
# Calcula o novo salário com 15% de aumento
aumento = salario * 0.15
novo_salario = salario + aumento
# Exibe o resultado
print(f"O novo salário com 15% de aumento é R${novo_salario:.2f}.")

14) 
# Solicita a quantidade de Km percorridos e os dias de aluguel
km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias que o carro foi alugado: "))
# Calcula o preço total
preco_por_dia = 90
preco_por_km = 0.20
custo_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)
# Exibe o resultado
print(f"O preço total a pagar é R${custo_total:.2f}.")

15) 
# Solicita o número de dias trabalhados
dias_trabalhados = int(input("Digite o número de dias trabalhados no mês: "))
# Cálculo do salário
horas_por_dia = 8
valor_por_hora = 25
salario = dias_trabalhados * horas_por_dia * valor_por_hora
# Exibe o resultado
print(f"O salário do funcionário é R${salario:.2f}.")

16) 
# Solicita a quantidade de cigarros fumados por dia e quantos anos fumou
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Quantos anos você fumou? "))
# Calcula a redução de vida em minutos
minutos_perdidos_por_cigarro = 10
total_cigarros = cigarros_por_dia * 365 * anos_fumando
tempo_perdido = total_cigarros * minutos_perdidos_por_cigarro
# Converte para dias
dias_perdidos = tempo_perdido / (60 * 24)
# Exibe o resultado
print(f"Você perderá aproximadamente {dias_perdidos:.2f}dias_de_vida.")

17)
# Calcula a velocidade de um carro

# Pergunta a velocidade do carro
velocidade = float(input("Qual a velocidade do carro (em km/h)? "))
# Velocidade permitida
limite_velocidade = 80
# Se a velocidade ultrapassar o limite, aplica a multa
if velocidade > limite_velocidade:
excesso = velocidade - limite_velocidade
multa = excesso * 5  # 5 reais por km acima do limite
print(f"Você foi multado! O valor da multa é R${multa:.2f}.")
else:
print("Você está dentro do limite de velocidade. Não há multa.")
