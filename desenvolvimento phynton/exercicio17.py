nome = input("Digite o nome ")
salario = float(input("Digite o salário))
anos = int (input("Digite quantos anos trabalha na empresa"))

if anos <= 3 :
   aumento = salario * 0.03
elif 3 < anos <= 10:
   aumento = salario * 0.125
else:
   aumento = salario * 0.20
   faixa_aumento = "20%"
novo_salario = salario + aumento
print(f"aumento de salario com ",faixa_aumento)
print(f"Novo salario R$ {novo_salario:.2f}")

