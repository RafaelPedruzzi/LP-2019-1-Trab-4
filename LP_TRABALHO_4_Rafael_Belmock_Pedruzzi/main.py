# -------------------------------------------------------- #
# Linguagens de Programação - Prof. Flavio Varejão - 2019-1
# Segundo trabalho de implementação
#
# Aluno: Rafael Belmock Pedruzzi
#
# main.py: módulo main
# -------------------------------------------------------- #

from trabIO import *
from point import *

# Lendo a distância limite e a lista de pontos:
dist, points = read_Entry()

# Realizando o algoritimo de agrupamento:
g = make_Groups(dist,points)

# Calculando o SSE do agrupamento:
sse = sse(g,points)

# Imprimindo arquivos de saida:
print_Groups(g)
print_SSE(sse)

#print(points)
#print(g)