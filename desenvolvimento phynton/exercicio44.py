primeiro_valor = int(input("Digite o primeiro valor:"))
ultimo_valor = int(input("Digite o ultimo valor"))
incremento = int(input("Digite o incremento"))

valor_atual = primeiro_valor

while primeiro_valor <= ultimo_valor:
print(primeiro_valor, end=" ")
primeiro_valor = primeiro_valor + incremento
print("Acabou!")
