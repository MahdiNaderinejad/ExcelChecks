## How to use this code?

### Dependecnies
Add dependencies using these two commands in your cmd or terminal:

pip install pandas
pip install openpyxl

### Files
You should have two files of your values resulted from experiments and real values.
These files must be spreadsheets and sorted only in the first column with only one single row of header.

### Code
In the code, change the name(address) of the files and the header values coming from both files.
These modifications can be done through lines 6-9 in the excelchecks.py.

### Output
This code will add a column named "Exists" to the existing experiment file and if a given value of this file exists in real, it writes 1 in front of it and 0 otherwise.
