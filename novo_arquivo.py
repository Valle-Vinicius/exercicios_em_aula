valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um valor: "))
valor3 = int(input("Digite um valor: "))
media = valor1 + valor2 + valor3/3

if media > 0 and media <= 6:
    print(f"A média dos valores é {media}, você reprovou!")
elif media > 6:
    print(f"A média dos valores é {media}, você passou!")