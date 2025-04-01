nome = input("digite seu nome")
idade = int(input("digite sua idade"))
salario = float(input("digite seu salário"))
percentual = float (input("digite o percentual"))

valorreal = salario *  percentual/100
novosalario = salario + valorreal

print(f"ola seu nome {nome} sua {idade}, seu novo salário {novosalario}")