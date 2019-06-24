# -------------------------------------------------------- #
# Linguagens de Programação - Prof. Flavio Varejão - 2019-1
# Segundo trabalho de implementação
#
# Aluno: Rafael Belmock Pedruzzi
#
# trabIO.py: módulo responsável pelo tratamento de I/O dos arquivos:
#			 entrada.txt, distancia.txt, result.txt e saida.txt
# -------------------------------------------------------- #

# Função para leitura dos arquivos entrada.txt e distancia.txt
# retorno: a distância limite e uma lista contendo listas que representam cada ponto lido (a posição na lista indica a linha que foi lido).
def read_Entry():
    # Abrindo arquivo distancia.txt para obter a distância limite:
    f = open("./distancia.txt", "r")
    dist = float(f.read())
    f.close()

    # Abrindo arquivo entrada.txt para obter os pontos:
    points = [] # lista de pontos.
    f = open("./entrada.txt", "r")
    for line in f.readlines():
        points.append([float(x) for x in line.split()])
    f.close()

    return dist, points

# Funcão para impressão do arquivo saida.txt
# parâmetros: a lista de grupos.
# pós-condição: lista inalterada inalterada.
def print_Groups(g):
    # Criando arquivo de escrita:
    saida = open("saida.txt", "w")

    # Imprimindo cada grupo. Somente os identifiicadores são impressos, em ordem cressente e separados por espaços. grupos diferentes são separados por uma linha em branco.
    for i in range(len(g)):
        if i != 0:
            saida.write("\n\n")
        for j in range(len(g[i])):
            if j != 0:
                saida.write(" ")
            saida.write(str(g[i][j]))

    # Fechando arquivo:
    saida.close

# Funcão para impressão do arquivo result.txt
# parâmetros: valor da SSE do agrupamento.
def print_SSE(sse):
    # Criando arquivo de escrita:
    saida = open("result.txt", "w")

    # Imprimindo a SSE:
    saida.write('{0:.{1}f}'.format(sse, 4))

    saida.close