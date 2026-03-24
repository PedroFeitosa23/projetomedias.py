# Lista para armazenar os alunos
lista_alunos = []


# Função para calcular média
def calcular_media(n1, n2):
    return (n1 + n2) / 2


# Função para verificar situação
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


# MENU PRINCIPAL
while True:
    print("\n===== SISTEMA ESCOLAR =====")
    print("1 - Cadastrar aluno")
    print("2 - Ver relatório")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # CADASTRAR ALUNO
    if opcao == "1":
        nome = input("Nome do aluno: ")

        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))

        media = calcular_media(nota1, nota2)
        situacao = verificar_situacao(media)

        aluno = {
            "nome": nome,
            "media": media,
            "situacao": situacao
        }

        lista_alunos.append(aluno)

        print(f"\nMédia: {media:.2f}")
        print(f"Situação: {situacao}")

    # RELATÓRIO FINAL
    elif opcao == "2":
        if len(lista_alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            print("\n===== RELATÓRIO =====")

            soma = 0
            maior = lista_alunos[0]
            menor = lista_alunos[0]

            for aluno in lista_alunos:
                print(f"\nNome: {aluno['nome']}")
                print(f"Média: {aluno['media']:.2f}")
                print(f"Situação: {aluno['situacao']}")

                soma += aluno["media"]

                if aluno["media"] > maior["media"]:
                    maior = aluno

                if aluno["media"] < menor["media"]:
                    menor = aluno

            media_turma = soma / len(lista_alunos)

            print("\n===== ESTATÍSTICAS =====")
            print(f"Quantidade de alunos: {len(lista_alunos)}")
            print(f"Média da turma: {media_turma:.2f}")
            print(f"Maior média: {maior['nome']} ({maior['media']:.2f})")
            print(f"Menor média: {menor['nome']} ({menor['media']:.2f})")

    # SAIR
    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")