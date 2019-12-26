import networkx as nx


G = nx.read_gml("facebook_final_colors_edited.gml", label='id')

f = open("facebook_final.dot","w+")
f.write("strict graph {\n") #Strict graph stuff

for u in G.nodes():
    if u == '0' or u == '414':
        f.write(str(u) + "[label=\"J\",")
        f.write("width = 0.3,")
    else:
        f.write(str(u)+"[label=\"\",")

    f.write("color=\""+str(G.nodes[u]['Fill'])+"\",")
    f.write("fillcolor=\"" + str(G.nodes[u]['Color']) + "\",")
    f.write("pos=\"" + str(G.nodes[u]['Location'][0]) + "," + str(G.nodes[u]['Location'][1]) + "!\"")
    f.write("];"+'\n')

for u,v in G.edges():
    f.write(str(u) + ' -- ' + str(v) + '\n')

f.write("}")

f.close()