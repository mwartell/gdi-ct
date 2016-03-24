"""The simplest data reader."""

for line in open('ice-cream.csv'):
    row = line.split(',')
    print(row)
