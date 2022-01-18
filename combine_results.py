#!/usr/bin/env python3
'''
Combined retrieved files into one ginormous csv file. You'll need to edit the file to change names, etc.'
Author: Benjamin J. Chapman
Email: bchapman8@gsu.edu
Organization: Legal Analytics & Innovation Initiative Georgia State University College of Law
Date: Tuesday, October 26, 2021
Version: 0.03
License: CC-by-SA 4.0
'''

import csv
import glob

year_files = glob.glob('Results*csv')
combined_file = 'all_results.csv'
field_names = ['Date', 'County', 'Murder', 'Rape', 'Robbery', 'Assault', 'Burglary', 'Larceny', 'Vehicle Theft']
all_data = []

for file in year_files:
    with open(file,'r') as f:
        csv_file = csv.DictReader(f)
        for line in csv_file:
            all_data.append(line)
        print(f'Processed {file}.')

with open(combined_file, 'w') as f:
    csv_file = csv.DictWriter(f, fieldnames=field_names)
    csv_file.writeheader()
    for row in all_data:
        csv_file.writerow(row)

print(f'Wrote {combined_file}. Done.')

