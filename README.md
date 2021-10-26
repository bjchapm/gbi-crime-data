## Data retrieval for Georgia Bureau of Investigation Crime Statistics

The GBI has a [GBI Crime Statistics
Database](https://gbi.georgia.gov/services/crime-statistics/gbi-crime-statistics-database)
page that describes the Georgia Uniform Crime Reporting program. The
page has a link to a page called [Crime Statistics
Search](https://services.georgia.gov/gbi/crimestats/). That page
links to the [Crime Statistics
Report](https://services.georgia.gov/gbi/crimestats/pages/reports.xhtml)
page.

This is the page that we are interested in. It allows researchers
to retrieve county by county crime statistics by year for seven
major crimes:

* Murder
* Rape
* Robbery
* Assault
* Burglary
* Larceny
* Vehicle Theft

I wrote this Python script to help automate the process of retrieving this
data. Please contact me if you have questions or comments about it.

Files are saved as CSV files by year of report in the same folder as the script. By default, it will
retrieve the data for 2015, 2016, and 2017. Dates can be submitted on the command line with `--start XXXX` and
`--end YYYY`. Use `--help` to get help. Output CSV files will be auto-named with the report title.

When the script is launched, you should see:

```
Wrote Results for All Months, 2015, All Counties-gbi_data.csv.
Wrote Results for All Months, 2016, All Counties-gbi_data.csv.
Wrote Results for All Months, 2017, All Counties-gbi_data.csv.
```

as it processes and writes the CSV files for the data.

As of October, 2021, there is GBI data for 1980
through 2017.

## Notes

This produces one file per each year of data. If you need the files concatenated into one file, let me know and I'll
add that as an option. You can also do it on the commandline in Linux or using a Mac with something like: 

```cat Results* > bigfile.txt```

This will leave you with extra headers. An easy way to get rid of them is to search for lines beginning with 'Date' and
delete them. 

Ben Chapman

Georgia State University College of Law

Legal Analytics & Innovation Initiative

