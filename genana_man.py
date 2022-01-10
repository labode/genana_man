import argparse
import nrrd


def write_csv(data, target_file):
    filename = str(target_file) + ".csv"
    output_file = open(filename, "w")

    # Write header
    output_file.write("Id; Man_Gen\n")

    for i in data:
        output_file.write(str(i[0]) + '; ' + str(i[1]) + '\n')


def read_nrrd(file):
    data, header = nrrd.read(file)

    return data


def analyze(nrrd_id, nrrd_gen):
    results = []

    # Iterate through every array position
    for i in range(len(nrrd_id)):
        for j in range(len(nrrd_id[i])):
            for k in range(len(nrrd_id[i][j])):
                # Values of 0 (background label) are not of interest
                if nrrd_id[i][j][k] != 0:
                    # If we find a id/gen combination we do not know yet -> add to result list
                    # Sometimes a node with a lower gen for the same id slips in (due to implicit node/edge conversion)
                    # if it got into our list: We remove it, if we already have an entry with a higher gen, ignore it
                    if [nrrd_id[i][j][k], nrrd_gen[i][j][k]] not in results \
                            and [nrrd_id[i][j][k], int(nrrd_gen[i][j][k]) + 1] not in results:
                        results.append([nrrd_id[i][j][k], nrrd_gen[i][j][k]])
                    if [nrrd_id[i][j][k], int(nrrd_gen[i][j][k] - 1)] in results:
                        results.remove([nrrd_id[i][j][k], int(nrrd_gen[i][j][k]) - 1])

    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create mapping from id to generation')
    parser.add_argument('-i', '--id', action='store', type=str, required=True,
                        help='.nrrd file containing ids')
    parser.add_argument('-g', '--gen', action='store', type=str, required=True,
                        help='.nrrd file containing generations')
    parser.add_argument('-f', '--filename', action='store', type=str, required=True, help='Name of output file')

    args = parser.parse_args()

    nrrd_id_file_path = args.id
    nrrd_gen_file_path = args.gen
    output_filename = args.filename

    nrrd_id_file = read_nrrd(nrrd_id_file_path)
    nrrd_gen_file = read_nrrd(nrrd_gen_file_path)

    analysis = analyze(nrrd_id_file, nrrd_gen_file)

    write_csv(analysis, output_filename)
