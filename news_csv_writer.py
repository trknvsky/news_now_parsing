import csv


class CSVFile:
    WRITE = 'w'
    DELIMITER = ','
    HEADERS = ['title', 'url', 'news maker']

    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, self.WRITE, newline='') as file:
            writer = csv.DictWriter(file, delimiter=self.DELIMITER, fieldnames=self.HEADERS)
            writer.writeheader()
            writer.writerows(data)
            file.close()
