# Hora de Praticar
# App Médica Escolar

print("Programa App Média Escolar em execução")

aluno = input("Aluno(a) digite seu nome: ")
print(aluno)
materia = input("Aluno(a) digite o nome da matéria: ")
print(materia)
primeira_nota = input("Aluno(a) digite sua primeira nota: ")
print(primeira_nota)
segunda_nota = input("Aluno(a) digite sua segunda nota: ")
print(segunda_nota)
terceira_nota = input("Aluno(a) digite sua terceira nota: ")
print(terceira_nota)
quarta_nota = input("Aluno(a) digite sua quarta nota: ")
print(quarta_nota)

VAZIO = ''

primeira_nota = 0 if not primeira_nota or not primeira_nota.isdigit() else primeira_nota
segunda_nota = 0 if not segunda_nota or not segunda_nota.isdigit() else segunda_nota
terceira_nota = 0 if not terceira_nota or not terceira_nota.isdigit() else terceira_nota
quarta_nota = 0 if not quarta_nota or not quarta_nota.isdigit() else quarta_nota

media_notas = (float(primeira_nota) + float(segunda_nota) + float(terceira_nota) + float(quarta_nota)) / 4

if media_notas < 7:
    print("Aluno(a) %s, você foi REPROVADO(A). Sua média em %s foi %.2f!" % (aluno, materia, media_notas))
elif media_notas >= 7:
    print("PARABENS!!\nAluno(a) %s, você foi APROVADO(A). Sua média em %s foi %.2f!" % (aluno, materia, media_notas))
