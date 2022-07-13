#--------------------------------------------#
#                 CONTRATADO!                #

# criando o dicionário inicial para cadastro geral dos candidatos
dicionario_cadidatos = dict()

while True:  # entrando no programa
    voltar = True
    verificacao = input(
        "Se você deseja fazer uma nova inscrição, digite [1].\nMas, se deseja verificar os cadidatos na base, digite [2]: ")
    if verificacao == '1' or verificacao == '2':
        verificacao = int(verificacao)
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
            'Digite o nome completo do candidato: ').lower()
        lista_candidato = []

        vaga_candidato_escolha = input(
            'Digite [1] para vaga de Analista de Dados ou digite [2] para vaga de Cientista de Dados: ').lower()
        if vaga_candidato_escolha == '1':
            vaga_candidato = 'analista de dados'
        elif vaga_candidato_escolha == '2':
            vaga_candidato = 'cientista de dados'

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
    if 'analista' in valor[0]:
        count_analista += 1
        dicionario_analistas.update({chave: valor})
        # verificando se há as palavras chaves no resumo dos candidatos q se cadastraram para vaga de analista
        for chave, valor in dicionario_analistas.items():
            if 'python' in valor[1] or 'powerbi' in valor[1] or 'sql' in valor[1] or 'boa comunicação' in valor[1]:
                count_analista_requisito += 1
                dic_analista_ok.update({chave: valor})

    # verificando a vaga que os cadidatos se cadastraram (no caso, cientista de dados)
    elif 'cientista' in valor[0]:
        count_cientista += 1
        dicionario_cientista.update({chave: valor})
        # verificando se há as palavras chaves no resumo dos candidatos q se cadastraram para vaga de cientista
        for chave, valor in dicionario_cientista.items():
            if 'python' in valor[1] or 'banco de dados' in valor[1] or 'machine learning' in valor[1] or 'resolução de problemas' in valor[1] or 'estatística' in valor[1]:
                count_cientista_requisito += 1
                dic_cientista_ok.update({chave: valor})


print('----------')
# trazendo a contagem de cadidatos e os respectivos cadidatos para a vaga (no caso, analista de dados)
print('A quantidade de cadidatos cadastrado para vaga de Analista de Dados são: {}.\nSegue abaixo os cadidatos:\n{}'.format(
    count_analista, dicionario_analistas))
# trazendo a contagem de cadidatos e os respectivos cadidatos para a vaga que atendem os requisitos (palavras chaves no resumo)
print('A quantidade de cadidatos cadastrado para vaga de Analista de Dados que atende os requisitos são: {}.\nSegue abaixo os cadidatos:\n{}'.format(
    count_analista_requisito, dic_analista_ok))

print('----------')
# trazendo a contagem de cadidatos e os respectivos cadidatos para a vaga (no caso, cientista de dados)
print('A quantidade de cadidatos cadastrado para vaga de Cientísta de Dados são: {}.\nSegue abaixo os cadidatos:\n{}'.format(
    count_cientista, dicionario_cientista))
# trazendo a contagem de cadidatos e os respectivos cadidatos para a vaga que atendem os requisitos (palavras chaves no resumo)
print('A quantidade de cadidatos cadastrado para vaga de Cientísta de Dados que atende os requisitos são: {}.\nSegue abaixo os cadidatos:\n{}'.format(
    count_cientista_requisito, dic_cientista_ok))
