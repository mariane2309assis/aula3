nota1 = float(input("digite a 1  nota"))
nota2 = float(input("digite a 2 nota"))
nota3 = float(input("digite a 3 nota"))

media = (nota1+nota2+nota3)/3

if media >= 7:
    print(f"Aprovado{media}")
else:
    if media < 4:
        print(f"reprovado{media}")
    else:
        print(f"recuperação{media}")

