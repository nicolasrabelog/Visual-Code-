valor_casa = float(input("Informe o valor da casa "))
anos = int(input("Informe o quantos anos ira funcionar o carro "))
salario = float(input("Informe o salário" ))
prestacao = valor_casa / (anos * 12)
if prestacao > salario * 0.30 :
    print("O valor da prestação ultrapassa 30% do seu salário ")
    print(f"Valor da prestação R$ {prestacao .2f}")
else:
    print(f"Valor da prestação R$ {prestacao .2f}")
    print(f"paga em {anos*12} meses ")
