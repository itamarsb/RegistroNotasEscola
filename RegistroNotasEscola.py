# Pede ao usuário (o professor) que digite o nome do aluno.
def pedir_nome():
    return input("Digite o nome do aluno (ou 'fim' para encerrar): ")

# Pede ao professor que digite a nota do aluno.
def pedir_nota():
    return input("Digite a nota de 0 a 10: ")

# Verifica se a nota digitada pode ser convertida para número e está entre 0 e 10.
def nota_valida(nota_str):
    try:
        nota = float(nota_str)
        if nota >= 0 and nota <= 10:
            return True
        else:
            return False
    except:
        return False

# Recebe o dicionário com nomes e notas e soma todas as notas, dividindo pela quantidade de alunos, pra calcular a média da turma.
def calcular_media(dicionario_notas):
    soma = 0
    for nota in dicionario_notas.values():
        soma = soma + nota
    return soma / len(dicionario_notas)

# É a função principal da estrutura de código, onde tudo começa. Começando por mostrar as instruções ao professor.
def main():
    print("Cadastro de notas da turma")
    print("Digite 'fim' quando quiser encerrar o cadastro")

    # Cria esse dicionário chamado notas_alunos.
    notas_alunos = {}

    # Nesse laço pede o nome do aluno e associa a nota do mesmo.
    while True:
        nome = pedir_nome()
        if nome == 'fim':
            break

        nota_entrada = pedir_nota()

        # Verifica se a nota é válida. Se for válida, guarda a nota no dicionário, associada ao nome.
        if nota_valida(nota_entrada):
            notas_alunos[nome] = float(nota_entrada)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")

    # Depois que o professor digitar 'fim', calcula a média com base nas notas armazenadas e exibe a média final da turma.
    if len(notas_alunos) > 0:
        media = calcular_media(notas_alunos)
        print("A média da turma é:", media)
    else:
        print("Nenhuma nota válida foi registrada.")

main()
