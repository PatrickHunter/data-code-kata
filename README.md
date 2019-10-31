# Data Engineering Coding Challenge
<<<<<<< HEAD
This is my (Patrick Hunter's) solution to the coding challenge.
=======
This is my (Patrick Hunter's) solution to the coding challenge
>>>>>>> 34a2f326f6805a29e3445c7a43d008b5d4b45d38

## Requirments

Just Python 3 and this git repo.  No external packages needed.

## Usage
<<<<<<< HEAD
$python RunMe.py
=======
$python3 RunMe.py
>>>>>>> 34a2f326f6805a29e3445c7a43d008b5d4b45d38

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
<<<<<<< HEAD
$python TestParseFixedWidthToCSV.py
=======
$TestParseFixedWidthToCSV.py
>>>>>>> 34a2f326f6805a29e3445c7a43d008b5d4b45d38

Will run the PyUnit tests.