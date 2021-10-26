#!/usr/bin/env python3

'''
Scrape crime data from GBI site and make it more useful for analysis.
Author: Benjamin J. Chapman
Email: bchapman8@gsu.edu
Organization: Legal Analytics & Innovation Initiative Georgia State University College of Law
Date: Tuesday, October 26, 2021
Version: 0.03
License: CC-by-SA 4.0
'''

from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv
import re
import sys
import argparse

DEBUG = False
URL = 'https://services.georgia.gov/gbi/crimestats/pages/crimeStatsForm.xhtml'
MONTHS = ['January', 'February', 'March',
          'April','May','June',
          'July','August','September',
          'October','November','December']

HEADER = ['Date', 'County', 'Murder', 'Rape', 'Robbery', 'Assault', 'Burglary', 'Larceny', 'Vehicle Theft']

def get_lines(url, year):
    params = {'reportsForm' : 'reportsForm',
                'reportsForm:months' : 'ALL',
                'reportsForm:counties' : 'ALL',
                'javax.faces.ViewState' : 'stateless',
                'reportsForm:j_idt76' : 'reportsForm:j_idt76'
                }
    params['reportsForm:year'] = year
    
    session = HTMLSession()
    response = session.post(url, params = params)
    soup = BeautifulSoup(response.html.html, 'html.parser')
    # Shrink down from 8MB of HTML to text
    text = soup.get_text()
    # Get rid of a bunch of extra newlines
    text = re.sub(r'\n+',r'\n',text)
    lines = text.split('\n')
    return lines

def get_title(lines):
    for line in lines:
        if line.startswith('Results for All Months'):
            if DEBUG:
                print('Title:', line)
            return line


def get_month_sections(lines):
    month_index = {}
    for month in MONTHS:
        for index, line in enumerate(lines):
            if line.startswith(month):
                month_index[month] = index
            if DEBUG: print(month_index)
    return month_index

def get_data_end(lines):
    for index, line in enumerate(lines):
        if line.startswith('Search Again'):
            return index

def load_months(lines, month_index):
    # Not elegant at all
    # Suggestions welcomed
    jan_data = lines[month_index['January']:month_index['February']]
    feb_data = lines[month_index['February']:month_index['March']]
    mar_data = lines[month_index['March']:month_index['April']]
    apr_data = lines[month_index['April']:month_index['May']]
    may_data = lines[month_index['May']:month_index['June']]
    jun_data = lines[month_index['June']:month_index['July']]
    jul_data = lines[month_index['July']:month_index['August']]
    aug_data = lines[month_index['August']:month_index['September']]
    sep_data = lines[month_index['September']:month_index['October']]
    oct_data = lines[month_index['October']:month_index['November']]
    nov_data = lines[month_index['November']:month_index['December']]
    dec_data = lines[month_index['December']:get_data_end(lines)]

    return (jan_data, feb_data, mar_data, 
            apr_data, may_data, jun_data, jul_data, aug_data,
            sep_data, oct_data, nov_data, dec_data)


def get_month_data(month_data):
    # Exclude header and total lines
    # Notice the interesting thing below; step by 8
    month = month_data[0]
    data = month_data[9:-8]
    data_rows = []
    for row in range(0,len(data),8):
        new_row = [month] + data[row:row+8]
        data_rows.append(new_row)
    return data_rows

def write_file(output_csv, title, header, data_rows):
    with open(output_csv,'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in data_rows:
            writer.writerow(row)

def process_year(year):            
    lines = get_lines(URL, str(year))
    if DEBUG: print('total lines for %s: %s' % (year,len(lines)))
    title = get_title(lines)
    month_index = get_month_sections(lines)
    months = load_months(lines, month_index)
    data_rows = []
    for m in months:
        data_rows += get_month_data(m)
    output_csv = title + '-gbi_data.csv'
    write_file(output_csv, title, HEADER, data_rows)
    print('Wrote %s.' % output_csv)

if __name__ == "__main__":
    # Default range is 2014-2017 (inclusive)
    parser = argparse.ArgumentParser(description='Create nicely-formatted CSV files by year of crime data from the GBI')
    parser.add_argument('-s', '--start', help='start year to be included in output (min = 1980)', type=int, default = 2014)
    parser.add_argument('-e', '--end', help='end year to be included in output (max = 2017)', type=int, default = 2017)
    args = parser.parse_args()
    if args.start < 1980: args.start = 1980
    for year in range(args.start,args.end+1):
        process_year(year)
