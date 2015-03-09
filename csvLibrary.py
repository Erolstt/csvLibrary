__author__ = 'erol.selitektay'
import csv
class csvLibrary(object):

    def read_csv_file(self, filename):
        '''
        Reads data from given csv file.

        Example: 

        ${data} Read Csv File  "path-to-csvfile"

        You can get the data such as ${data[rowNumber][ColumnNumber]}
        
        Starting point is [0][0]
        '''
        data = []
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data
        csvfile.close()