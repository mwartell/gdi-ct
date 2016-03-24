import csv

def read_data(path):
    """Reads comma separated data from path."""
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assert row['gender'] in 'mf'
            assert row['preference'] in 'ps'
            print(row['gender'], row['preference'])

read_data('ice-cream.csv')
