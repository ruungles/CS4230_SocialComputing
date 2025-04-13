"""
Name : NetworkX - Directed Graph to Undirected Graph (Twitter dataset)
Date Created : April 9th, 2025
Author : Ryan Larson
Synopsis : This module takes a direct network (Twitter dataset) 
Inputs : Twitter Directed Network
Outputs : Degree and Closeness and Betweenness Centraility Values
Globals : 
"""

import networkx as nx
from matplotlib import pyplot as plt
import pickle
import statistics

def twitter_directed_to_undirected (file):
    print ("Starting directed graph to undirected graph representatin ...")
    """
    """
    read_adjacent_list(file,'directed_graph.pkl')

    """
    """
    with open ("directed_graph.pkl", 'rb') as f:
        directed_g = pickle.load(f)

    """
    """
    undirected_g = directed_g.to_undirected()
    largest_component = identify_largest_component(undirected_g)
    generatefile(largest_component, 'undirected_graph_largest_comp.pkl')

    """
    """
    degree, closeness, betweenness = generate_centrality_values(largest_component)
    degree_values = list(degree.values())
    closeness_values = list(closeness.values())
    betweenness_values = list(betweenness.values())

    plt.figure(figsize = (15, 5))

    plt.subplot(1,3,1)
    plt.hist(degree_values,bins = 20, edgecolor='black')
    plt.title("Degree Centrality")
    plt.xlabel("Centrality Value")
    plt.ylabel("Frequency")

    plt.subplot(1, 3, 2)
    plt.hist(closeness_values, bins=20, edgecolor='black')
    plt.title("Closeness Centrality")
    plt.xlabel("Centrality Value")

    plt.subplot(1, 3, 3)
    plt.hist(betweenness_values, bins=20, edgecolor='black')
    plt.title("Betweenness Centrality")
    plt.xlabel("Centrality Value")

    plt.tight_layout()

    plt.savefig("centrality_histograms.png", dpi=300)

    """
    """
    top_200_degree = sorted(degree.items(), key=lambda x: x[1], reverse=True)[:200]
    top_200_degree_values = [value for node, value in top_200_degree]
    mean_degree = statistics.mean(top_200_degree_values)
    median_degree = statistics.median(top_200_degree_values)
    stdev_degree = statistics.stdev(top_200_degree_values)

    top_200_closeness = sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:200]
    top_200_closeness_values = [value for node, value in top_200_closeness]
    mean_closeness = statistics.mean(top_200_closeness_values)
    median_closeness = statistics.median(top_200_closeness_values)
    stdev_closeness = statistics.stdev(top_200_closeness_values)

    top_200_betweenness = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:200]
    top_200_betweenness_values = [value for node, value in top_200_betweenness]
    mean_betweenness = statistics.mean(top_200_betweenness_values)
    median_betweenness = statistics.median(top_200_betweenness_values)
    stdev_betweenness = statistics.stdev(top_200_betweenness_values)

    output_text = (
        f'Calculated Degree Statistics:\n'
        f'Mean: {mean_degree}\n'
        f'Median: {median_degree}\n'
        f'Standard Deviation: {stdev_degree}\n \n'
        f'Calculated Closeness Statistics:\n'
        f'Mean: {mean_closeness}\n'
        f'Median: {median_closeness}\n'
        f'Standard Deviation: {stdev_closeness}\n \n'
        f'Calculated Betweenness Statistics:\n'
        f'Mean: {mean_betweenness}\n'
        f'Median: {median_betweenness}\n'
        f'Standard Deviation: {stdev_betweenness}\n'
    )
    with open("statisitc.txt", "w") as file:
        file.write(output_text)

    """
    """
    return

def triatic_census(file):
    print('Triadic Census ... ')
    read_adjacent_list(file, 'triadic_directed_graph.plk')
    with open ("triadic_directed_graph.plk", 'rb') as f:
        directed_g = pickle.load(f)
    census = nx.triadic_census(directed_g)
    with open('triadic_census.txt', 'w') as file:
        file.write(str(census))
    print("Done.")

def generate_centrality_values (graph):
    print('Calculating degree, closeness, betweenness centralities ...')
    degree_cent = nx.degree_centrality(graph)
    closeness_cent = nx.closeness_centrality(graph)
    betweenness_cent = nx.betweenness_centrality(graph)
    print('Done.')
    return degree_cent, closeness_cent, betweenness_cent

def identify_largest_component (graph):
    print('Identifying largest component in network...')
    largest_component = max(nx.connected_components(graph), key=len)
    sub_graph = graph.subgraph(largest_component).copy()
    print('Done.')
    return sub_graph

def read_adjacent_list (file, file_name):
    graph = nx.read_adjlist(file, create_using=nx.DiGraph)
    generatefile(graph, file_name)

def generatefile (graph, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(graph, f)

if __name__ == "__main__" :
    #G_rand = nx.gnp_random_graph(1000, p=0.2, directed=True)
    #nx.write_adjlist(G_rand,'data\\rand.txt')

    file = 'twitter_combined.txt'
    twitter_directed_to_undirected(file)
    triatic_census(file)