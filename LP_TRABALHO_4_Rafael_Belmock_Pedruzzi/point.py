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

# Função que calcula o centro de massa de um grupo
# parâmetros: a lista de grupos, a lista de pontos e a posição do grupo na lista de grupos.
# retorno: lista representando o ponto do centro de massa do grupo.
# condição: todos os pontos devem ter o mesmo número de dimensões.
# pós-condição: lista de grupos inalterada.
def centro_Massa(g, points, pos):
    c = [] # centro de massa.
    nd = range(len(points[pos])) # iterador contendo o número de dimensões.
    np = range(len(g[pos]))      # iterador contendo o número de pontos no grupo.

    # Inicializando c:
    for i in nd:
        c.append(0)

    # Realizando o somatório de todos os pontos do grupo em c:
    for i in np:
        p = g[pos][i] -1

        for j in nd:
            c[j] += points[p][j]

    # Dividindo cada coordenada de c pelo número de elementos no grupo:
    for i in nd:
        c[i] /= len(g[pos])

    return c

# Função que calcula a SSE de um agrupamento
# parâmetros: a lista de grupos e a lista de pontos.
# retorno: valor da SSE do agrupamento.
# condição: todos os pontos devem ter o mesmo número de dimensões.
# pós-condição: estruturas inalteradas.
def sse(g, points):
    sse = 0 # resultado da sse.

    for i in range(len(g)): # para cada grupo i na lista de grupos.
        cMassa = centro_Massa(g,points,i)
        groupSum = 0 # auxiliar para o somatório de cada grupo.

        for j in range(len(g[i])): # para cada elemento j do grupo i.
            d = dist_Points(points[g[i][j]-1], cMassa) # d = distância entre o ponto j e o centro de massa do grupo.
            groupSum += d * d # atualizando somatório do grupo atual.

        sse += groupSum # SSE será a soma de todos os somatórios parciais.

    return sse