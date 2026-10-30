alunos = {}
def classificar():

    for i in alunos:
        if alunos[nome] >= 6:
            print(f"O aluno {nome} foi aprovado com nota {nota}")

        elif alunos[nome] >= 4 and alunos[nome] <= 5.9:
            print(f"O aluno {nome} esta de recuperação com nota {nota}")

        elif alunos[nome] < 4:
            print(f"O aluno {nome} foi reprovado com nota {nota}")

print("--Cadastro de alunos--")
nome = input("Digite o nome do aluno: ").upper()
nota = int(input("Digite a nota do aluno: "))
alunos[nome] = nota
print("--Deseja adcionar outro aluno?[S/N]--")
escolha = input("").upper()


while True:
    if escolha == "S":
        print("--Cadastro de alunos--")
        nome = input("Digite o nome do aluno: ").upper()
        nota = int(input("Digite a nota do aluno: "))
        alunos[nome] = nota
        print("--Deseja adcionar outro aluno?[S/N]--")
        escolha = input("").upper()
    elif escolha == "N":
        print(alunos)
        classificar()
        break


