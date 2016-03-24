import csv
from collections import defaultdict

def ice_cream_counts(path):
    """Returns gender/preference counts from csv in path."""
    counts = {'m': defaultdict(int), 'f': defaultdict(int)}

    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            counts[row['gender']][row['preference']] += 1

    return counts

counts = ice_cream_counts('ice-cream.csv')
print(counts)
