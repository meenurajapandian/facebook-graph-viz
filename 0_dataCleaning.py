import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

G1 = nx.Graph()
with open("facebook/0.edges", "r") as f:
    content = f.readlines()
    for x in content:
        y = str.split(x)
        G1.add_edge(int(y[0]), int(y[1]))

main_node = [(0, b) for b in G1.nodes()]
G1.add_edges_from(main_node)

G2 = nx.Graph()
with open("facebook/414.edges", "r") as f:
    content = f.readlines()
    for x in content:
        y = str.split(x)
        G2.add_edge(int(y[0]), int(y[1]))

main_node = [(414, b) for b in G2.nodes()]
G2.add_edges_from(main_node)

#print(nx.number_of_nodes(G2))

G = nx.compose(G1, G2)

#print(sorted(nx.common_neighbors(G,0,414)))
#print(nx.number_of_nodes(G))

with open("facebook/0.circles", "r") as f:
    content = f.readlines()
    circle = 1
    for x in content:
        y = str.split(x)
        for uy in range(0,(len(y)-1)):
            try:
                G.nodes[int(y[uy+1])]['Circle0']= circle
            except KeyError:
                pass

        circle = circle + 1

G.nodes[0]['Circle0'] = 0


with open("facebook/414.circles", "r") as f:
    content = f.readlines()
    circle = 1
    for x in content:
        y = str.split(x)
        for uy in range(0,(len(y)-1)):
            try:
                G.nodes[int(y[uy+1])]['Circle1']=circle
            except KeyError:
                pass

        circle = circle + 1

G.nodes[414]['Circle1'] = 0

# common_circle0 = []
# common_circle1=[]
# for u in G.nodes():
#     if len(G.nodes[u]['Circle0']) > 1:
#         common_circle0.append(G.nodes[u]['Circle0'])
#
#     if len(G.nodes[u]['Circle1']) > 1:
#         common_circle1.append(G.nodes[u]['Circle1'])


del G1
del G2

for u in G.nodes():
    try:
        G.nodes[u]['Circle'] = G.nodes[u]['Circle0']
        G.nodes[u]['User'] = 0
    except:
        try:
            G.nodes[u]['Circle'] = G.nodes[u]['Circle1']
            G.nodes[u]['User'] = 1
        except:
            if G.has_edge(0,u):
                G.nodes[u]['User'] = 0
            else:
                G.nodes[u]['User'] = 1

L = G.copy()

for circle0 in range(1, 22):
    merge = None
    for u in G.nodes():
        try:
            if G.nodes[u]['Circle0'] == circle0:
                if merge is None:
                    merge = u
                else:
                    L = nx.contracted_nodes(L,merge,u)
        except KeyError:
            pass


#print(nx.number_of_nodes(L))
#temp = L.copy()

for circle1 in range(1, 8):
    merge = None
    for u in G.nodes():
        try:
            if G.nodes[u]['Circle1'] == circle1:
                if merge is None:
                    merge = u
                else:
                    L = nx.contracted_nodes(L,merge,u)
        except KeyError:
            pass


#print(nx.number_of_nodes(L))

colors = ['#000000','#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075']
color_map = []

#L.remove_node(0)
#L.remove_node(414)

for u in L.nodes():
    try:
        del L.nodes[u]['contraction']
    except:
        pass


for u in L.nodes():
    try:
        color_map.append(colors[L.nodes[u]['Circle']])
        L.nodes[u]['Color'] = colors[L.nodes[u]['Circle']]
    except:
        color_map.append('#a9a9a9')
        L.nodes[u]['Color'] = '#a9a9a9'


Sp_Lay = nx.spring_layout(L,pos={0:(0,0),414:(8,8)}, fixed = [0,414])
#nx.set_node_attributes(L,'Location',Sp_Lay)
#Sp_Lay = nx.spring_layout(L)

for u in L.nodes():
    L.nodes[u]['Location'] = list(Sp_Lay[u])



nx.write_gml(G,"facebook.gml")
nx.write_gml(L,"facebook_reduced.gml")
nx.draw(L, pos = Sp_Lay, node_color = color_map, with_labels = True)
#plt.show()
