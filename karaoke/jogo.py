print("=-="*15)

print("     Bem vindo ao jogo do Mendigo maluco   ")

print("=-="*15)



p = str(input("Digite seu nome: "))

print("=-="*17)

lista = ("Uma mão no volante, ea outra no carinho","Parabéns pelo que que você é","Se você nunca calou um homem, você me calou agora","Se for ruim com elas, vai ser muito pior sem elas","Sou um amante das mulheres")

p1 = int(input("Digite um número, para começar o jogo obs(1 a 5): "))

while True:

    while p1 > 5:

        p1= int(input("Opção inválida, Digite um número de (1 a 5): "))

    if p1 == 1:

        print(lista[0])

    if p1 == 2:

        print(lista[1])

    if p1 == 3:

        print(lista[2])

    if p1 == 4:

        print(lista[3])

    if p1 == 5:

        print(lista[4])

    p3 = str(input("Você quer continuar.? [S/N]")).upper().strip()

    if p3 == "N":

        break

    if p3 == "S":

        p1 = int(input("Digite um novo número: "))



   

   

print(f"Obrigado por participar {p}")