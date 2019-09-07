import random

advinha = random.randrange(1,10)
num = int(input("advinhe o numero:"))

while advinha != num:
	if advinha > num:
		print("maior")
		num = int(input("advinhe o numero:"))
	if advinha < num:
		print("menor")
		num = int(input("advinhe o numero:"))
	if advinha == num:
		print("Achouu...", advinha)


