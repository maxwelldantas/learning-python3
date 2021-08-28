# Hora de Praticar
# App Média Escolar

print()
print("#################################################")
print("Bem vindo ao programa de cálculo de Média Escolar")
print("#################################################")
print()

nome = input("Aluno(a) digite seu nome: ")
materia = input("Aluno(a) digite o nome da matéria: ")
print("Agora você precisa informar as suas quatro notas")
nota1 = input("Aluno(a) digite sua primeira nota: ")
nota2 = input("Aluno(a) digite sua segunda nota: ")
nota3 = input("Aluno(a) digite sua terceira nota: ")
nota4 = input("Aluno(a) digite sua quarta nota: ")

nota1 = 0 if not nota1.isdigit() else nota1
nota2 = 0 if not nota2.isdigit() else nota2
nota3 = 0 if not nota3.isdigit() else nota3
nota4 = 0 if not nota4.isdigit() else nota4

media_notas = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4

if media_notas < 7:
    print("Aluno(a) %s, você foi REPROVADO(A). Sua média em %s foi %.2f!" % (nome, materia, media_notas))
else:
    print("PARABENS!!\nAluno(a) %s, você foi APROVADO(A). Sua média em %s foi %.2f!" % (nome, materia, media_notas))
