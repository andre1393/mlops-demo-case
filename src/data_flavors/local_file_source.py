import os
import pandas as pd


class LoadLocalFile:
    def __init__(self, format, path, **params):
        self.format = format
        self.path = path
        self.params = params

        self.data_formats = {
            'csv': pd.read_csv
        }

        self.read_format = self.data_formats[self.format]

    def load(self):
        files = []
        if os.path.isdir(self.path):
            for file in os.listdir(self.path):
                if file.endswith(f'.{self.format}'):
                    files.append(os.path.join(self.path, file))
        else:
            files.append(self.path)
        if not files:
            print(f'No file found. at {self.path}')
        for file in files:
            print(f'loading file: {file}')
            yield self.read_format(file, **self.params), {'name': os.path.basename(file)}
