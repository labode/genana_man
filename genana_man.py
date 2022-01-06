import networkx as nx
import sys
import csv
import nrrd


def read_csv(file):
    content = []

    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        i = 0
        for row in reader:
            if i == 0:
                i += 1
                continue
            else:
                i += 1
                content.append([row[0], row[1]])

    return content


def write_csv(data, target_file):
    filename = str(target_file) + ".csv"
    output_file = open(filename, "w")

    # Write header
    output_file.write("Id; Vertex Id; Man_Gen\n")

    for i in data:
        output_file.write(str(i[0]) + '; ' + str(i[1]) + '; ' + str(i[2]) + '\n')


def read_graph(file):
    dot_graph = nx.drawing.nx_pydot.read_dot(file)

    return dot_graph


def read_nrrd(file):
    data, header = nrrd.read(file)

    return data


def analyse(data, graph, nrrd_array):
    analysis = []

    for i in data:
        coordinates = graph.node[str(i[0])]['spatial_node']
        coordinates = coordinates.replace('"', '')
        coordinates = coordinates.split(' ')

        id_label = nrrd_array[int(coordinates[0]), int(coordinates[1]), int(coordinates[2])]

        result = [id_label, i[1]]
        analysis.append(result)

    return analysis


if __name__ == '__main__':
    try:
        genana_file = sys.argv[1]
        dot_file = sys.argv[2]
        nrrd_file = sys.argv[3]
        output_csv = sys.argv[4]

    except IndexError:
        sys.exit('Missing parameters \nPlease supply: generation file, dot graph, nrrd file,'
                 ' output file name')

    genana = read_csv(genana_file)
    nrrd_data = read_nrrd(nrrd_file)
    graph_data = read_graph(dot_file)

    results = analyse(genana, graph_data, nrrd_data)
    write_csv(results, output_csv)



