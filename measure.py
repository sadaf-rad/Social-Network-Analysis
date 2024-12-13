import networkx as nx
import numpy as np

#display and measure graph info
def display_info(sn_graph):
    try:
        print(nx.info(sn_graph))
        #Betweennss
        betweenness = nx.betweenness_centrality(sn_graph, normalized=True).values()
        print("betweeness centrality (maximum): ", np.max(np.array(list(betweenness))))
        print("betweenness centrality (average): ", np.mean(np.array(list(betweenness))))
        #Closeness
        closeness = nx.closeness_centrality(sn_graph).values()
        print("closeness centrality (maximum): ", np.max(np.array(list(closeness))))
        print("closeness centrality (average): ", np.mean(np.array(list(closeness))))
        #Any seprate node?
        print("Any seprate node: ", nx.number_of_isolates(sn_graph))
        #BigestSubgraph
        subgraphs = sorted(nx.connected_component_subgraphs(sn_graph), key=len, reverse=True)
        print("Biggest sub component : ", subgraphs[0].order(), subgraphs[0].size())
        #diameter
        diameter=nx.diameter(sn_graph)
        print("graph diameter : ",diameter)
    except :
        print("Measure Error - diameter!!! ")

