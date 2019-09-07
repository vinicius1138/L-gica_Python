from datetime import datetime

hora1 = input("HORA DE ENTRADA:\n")
hora2 = input("HORA DE SAÍDA:\n")

formato = '%H:%M'#21:00
hora1c = datetime.strptime(hora1, formato)
hora2c = datetime.strptime(hora2, formato)

tempo = (hora2c - hora1c).total_seconds()/3600
print(tempo)