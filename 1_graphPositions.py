import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

L = nx.read_gml("facebook_reduced.gml")
G = nx.read_gml("facebook.gml")

color_map = []
for u in L.nodes():
    color_map.append(L.nodes[u]['Color'])
    try:
        if L.nodes[u]['User'] == 0:
                pos = L.nodes[u]['Location']
                pos[0] = 2*pos[0]
                pos[1] = 2*pos[1]
                L.nodes[u]['Location'] = pos
    except:
        print(u)
        print(L.nodes[u])

for u in L.nodes():
    color_map.append(L.nodes[u]['Color'])
    try:
        if L.nodes[u]['User'] == 1:
                pos = L.nodes[u]['Location']
                pos[0] = 1.5*pos[0]
                pos[1] = 1.5*pos[1]
                L.nodes[u]['Location'] = pos
    except:
        print(u)
        print(L.nodes[u])

#nx.draw(L,pos=nx.get_node_attributes(L,'Location'), node_color = color_map)
#plt.show()

circle0_pos = [None]*21
circle1_pos = [None]*6

for u in L.nodes():
    try:
        circle = L.nodes[u]['Circle']
        if L.nodes[u]['User'] == 0:
            circle0_pos[circle] = L.nodes[u]['Location']
        else:
            circle1_pos[circle] = L.nodes[u]['Location']
    except KeyError:
        pass


circle0_members = [[] for i in range(21)]
circle1_members = [[] for i in range(6)]

for u in G.nodes():
    try:
        circle = G.nodes[u]['Circle']
        if G.nodes[u]['User'] == 0:
            circle0_members[circle].append(u)
        else:
            circle1_members[circle].append(u)
    except KeyError:
        pass

for u in L.nodes():
    G.nodes[u]['Location'] = L.nodes[u]['Location']

for i in range(21):
    if len(circle0_members[i]) > 1:
        mem_len = len(circle0_members[i])
        x = np.random.normal(0, (0.17*np.log(mem_len)), mem_len)
        y = np.random.normal(0, (0.17*np.log(mem_len)), mem_len)
        for sg in range(0,len(circle0_members[i])):
            G.nodes[circle0_members[i][sg]]['Location'] = [circle0_pos[i][0]+x[sg], circle0_pos[i][0]+y[sg]]

for i in range(6):
    if len(circle1_members[i]) > 1:
        mem_len = len(circle1_members[i])
        x = np.random.normal(0, (0.17*np.log(mem_len)), mem_len)
        y = np.random.normal(0, (0.17*np.log(mem_len)), mem_len)
        for sg in range(0,len(circle1_members[i])):
            G.nodes[circle1_members[i][sg]]['Location'] = [circle1_pos[i][0]+x[sg], circle1_pos[i][0]+y[sg]]


# for i in range(21):
#     if len(circle0_members[i]) > 1:
#         SG = G.subgraph(circle0_members[i]).copy()
#         sg_pos = nx.spring_layout(SG,center=[0,0])
#         for s in SG.nodes():
#             p = sg_pos[s]
#             p[0] = p[0]+circle0_pos[i][0]
#             p[1] = p[1]+circle0_pos[i][0]
#             G.nodes[s]['Location'] = p
#
# for i in range(6):
#     if len(circle1_members[i]) > 1:
#         SG = G.subgraph(circle1_members[i]).copy()
#         sg_pos = nx.spring_layout(SG,center=[0,0])
#         for s in SG.nodes():
#             p = sg_pos[s]
#             p[0] = p[0]+circle1_pos[i][0]
#             p[1] = p[1]+circle1_pos[i][0]
#             G.nodes[s]['Location'] = p
#

colors = ['#000000','#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075']
color_map = []
for u in G.nodes():
    try:
        color_map.append(colors[G.nodes[u]['Circle']])
        G.nodes[u]['Color'] = colors[G.nodes[u]['Circle']]
    except:
        color_map.append('#a9a9a9')
        G.nodes[u]['Color'] = '#a9a9a9'

for u in G.nodes():
    if G.nodes[u]['User'] == 1:
        try:
            if G.nodes[u]['Circle']==1:
                G.nodes[u]['Location'][1] = G.nodes[u]['Location'][1] + 1.5
            elif G.nodes[u]['Circle'] == 4:
                G.nodes[u]['Location'][1] = G.nodes[u]['Location'][1] - 2
            elif G.nodes[u]['Circle'] == 2:
                G.nodes[u]['Location'][1] = G.nodes[u]['Location'][1] - 0.9
            else:
                None
        except:
            pass

for u in G.nodes():
    if G.nodes[u]['User'] == 0:
        try:
            if G.nodes[u]['Circle'] == 6:
                G.nodes[u]['Location'][1] = G.nodes[u]['Location'][1] - 2
                G.nodes[u]['Location'][0] = G.nodes[u]['Location'][0] + 1.5
            elif G.nodes[u]['Circle'] == 16:
                G.nodes[u]['Location'][0] = G.nodes[u]['Location'][0] + 0.8
                G.nodes[u]['Location'][1] = G.nodes[u]['Location'][1] + 0.3
            elif G.nodes[u]['Circle'] == 8:
                G.nodes[u]['Location'][0] = G.nodes[u]['Location'][0] - 1.75
                G.nodes[u]['Location'][1] = G.nodes[u]['Location'][1] + 1
            elif G.nodes[u]['Circle'] == 10:
                # G.nodes[u]['Location'][0] = G.nodes[u]['Location'][0] - 1.75
                G.nodes[u]['Location'][1] = G.nodes[u]['Location'][1] -2
            elif G.nodes[u]['Circle'] == 4:
                G.nodes[u]['Location'][0] = G.nodes[u]['Location'][0] + 0.2
                G.nodes[u]['Location'][1] = G.nodes[u]['Location'][1] + 0.7
            elif G.nodes[u]['Circle'] == 14:
                # G.nodes[u]['Location'][0] = G.nodes[u]['Location'][0] + 0.2
                G.nodes[u]['Location'][1] = G.nodes[u]['Location'][1] - 0.7
            elif G.nodes[u]['Circle'] == 12:
                # G.nodes[u]['Location'][0] = G.nodes[u]['Location'][0] + 0.2
                G.nodes[u]['Location'][1] = G.nodes[u]['Location'][1] - 0.8
            else:
                None
        except:
            pass


G.nodes['0']['Location'][0] = 3.57418
G.nodes['0']['Location'][1] = 3.30811
G.nodes['414']['Location'][0] = 9.44588
G.nodes['414']['Location'][1] = 10.2742


nx.draw_networkx_nodes(G, pos = nx.get_node_attributes(G,'Location'), node_color=color_map)
plt.show()
nx.draw(G, pos = nx.get_node_attributes(G,'Location'), node_color = color_map, with_labels=True)
#nx.draw(L,pos=nx.get_node_attributes(L,'Location'), node_color = color_map)
plt.show()

nx.write_gml(G,"facebook_final.gml")