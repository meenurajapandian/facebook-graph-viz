import networkx as nx
import random
from networkx.algorithms.community import greedy_modularity_communities

G = nx.read_gml("facebook_final_colors_edited.gml")
communities = list(greedy_modularity_communities(G))

col_list = []
colors = ['#e51b4c','#3cb44b','#fdf170','#3a58a8','#f79237','#863d97','#56c9ea','#d466a7','#c2d82e','#f9bebe','#7f8133','#f79237','#9a6427','#fdf170','#7f8133','#d4e6ab','#7f8133','#c2d82e']
fill_colors =['#7f1637','#1e4c25','#968c43','#20365b','#8e5322','#51275b','#327482','#602f51','#687130','#806261','#47481e','#8e5322','#5a3a18','#968c43','#47481e','#6a7356','#47481e','#687130']

for comm in communities:
    nods = list(comm)
    col = G.nodes[nods[0]]['Color']
    fcol = G.nodes[nods[0]]['Fill']
    temp = 0
    while col == '#000000' or col == '#bfbfbf' or col in col_list:
        temp = temp + 1
        try:
            col = G.nodes[nods[temp]]['Color']
            fcol = G.nodes[nods[temp]]['Fill']
        except IndexError:
            r = random.randint(0, 17)
            col = colors[r]
            fcol = fill_colors[r]

    col_list.append(col)
    for c in list(comm):
        if (c != '0') and (c != '414'):
            G.nodes[c]['Color'] = col
            G.nodes[c]['Fill'] = fcol
        else:
            print(c)

f = open("facebook_final_comm.dot","w+")
f.write("strict graph {\n") #Strict graph stuff

for u in G.nodes():
    f.write(str(u)+"[label=\"\",")
    f.write("color=\""+str(G.nodes[u]['Fill'])+"\",")
    f.write("fillcolor=\"" + str(G.nodes[u]['Color']) + "\",")
    f.write("pos=\"" + str(G.nodes[u]['Location'][0]) + "," + str(G.nodes[u]['Location'][1]) + "!\"")
    f.write("];"+'\n')

for u,v in G.edges():
    f.write(str(u) + ' -- ' + str(v) + '\n')

f.write("}")

f.close()