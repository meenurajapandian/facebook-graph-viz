import networkx as nx

G = nx.read_gml("facebook_final.gml")

colors = ['#000000','#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231',
          '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff',
          '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075']


for u in G.nodes():
    if G.nodes[u]['Color'] =='#e6194b': #red
        G.nodes[u]['Color'] = '#e51b4c'
        G.nodes[u]['Fill'] = '#7f1637'
    elif G.nodes[u]['Color'] == '#3cb44b': #green
        G.nodes[u]['Fill'] = '#1e4c25'
    elif G.nodes[u]['Color'] == '#ffe119':
        G.nodes[u]['Color'] = '#fdf170'
        G.nodes[u]['Fill'] = '#968c43'
    elif G.nodes[u]['Color'] == '#4363d8':
        G.nodes[u]['Color'] = '#3a58a8'
        G.nodes[u]['Fill'] = '#20365b'
    elif G.nodes[u]['Color'] == '#f58231':
        G.nodes[u]['Color'] = '#f79237'
        G.nodes[u]['Fill'] = '#8e5322'
    elif G.nodes[u]['Color'] == '#911eb4':
        G.nodes[u]['Color'] = '#863d97'
        G.nodes[u]['Fill'] = '#51275b'
    elif G.nodes[u]['Color'] == '#46f0f0':
        G.nodes[u]['Color'] = '#56c9ea'
        G.nodes[u]['Fill'] = '#327482'
    elif G.nodes[u]['Color'] == '#f032e6':
        G.nodes[u]['Color'] = '#d466a7'
        G.nodes[u]['Fill'] = '#602f51'
    elif G.nodes[u]['Color'] == '#bcf60c': #lime
        G.nodes[u]['Color'] = '#c2d82e'
        G.nodes[u]['Fill'] = '#687130'
    elif G.nodes[u]['Color'] == '#fabebe':
        G.nodes[u]['Color'] = '#f9bebe'
        G.nodes[u]['Fill'] = '#806261'
    elif G.nodes[u]['Color'] == '#008080': #teal
        G.nodes[u]['Color'] = '#7f8133'
        G.nodes[u]['Fill'] = '#47481e'
    elif G.nodes[u]['Color'] == '#e6beff':
        G.nodes[u]['Color'] = '#f79237'
        G.nodes[u]['Fill'] = '#8e5322'
    elif G.nodes[u]['Color'] == '#9a6324':
        G.nodes[u]['Color'] = '#9a6427'
        G.nodes[u]['Fill'] = '#5a3a18'
    elif G.nodes[u]['Color'] == '#fffac8':
        G.nodes[u]['Color'] = '#fdf170'
        G.nodes[u]['Fill'] = '#968c43'
    elif G.nodes[u]['Color'] == '#800000':
        G.nodes[u]['Color'] = '#7f8133'
        G.nodes[u]['Fill'] = '#47481e'
    elif G.nodes[u]['Color'] == '#aaffc3':
        G.nodes[u]['Color'] = '#d4e6ab'
        G.nodes[u]['Fill'] = '#6a7356'
    elif G.nodes[u]['Color'] == '#808000':
        G.nodes[u]['Color'] = '#7f8133'
        G.nodes[u]['Fill'] = '#47481e'
    elif G.nodes[u]['Color'] == '#000075':
        G.nodes[u]['Color'] = '#c2d82e'
        G.nodes[u]['Fill'] = '#687130'
    elif G.nodes[u]['Color'] == '#a9a9a9':
        G.nodes[u]['Color'] = '#bfbfbf'
        G.nodes[u]['Fill'] = '#757575'
    else:
        G.node[u]['Fill'] = '#000000'


nx.write_gml(G,"facebook_final_colors_edited.gml")


