## Notes on GBI Crime Data data files for 1980-2017

This is a collection of the crime data files from 1980 to 2017, inclusive. 

## Individual Results Files and line counts

Each file has a single header line that looks like this:

```Date,County,Murder,Rape,Robbery,Assault,Burglary,Larceny,Vehicle Theft```

Dates are provided in Month Year format.

Files are listed below, preceded by a line count for each file.

```
    1908 Results for All Months, 1980, All Counties-gbi_data.csv
    1909 Results for All Months, 1981, All Counties-gbi_data.csv
    1909 Results for All Months, 1982, All Counties-gbi_data.csv
    1909 Results for All Months, 1983, All Counties-gbi_data.csv
    1909 Results for All Months, 1984, All Counties-gbi_data.csv
    1909 Results for All Months, 1985, All Counties-gbi_data.csv
    1909 Results for All Months, 1986, All Counties-gbi_data.csv
    1909 Results for All Months, 1987, All Counties-gbi_data.csv
    1909 Results for All Months, 1988, All Counties-gbi_data.csv
    1909 Results for All Months, 1989, All Counties-gbi_data.csv
    1909 Results for All Months, 1990, All Counties-gbi_data.csv
    1909 Results for All Months, 1991, All Counties-gbi_data.csv
    1909 Results for All Months, 1992, All Counties-gbi_data.csv
    1909 Results for All Months, 1993, All Counties-gbi_data.csv
    1909 Results for All Months, 1994, All Counties-gbi_data.csv
    1909 Results for All Months, 1995, All Counties-gbi_data.csv
    1909 Results for All Months, 1996, All Counties-gbi_data.csv
    1909 Results for All Months, 1997, All Counties-gbi_data.csv
    1909 Results for All Months, 1998, All Counties-gbi_data.csv
    1909 Results for All Months, 1999, All Counties-gbi_data.csv
    1898 Results for All Months, 2000, All Counties-gbi_data.csv
    1909 Results for All Months, 2001, All Counties-gbi_data.csv
    1909 Results for All Months, 2002, All Counties-gbi_data.csv
    1909 Results for All Months, 2003, All Counties-gbi_data.csv
    1909 Results for All Months, 2004, All Counties-gbi_data.csv
    1909 Results for All Months, 2005, All Counties-gbi_data.csv
    1909 Results for All Months, 2006, All Counties-gbi_data.csv
    1903 Results for All Months, 2007, All Counties-gbi_data.csv
    1874 Results for All Months, 2008, All Counties-gbi_data.csv
    1849 Results for All Months, 2009, All Counties-gbi_data.csv
    1852 Results for All Months, 2010, All Counties-gbi_data.csv
    1872 Results for All Months, 2011, All Counties-gbi_data.csv
    1899 Results for All Months, 2012, All Counties-gbi_data.csv
    1863 Results for All Months, 2013, All Counties-gbi_data.csv
    1859 Results for All Months, 2014, All Counties-gbi_data.csv
    1872 Results for All Months, 2015, All Counties-gbi_data.csv
    1892 Results for All Months, 2016, All Counties-gbi_data.csv
    1885 Results for All Months, 2017, All Counties-gbi_data.csv
   72151 total
```

### Combined results and line count

Individual files were combined with the `combine_results.py` utility. Results were saved to `all_results.csv`. The file is 72,114 lines long.

### Checksums

