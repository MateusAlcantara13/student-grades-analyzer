# ==============================
# Função utilitária (tratamento de entrada)
# ==============================
def formatar_entrada(nota):
    # Converte formato brasileiro (7,5) para padrão Python (7.5)
    nota = nota.replace(',', '.')
    return float(nota)


# ==============================
# Função de entrada de dados (cadastro)
# ==============================
def inserir_notas(quantNotas):

    notas = []

    for i in range(quantNotas):
        nota = formatar_entrada(input(f'Insira a {i + 1}ª nota: '))

        # Validação de dados (controle de erro do usuário)
        while nota < 0 or nota > 10:
            print('Insira uma nota válida!')
            nota = formatar_entrada(input(f'Insira a {i + 1}ª nota: '))

        notas.append(nota)

    # Retorna a lista pronta
    return notas


# ==============================
# Função de processamento (lógica)
# ==============================
def maiorNota_menorNota_posMaior_posMenor(notas):

    maiorNota = notas[0]
    menorNota = notas[0]
    posMaior = 1
    posMenor = 1

    # enumerate → percorre lista com índice e valor
    for i, valor in enumerate(notas):
        if valor > maiorNota:
            maiorNota = valor
            posMaior = i + 1

        if valor < menorNota:
            menorNota = valor
            posMenor = i + 1

    # Retorno múltiplo (desempacotamento)
    return maiorNota, menorNota, posMaior, posMenor


# ==============================
# Função de contagem (processamento)
# ==============================
def contar_acima_abaixo_igual(notas, mediaMin):

    acima = 0
    abaixo = 0
    igual = 0

    for nota in notas:
        if nota > mediaMin:
            acima += 1
        elif nota < mediaMin:
            abaixo += 1
        else:
            igual += 1

    return acima, abaixo, igual


# ==============================
# Função de saída (procedimento / side effect)
# Apenas imprime — não retorna valor
# ==============================
def pontos_acima_abaixo_igual(mediaTurma, mediaMin):

    if mediaTurma > mediaMin:
        print(f'A média da turma foi {mediaTurma - mediaMin:.2f} pontos mais alta do que a média mínima!')
    elif mediaTurma < mediaMin:
        print(f'A média da turma foi {mediaMin - mediaTurma:.2f} pontos abaixo da média mínima!')
    else:
        print('A média da turma foi igual à média mínima!')


# ==============================
# Função de exibição (procedimento / saída no terminal)
# ==============================
def mostrar_relatorios(notas, acima, abaixo, igual, maiorNota, posMaior, menorNota, posMenor, mediaTurma):

    print(f'Notas registradas: {notas}')
    print('=' * 30)

    print(f'Quantidade de notas acima: {acima}')
    print(f'Quantidade de notas abaixo: {abaixo}')
    print(f'Quantidade de notas iguais à média mínima: {igual}')
    print('=' * 30)

    print(f'Maior nota registrada: {maiorNota} (posição: {posMaior})')
    print(f'Menor nota registrada: {menorNota} (posição: {posMenor})')
    print('=' * 30)

    print(f'A média da turma foi: {mediaTurma:.2f}')
    print('=' * 30)


# ==============================
# Função de cálculo (processamento matemático)
# ==============================
def media_turma(notas):
    media = sum(notas) / len(notas)
    return media


# ==============================
# PROGRAMA PRINCIPAL (fluxo de execução)
# Aqui as funções são chamadas
# ==============================

quantNotas = int(input('Insira a quantidade de notas para serem cadastradas: '))

notas = inserir_notas(quantNotas)

mediaMin = formatar_entrada(input('Insira a nota mínima de aprovação: '))
mediaTurma = media_turma(notas)

acima, abaixo, igual = contar_acima_abaixo_igual(notas, mediaMin)
maiorNota, menorNota, posMaior, posMenor = maiorNota_menorNota_posMaior_posMenor(notas)

mostrar_relatorios(notas, acima, abaixo, igual, maiorNota, posMaior, menorNota, posMenor, mediaTurma)
pontos_acima_abaixo_igual(mediaTurma, mediaMin)
