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


def write_html(counts):
    flavors = {'p': 'pistachio', 's': 'strawberry'}
    heading = """
    <!DOCTYPE html>
    <html><head><title>Ice Cream Preferences</title></head><body>
    <table border="1">
    <tr> <th>preference</th> <th>female</th> <th>male</th> </tr>""".lstrip()
    table_row = '<tr> <td>{}</td> <td>{}</td> <td>{}</td> </tr>'

    print(heading)
    for f, flavor in flavors.items():
        print(table_row.format(flavor, counts['f'][f], counts['m'][f]))
    print('</table></body></html>')

counts = ice_cream_counts('ice-cream.csv')
write_html(counts)
