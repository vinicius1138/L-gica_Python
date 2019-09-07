nome = input("INSIRA  SEU NOME:\n")
peso = input("INSIRA SEU PESO:\n")
altura = input("INSIRA SUA ALTURA:\n")

imc = float(peso)/(float(altura)*float(altura))

if imc < 18:
    print("ABAIXO DO PESO")
elif  imc >= 18.5 - imc <= 24.9:
    print("PESO NORMAL") 
elif imc >= 25 - imc <= 29.9:
    print("ACIMA DO PESO")
elif imc >= 30 - imc <= 34.9:
    print("OBESIDADE GRAU I")
elif imc >= 35 - imc <= 39.9:
    print("OBESIDADE GRAU II")
elif imc >= 40:
    print("OBESIDADE GRAU III")

print("O IMC DE", nome, "E", imc)