time1 = input("digite o nome do time")
time2 = input("digite o nome do segundo time")

gols1 = int(input("digite quantos gols esse time fez:"))
gols2 = int(input("digite quantos gols esse time fez:"))

if gols1 > gols2:
    print(f"o {time1} venceu")
else:
    if gols1 == gols2:
        print("empate")
    else:
        print(f"o {time2} venceu")