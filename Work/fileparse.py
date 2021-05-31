# fileparse.py
import csv
import report

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    if select and has_headers == False:
        raise RuntimeError("select argument requires column headers")
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        headers = next(rows) if has_headers else []

        # If specific columns have been selected, make indices for filtering
        if select:
            indices = [ headers.index(colname) for colname in select ]
            print(colname)
            headers = select

        records = []
        for rowno, row in enumerate(rows, 1):
            try:
                if not row:     # Skip rows with no data
                    continue

                # If specific column indices are selected, pick them out
                if select:
                    row = [ row[index] for index in indices]

                # Apply type conversion to the row
                if types:
                    row = [func(val) for func, val in zip(types, row)]

                # Make a dictionary or a tuple
                if headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print("Row {}: Couldn't convert {}".format(rowno, row))
                    print("Row {}: Reason {}".format(rowno, e))
                continue
        return records
