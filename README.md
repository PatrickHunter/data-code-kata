# Data Engineering Coding Challenge
This is my (Patrick Hunter's) solution to the coding challenge

## Requirments

Just Python 2 and this git repo.  No external packages needed.

## Usage
```
$python RunMe.py
```

This will create a file named 'DummyFixedWidthFile' and 
populate it with randomly generated data in the fixed
width format provided with the challenge.  Then parse it
and create DummyCSVFile.csv with the same data.

### File structure
The top level folder contains all of the code used for the
assignment proper, 'tests' contains the PyUnit testing 
code and various data files used input by the tests.
Within the top level folder: CreateDummyFixedWidthFile 
contains code for creating fixed width files with dummy data,
ParseFixedWidthFileToCSV.py contains code for parseing fixed
width files to CSV, and RunMe.py is a wrapper that calls the
primary functions of the previous files.  The remaining files
are used for testing.

## Testing
```
$python TestParseFixedWidthFileToCSV.py
```
Will run the PyUnit tests.