These are the md5 checksums for the various results files. To verify the checksums, use the `md5` command on the Mac or follow [this guidance](https://infosecscout.com/md5-checksum-on-windows/) to use PowerShell to check the MD5 checksum on Windows.

```MD5 (Results for All Months, 1980, All Counties-gbi_data.csv) = 0c722a20e32c4e9a43f34b4a7ab8c5c1
MD5 (Results for All Months, 1981, All Counties-gbi_data.csv) = 3ce05dacf24e58f77a68a8d1c7b1c71f
MD5 (Results for All Months, 1982, All Counties-gbi_data.csv) = 1c06190153db099bf3c7cbeb60bfe266
MD5 (Results for All Months, 1983, All Counties-gbi_data.csv) = bb13aed36bf85ee98e6a4d6503fd8568
MD5 (Results for All Months, 1984, All Counties-gbi_data.csv) = 02b3083facb30fadfb1b93bcfe00fe89
MD5 (Results for All Months, 1985, All Counties-gbi_data.csv) = dabcadf665ab80961429a997d13f4fce
MD5 (Results for All Months, 1986, All Counties-gbi_data.csv) = d14f7c5057014d94e1fbf9c421c503e5
MD5 (Results for All Months, 1987, All Counties-gbi_data.csv) = 4860938919a233af83dbc745b7440b24
MD5 (Results for All Months, 1988, All Counties-gbi_data.csv) = 9be9e370832573c80d9da7fea01e2938
MD5 (Results for All Months, 1989, All Counties-gbi_data.csv) = 40c502f2709e05a463bb26330f20fdbc
MD5 (Results for All Months, 1990, All Counties-gbi_data.csv) = f27adb38c0b165c6aedd58438ac7fcb5
MD5 (Results for All Months, 1991, All Counties-gbi_data.csv) = 6143fee40f2750a2bd69ba2a6b8d1f15
MD5 (Results for All Months, 1992, All Counties-gbi_data.csv) = 88b5ed6d4589970d43bbe534664de3ea
MD5 (Results for All Months, 1993, All Counties-gbi_data.csv) = 5fb68d7d0a041515ba7163522ee7cd77
MD5 (Results for All Months, 1994, All Counties-gbi_data.csv) = 462ddfdea0a6be374123123958b083a3
MD5 (Results for All Months, 1995, All Counties-gbi_data.csv) = dda98f0cfca96815bacc49c3f242fd38
MD5 (Results for All Months, 1996, All Counties-gbi_data.csv) = bd8f6e4db40a1f50901ac418619c9eb9
MD5 (Results for All Months, 1997, All Counties-gbi_data.csv) = 2053b83a990514e79d5b2f38df02517b
MD5 (Results for All Months, 1998, All Counties-gbi_data.csv) = 65221499309dae644dadfaa9d66b76f7
MD5 (Results for All Months, 1999, All Counties-gbi_data.csv) = b55a2b989642da143f78553414f628bb
MD5 (Results for All Months, 2000, All Counties-gbi_data.csv) = b6dd471cc3482d38da5d3f965ebb46d4
MD5 (Results for All Months, 2001, All Counties-gbi_data.csv) = 2a6ab4db6b2d61c886fafbd42484e648
MD5 (Results for All Months, 2002, All Counties-gbi_data.csv) = 439ffadcd89d9f685c33226b96fb82e4
MD5 (Results for All Months, 2003, All Counties-gbi_data.csv) = 2cd24eb4738018d32873a992cec54661
MD5 (Results for All Months, 2004, All Counties-gbi_data.csv) = 5dc44a3014b1d9e7c3d307f3207166cd
MD5 (Results for All Months, 2005, All Counties-gbi_data.csv) = 82a07eec638c75a9b9e009b73f7d8f80
MD5 (Results for All Months, 2006, All Counties-gbi_data.csv) = 9fb8964899e1089b8e935ff221438e3d
MD5 (Results for All Months, 2007, All Counties-gbi_data.csv) = c57d2d96979f0c82d9c6af4114d2a9b3
MD5 (Results for All Months, 2008, All Counties-gbi_data.csv) = 2f64c15ece0649aac445f526d4bd83eb
MD5 (Results for All Months, 2009, All Counties-gbi_data.csv) = 34083b1d1e154aef5a06a7567fccc8c4
MD5 (Results for All Months, 2010, All Counties-gbi_data.csv) = f18041ef2207a39c3df0a91d985472f5
MD5 (Results for All Months, 2011, All Counties-gbi_data.csv) = df329d37f78b61cc4e5ca4698c6eab9b
MD5 (Results for All Months, 2012, All Counties-gbi_data.csv) = c087512307be3bcbb04196eed9191e54
MD5 (Results for All Months, 2013, All Counties-gbi_data.csv) = 6da94d0994c0f99317b2ac7f1614b162
MD5 (Results for All Months, 2014, All Counties-gbi_data.csv) = 6d7453936a231383a93c9dfe0383e7fd
MD5 (Results for All Months, 2015, All Counties-gbi_data.csv) = 826f66cb790e461d1c13a13edf4c5c4b
MD5 (Results for All Months, 2016, All Counties-gbi_data.csv) = d7626926ca5d9d9c35dfe704766df940
MD5 (Results for All Months, 2017, All Counties-gbi_data.csv) = 3ac8c7d181d7b6d237d51d2ca71cf66d
MD5 (all_results.csv) = ee4e21e1e39b7c79643b3900b412443c
```

