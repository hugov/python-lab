# Este código tem como objetivo construir uma programa 
# que que calcula a média escolar de um aluno em Python.

aluno = input("Informe o seu nome: ")

media = 0

for indice in range(1 , 5):
    
    msgNotaInput = "Informe a nota {} : ".format(indice)
    nota = input(msgNotaInput)

    media += float(nota)

    msgNota = "A nota {} informada foi {} ".format(indice, nota)

media /= 4
situacao = None

if media >= 7:
    situacao = "Aprovado(a)"
else:
    situacao = "Reprovado(a)"

msgMedia = "O aluno(a) {} obteve a média {} . Situação: {} ".format(aluno, str(media), situacao)
print(msgMedia)