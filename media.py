nome = input("NOME DO ALUNO:")

np = input("INFORME A NOTA DA PROVA\n")

nt = input("INFORME A NOTA DO TRABALHO\n")

nq = input("INFORME A NOTA DA QUALITATIVA\n")

media = ( float (np)*6 + float (nt)*3 + float(nq))/10

if media>= 6:
	print("aprovado")
else:
	print("reprovado")

print("MEDIA DO ALUNO", nome, "e", media)