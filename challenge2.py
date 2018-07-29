import pandas as pd
import os
import sys
import shutil


# Fucntion to compare two data rows for sorting
# Returns True if row1 should appear earlier, else returns False
def isLess(row1, row2):
    if not row2:
        return True
    if not row1:
        return False

    id1 = row1[1]
    id2 = row2[1]
    date1 = row1[6]
    date2 = row2[6]

    if id1 < id2:
        return True
    elif id1 == id2:
        if date1 and date2 and date1 < date2:
            return True
    else:
        return False


# Merge-sort two sorted files into filename1, deletes filename2
def merge_files(filename1, filename2):
    with open(filename1) as file1, open(filename2) as file2, open('temp_file.csv', 'w') as output_file:
        header1, header2 = next(file1), next(file2)
        output_file.write(header1)

        line1, line2 = next(file1), next(file2)
        while line1 or line2:
            row1 = line1.split(',') if line1 else None
            row2 = line2.split(',') if line2 else None

            if isLess(row1, row2):
                output_file.write(line1)
                line1 = next(file1, None)
            else:
               output_file.write(line2)
               line2 = next(file2, None)

    os.remove(filename1)
    os.remove(filename2)
    os.rename('temp_file.csv', filename1)


def lookup(s):
    dates = {date:pd.to_datetime(date) for date in s.unique()}
    return s.map(dates)


# Breaks up a data file into chunks, sorts them and saves the files in dirname
def sort_by_chunk(data_filename, chunksize, dirname):
    idx = 0
    os.mkdir(dirname)
    filenames = []
    for chunk in pd.read_csv(data_filename, chunksize=chunksize):
        chunk['Date'] = lookup(chunk['Date'])
        sorted_chunk = chunk.sort_values(by=['Device_ID', 'Date'])
        filename = dirname + '/temp_data%d.csv' % idx
        sorted_chunk.to_csv(filename)
        filenames.append(filename)
        idx += 1

    return filenames

data_filename = sys.argv[1]
dirname = './temp'
if os.path.isdir(dirname):
    shutil.rmtree(dirname)

filenames = sort_by_chunk(data_filename, 100000, dirname)
for file in filenames[1:]:
    merge_files(filenames[0], file)

os.rename(filenames[0], './sorted_data.csv')
shutil.rmtree(dirname)
print("Sorted")

