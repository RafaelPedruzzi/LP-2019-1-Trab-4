# -------------------------------------------------------- #
# Linguagens de Programação - Prof. Flavio Varejão - 2019-1
# Segundo trabalho de implementação
#
# Aluno: Rafael Belmock Pedruzzi
#
# point.py: módulo responsável pela implementação dos calculos e
#           estruturas feitos com pontos muldidimensionais
# -------------------------------------------------------- #

from math import *

# Função que calcula a distância euclidiana entre dois pontos
# parâmetros: duas listas, p1 e p2, representando os pontos.
# retorno: a distância euclidiana entre p1 e p2.
# pré-condição: p1 e p2 devem ter o mesmo número de dimensões.
def dist_Points(p1, p2):
    sum = 0
    for i in range(len(p1)):
        sub = p1[i] - p2[i]
        sum += sub * sub

    return sqrt(sum)

# Função que monta os grupos segundo o algoritimo de agrupamento por líder
# parâmetros: a distância limite entre um ponto e seu líder e a lista de pontos.
# retorno: uma lista contendo listas representando cada grupos formado (líder é o ponto na primeira posição da lista do grupo) e a lista de pontos.
# condição: todos os pontos devem ter o mesmo número de dimensões.
# pós-condição: lista de pontos inalterada.
def make_Groups(dist, points):
    g = [[1]] # adicionando o primeiro ponto como líder do primeiro grupo.

    for i in range(1,len(points)): # para cada ponto i (exceto o primeiro) na lista de pontos.
        for j in range(len(g)): # para cada grupo j em g.

            p = g[j][0] - 1 # posição do líder do grupo j em points.
            lider = True

            # Verificando se a distância do ponto i ao lider do grupo j é menor ou igual a dist. Caso verdadeiro, i é adicionado a j:
            if dist_Points(points[i], points[p]) <= dist:
                g[j].append(i+1)
                lider = False
                break
        else: # caso i seja líder, um novo grupo será criado para i.
            g.append([i+1])

    return g