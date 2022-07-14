#--------------------------------------------#
#                 CONTRATADO!                #

# criando o dicionário inicial para cadastro geral dos candidatos
dicionario_cadidatos = dict()

while True:  # entrando no programa
    voltar = True
    verificacao = int(input(
        "Se você deseja fazer uma nova inscrição, digite [1].\nMas, se deseja verificar os cadidatos na base, digite [2]: "))
    if not(verificacao == 1 or verificacao == 2):
        voltar == True
    else:
        break

id = 1  # id de identificação dos candidados, caso haja nomes repitidos
while True:  # recebendo as informações dos cadidatos
    voltar = True
    if verificacao == 1:
        print('----------')
        nome_candidato = input(
            'Digite o nome completo do candidato: ')
        lista_candidato = []
        vaga_candidato_escolha = int(input(
            'Digite [1] para vaga de Analista de Dados ou digite [2] para vaga de Cientista de Dados: '))
        if vaga_candidato_escolha == 1:
            vaga_candidato = 'Analista de Dados'
        elif vaga_candidato_escolha == 2:
            vaga_candidato = 'Cientista de Dados'

        # criando e lendo o arquivo .txt com o resumo dos respectivos candidatos
        arquivo_candidato = open(nome_candidato + str(id) + '.txt', 'w')
        arquivo_candidato.write(input("Digite o seu resumo: "))
        arquivo_candidato = open(
            nome_candidato + str(id) + '.txt', 'r', encoding="utf8")
        id += 1
        for linha in arquivo_candidato:
            linha = linha.lower()
        resumo_candidato = linha

        # adicionando as informações no dicionário geral
        lista_candidato = [vaga_candidato, resumo_candidato]
        dicionario_cadidatos[nome_candidato] = lista_candidato

        print('----------')
        # verificando se há mais cadidatos a serem cadastrados, ou se podemos seguir com o código
        verificacao = int(input(
            "Se você deseja fazer uma nova inscrição, digite [1].\nMas, se deseja verificar os cadidatos na base, digite [2]: "))
        if verificacao == 1:
            voltar == True
        elif verificacao == 2:
            voltar == False
    elif verificacao == 2:
        break

# dict que recebe todos os cadidatos que se candidataram a vaga de analista
dicionario_analistas = dict()
# dict que recebe todos os cadidatos que se candidataram a vaga de cientista
dicionario_cientista = dict()
# dict que recebe os cadidatos que se candidataram a vaga de analista e possuem as palvaras chaves no resumo
dic_analista_ok = dict()
# dict que recebe os cadidatos que se candidataram a vaga de cientista e possuem as palvaras chaves no resumo
dic_cientista_ok = dict()
count_analista = 0  # qnt de candidatos que se cadidataram para vaga de analista
count_cientista = 0  # qnt de candidatos que se cadidataram para vaga de cientista
# qnt de candidatos que se cadidataram para vaga de analista e possuem as palavras chave no resumo
count_analista_requisito = 0
# qnt de candidatos que se cadidataram para vaga de cientista e possuem as palavras chave no resumo
count_cientista_requisito = 0

# verificando a vaga que os cadidatos se cadastraram (no caso, analista de dados)
for chave, valor in dicionario_cadidatos.items():
    if 'Analista' in valor[0]:
        count_analista += 1
        dicionario_analistas.update({chave: valor})
        # verificando se há as palavras chaves no resumo dos candidatos q se cadastraram para vaga de analista
        for chave, valor in dicionario_analistas.items():
            if 'python' in valor[1] or 'powerbi' in valor[1] or 'sql' in valor[1] or 'boa comunicação' in valor[1]:
                count_analista_requisito += 1
                dic_analista_ok.update({chave: valor})

    # verificando a vaga que os cadidatos se cadastraram (no caso, cientista de dados)
    elif 'Cientista' in valor[0]:
        count_cientista += 1
        dicionario_cientista.update({chave: valor})
        # verificando se há as palavras chaves no resumo dos candidatos q se cadastraram para vaga de cientista
        for chave, valor in dicionario_cientista.items():
            if 'python' in valor[1] or 'banco de dados' in valor[1] or 'machine learning' in valor[1] or 'resolução de problemas' in valor[1] or 'estatística' in valor[1]:
                count_cientista_requisito += 1
                dic_cientista_ok.update({chave: valor})

print('----------')

# trazendo a contagem de cadidatos e os respectivos cadidatos para a vaga (no caso, analista de dados)
print(
    f'A quantidade de cadidatos cadastrado para vaga de Analista de Dados são: {count_analista}.\nSegue abaixo os cadidatos:')
for chave in dicionario_analistas:
    print(
        f'Cadidato: {[chave]}.\nVaga: {dicionario_analistas[chave][0]}.\nResumo: {dicionario_analistas[chave][1]}')

print('----------')
# trazendo a contagem de cadidatos e os respectivos cadidatos para a vaga que atendem os requisitos (palavras chaves no resumo)
print(
    f'A quantidade de cadidatos cadastrado para vaga de Analista de Dados que atende os requisitos são: {count_analista_requisito}.\nSegue abaixo os cadidatos:')
for chave in dic_analista_ok:
    print(
        f'Cadidato: {[chave]}.\nVaga: {dic_analista_ok[chave][0]}.\nResumo: {dic_analista_ok[chave][1]}')

print('----------')
# trazendo a contagem de cadidatos e os respectivos cadidatos para a vaga (no caso, cientista de dados)
print(
    f'A quantidade de cadidatos cadastrado para vaga de Cientista de Dados são: {count_cientista}.\nSegue abaixo os cadidatos:')
for chave in dicionario_cientista:
    print(
        f'Cadidato: {[chave]}.\nVaga: {dicionario_cientista[chave][0]}.\nResumo: {dicionario_cientista[chave][1]}')

print('----------')
# trazendo a contagem de cadidatos e os respectivos cadidatos para a vaga que atendem os requisitos (palavras chaves no resumo)
print(
    f'A quantidade de cadidatos cadastrado para vaga de Cientista de Dados que atende os requisitos são: {count_cientista_requisito}.\nSegue abaixo os cadidatos:')
for chave in dic_cientista_ok:
    print(
        f'Cadidato: {[chave]}.\nVaga: {dic_cientista_ok[chave][0]}.\nResumo: {dic_cientista_ok[chave][1]}')
