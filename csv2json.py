import csv
import json
from sys import argv

csvfile = open(argv[1], 'r') # Takes path to csv as first cli arg
jsonfile = open(argv[2], 'w') # Takes path to json as second cli arg

fieldnames = # Enter the column values of the csv here

reader = csv.DictReader( csvfile, fieldnames)
firstline = True
for row in reader:
	if firstline: 			# Skips first line of csv containing column names
		firstline = False
		continue
	json.dump(row, jsonfile)
	jsonfile.write('\n')


