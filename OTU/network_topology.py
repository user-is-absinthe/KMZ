import networkx
import matplotlib.pyplot
import os


PATH_TO_CSV = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/!_all.csv'
PATH_TO_IMG = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/'

try:
    os.makedirs(PATH_TO_IMG)
except FileExistsError:
    pass


def main():
    data = csv_reader(
        path=PATH_TO_CSV,
        separator=';',
        headline=True,
        encode='utf-8'
    )
    # print(data)
    from_to_list = list(set(data['from'] + data['to']))
    # to_list = list(set(data['to']))
    graph = networkx.Graph()
    graph.add_nodes_from(from_to_list)
    from_to_list = list()
    for index_line in range(len(data['from'])):
        graph.add_edge(data['from'][index_line], data['to'][index_line])
        from_to_list.append((data['from'][index_line], data['to'][index_line]))

    # position = networkx.spring_layout(graph)
    # networkx.draw(graph, position)
    # matplotlib.pyplot.show()
    # position = networkx.spring_layout(graph, scale=2)
    # networkx.draw_networkx(graph, position)
    # matplotlib.pyplot.show()
    connectivity_list = list()
    for node in graph.nodes:
        connectivity_list.append(networkx.len(connectivity_list)(graph, node))

    mini_graphs_list = list()
    for connect in connectivity_list:
        # temp_graph = networkx.Graph()
        temp_graph = networkx.DiGraph()
        temp_graph.add_nodes_from(connect)
        for user in connect:
            for u in from_to_list:
                if u[0] == user:
                    temp_graph.add_edge(u[0], u[1])
        mini_graphs_list.append(temp_graph)
        # temp_graph.clear()

    for index, mini_graph in enumerate(mini_graphs_list):
        # print(len(mini_graph.edges), len(set(mini_graph.edges)))
        if len(mini_graph.edges) != len(set(mini_graph.edges)):
            print(len(mini_graph.edges), len(set(mini_graph.edges)))

        # position = networkx.spring_layout(mini_graph)
        # edges = networkx.draw_networkx_edges(
        #     mini_graph, position, arrowstyle='->'
        # )
        # networkx.draw(edges)
        networkx.draw(mini_graph, with_labels=True, arrows=True)
        # matplotlib.pyplot.show()
        # break
        matplotlib.pyplot.savefig(PATH_TO_IMG + str(index) + '.png', format='png')
        matplotlib.pyplot.close()
        # break
    pass


def csv_reader(path, separator, headline=False, encode='utf-16'):
    with open(path, 'r', encoding=encode) as file:
        csv_file = file.readlines()
    csv_file = [this.strip() for this in csv_file]
    if headline:
        keys_to_dict = csv_file[0].split(separator)
    else:
        keys_to_dict = [i for i in range(0, len(csv_file[0].split(separator)))]

    opened_csv = dict()
    for key in keys_to_dict:
        opened_csv[key] = list()

    for line in csv_file:
        if headline and line == csv_file[0]:
            continue
        separated_line = line.split(separator)
        for index in range(len(keys_to_dict)):
            opened_csv[keys_to_dict[index]].append(separated_line[index])

    return opened_csv


if __name__ == '__main__':
    main()
