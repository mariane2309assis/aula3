
tipo = input("digite o tipo de combustível \n"
        "G para gasolina\n"
        "E etanol\n")

qnt =  float(input("quantos litros: "))

vEtal = 4.90
vGas = 5.80
valor = 0
if tipo == "G" or tipo == "g":
    valor = vGas * qnt
elif tipo == "E" or tipo == "e";
    valor = vEtal * qnt


else:

    print(f"você gastou R${valor: .2f}")



