# Running the Code

clone the repository
```
git clone https://github.com/hassanaliaskari/CanvassCodeChallenge.git
```

## Challenge 1

```
python challenge1.py
```

## Challenge 2

```
python challenge2.py random_data.csv
```

Wait for the console to print "sorted".

The sorted data can be found in the file sorted_data.csv

# Implementation and Design Decisions

## Challenge 1

The implementation tries to minimize the number of times the program lands on a odd-digit number. It does so by jumping to the next suitable canditate determmined by which digit in the current number is odd.

A recursive algorithm to generate the even-digit numbers was considered but since the data was small, a simpler implementation of comparable efficiency was chosen.

## Challenge2

The implementation does not require the whole data to be loaded in memory. So, it can handle data files of any size.

A merge sort approach was taken because the data needed to be broken down into chunks that can be loaded in memory. The intermediate files are stored in a separate folder for keep things clean in case of runtime errors. The filename is read from the console for ease of testing.
