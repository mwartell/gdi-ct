def read_data(path):
    """Reads comma separated data from path."""
    infile = open(path)
    infile.readline()   # discard headers
    for line in infile:
        line = line.strip()
        row = line.split(',')
        print(row)

read_data('ice-cream.csv')
