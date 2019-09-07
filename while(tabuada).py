num = int(input("NUMERO:\n"))
op = input("OPERACAO [+|-|*|/]:\n")
aux = 1

while aux <= 10:
	if op == "+":
		print(num,"+", aux, "=", num+aux)
	if op == "-":
		print(num,"-", aux, "=", num-aux)
	if op == "*":
		print(num,"x", aux, "=", num*aux)
	if op == "/":
		print(num,"/", aux, "=", num/aux)	
	aux += 1

