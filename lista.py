produtos = ["requeijao", "batata", "banana"]
valor = [2.20, 4.7, 4]
cod = int(input("INFORME O CODIGO DO PRODUTO:\n"))
qnt = int(input("QUANTIDADE:\n"))
total = valor[cod]*qnt
print("Produto:", qnt, "x" , produtos[cod])
print("Valor Unitario:", valor[cod])
print("Total: ", total)
