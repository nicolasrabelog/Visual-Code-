contador = 30
while (contador >= 0):
    if contador % 4 ==0:
        print(f"[{contador}]", end=" ")
    else:
        print(contador, end =" ")
    contador = contador -1
print("Acabou!")

#end=" "
