
print("Valor da gasolina por litro R$4,89\n")

litros = input("LITROS DE GASOLINA:  ")

precototal = (float (litros)*4.89)

if precototal>50:
	print("Preco total R$",precototal,"por",litros,"litro(s) esta caro") 
else:
	print("Preco total R$",precototal,"por",litros,"litro(s) esta barato")