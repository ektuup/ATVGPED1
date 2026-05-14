import csv
with open("estatisticas_ordenacao.csv", 'r') as fcsv:
    scanner = csv.DictReader(fcsv)
    scanner
    