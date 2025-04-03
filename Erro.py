gabarito = ["A", "B", "C", "D", "E", "A", "B", "C", "D", "E"]
gabaritoaluno = []
contadoracertos = 0
contador = 1

for i in range(10):
    valor = input(f"{contador}. Digite seu gabarito! ")
    gabaritoaluno.append(valor)
    contador += 1

for i in range(10):
    if gabarito[i] == gabaritoaluno[i]:
        contadoracertos += 1

print(f"Você terminou de corrigir sua prova e, ao todo, você acertou {contadoracertos}/10")