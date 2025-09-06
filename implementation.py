import container
import matplotlib.pyplot as plt
import networkx as nx

def BFS(frontier, legal):
    explored = []
    parent = {(0, 0, 0, 0): None}
    solution = []
    while(frontier.get_size() != 0):
        n = frontier.Dequeue().data

        if(frontier.GoalTest(n)):
            print(explored)
            return solution
        
        explored.append(n)

        for a in frontier.Actions(n):
            s_p = frontier.Transition(a, n)

            if(frontier.Retrieve(s_p) == None and s_p not in explored):
                frontier.Enqueue(s_p)
                #if(s_p in legal): #It's good to have this check
                #print(s_p)

    

    return None


def main():
    list_to_pass = [(0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1),(0,1,0,0),(0,1,0,1),(0,1,1,0),(0,1,1,1),(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,0,1,1),(1,1,0,0),(1,1,0,1),(1,1,1,0),(1,1,1,1)]
    #0, 2, 4, 5, 7, 8, 10, 11, 13, 15
    legal = [(0,0,0,0),(0,0,1,0), (0,1,0,0), (0,1,0,1), (0,1,1,1), (1,0,0,0), (1,0,1,0), (1,0,1,1), (1,1,0,1), (1,1,1,1)]


    graph = container.Graph(list_to_pass[0], list_to_pass[1], list_to_pass[2], list_to_pass[3],  list_to_pass[4] , list_to_pass[5], list_to_pass[6], list_to_pass[7], list_to_pass[8], list_to_pass[9], list_to_pass[10], list_to_pass[11], list_to_pass[12], list_to_pass[13], list_to_pass[14], list_to_pass[15])
    graph.AddEdge(0, list_to_pass[9])
    graph.AddEdge(0, list_to_pass[5])
    graph.AddEdge(0, list_to_pass[3])
    graph.AddEdge(0, list_to_pass[14])
    graph.AddEdge(2, list_to_pass[11])
    graph.AddEdge(2, list_to_pass[7])
    graph.AddEdge(2, list_to_pass[3])
    graph.AddEdge(4, list_to_pass[12])
    graph.AddEdge(4, list_to_pass[6])
    graph.AddEdge(4, list_to_pass[5])
    graph.AddEdge(5, list_to_pass[0])
    graph.AddEdge(5, list_to_pass[4])
    graph.AddEdge(7, list_to_pass[2])
    graph.AddEdge(7, list_to_pass[4])
    graph.AddEdge(7, list_to_pass[6])
    graph.AddEdge(8, list_to_pass[13])
    graph.AddEdge(8, list_to_pass[11])
    graph.AddEdge(8, list_to_pass[9])
    graph.AddEdge(10, list_to_pass[15] )
    graph.AddEdge(10, list_to_pass[11])
    graph.AddEdge(11, list_to_pass[2])
    graph.AddEdge(11, list_to_pass[8])
    graph.AddEdge(11, list_to_pass[10])
    graph.AddEdge(13, list_to_pass[4])
    graph.AddEdge(13, list_to_pass[8])
    graph.AddEdge(13, list_to_pass[12])
    graph.printGraph()

    new_container = container.Container(graph, graph.Adjacency[0].Access(0), graph.Adjacency[15].Access(0))

    solution = BFS(new_container, legal)


    #plot_graph_from_class(graph)
    print(solution)


def plot_graph_from_class(graph):
    # Create an undirected graph
    G = nx.Graph()

    # Add nodes (0..len(Adjacency)-1)
    G.add_nodes_from(range(len(graph.Adjacency)))

    # Collect edges from your Graph object
    for v1, adj_list in enumerate(graph.Adjacency):
        current = adj_list.head  # assuming LinkedList has 'head'
        while current:
            v2 = current.data
            # For undirected graph, ensure no duplicates
            if not G.has_edge(v1, v2):
                G.add_edge(v1, v2)
            current = current.next

    # Draw the graph
    pos = nx.spring_layout(G, seed=42)  # nice layout
    nx.draw(
        G, pos, with_labels=True,
        node_color="lightblue", node_size=800,
        font_size=10, font_weight="bold",
        edge_color="gray"
    )
    plt.title("Undirected Graph Visualization")
    plt.show()



if __name__ == '__main__':
    main()