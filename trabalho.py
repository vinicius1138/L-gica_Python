from datetime import datetime

Placa = input("PLACA:\n")
Tipo = ["moto","carro"]
Modelo = input("O QUE É SEU AUTOMÓVEL:\n")
hora1 = input("HORA DE ENTRADA:\n")
hora2 = input("HORA DE SAÍDA:\n")

formato = '%H:%M'
hora1c = datetime.strptime(hora1, formato)
hora2c = datetime.strptime(hora2, formato)

tempo = (hora2c - hora1c).total_seconds()/3600
print(tempo,"H")

if Modelo == "carro":
	print("VALOR DO ESTACIONAMENTO:",tempo*12.00, "reais","PLACA:", Placa, "TEMPO TOTAL:", tempo,"horas")
if Modelo == "moto":
	print("VALOR DO ESTACIONAMENTO:",tempo*8.00, "reais","PLACA:", Placa, "TEMPO TOTAL:", tempo,"horas")


 