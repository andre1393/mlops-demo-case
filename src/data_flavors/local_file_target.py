import os
from datetime import datetime

import pandas as pd


class SaveLocalFile:
    def __init__(self, format, path, predictions_column='predictions', **params):
        self.format = format
        self.path = path
        self.predictions_column = predictions_column
        self.params = params

        self.data_formats = {
            'csv': lambda df, *args, **kwargs: df.to_csv(*args, **kwargs)
        }

        self.save_method = self.data_formats[self.format]


    def save(self, df, predictions, metadata):
        df_save = df.copy()
        df_save[self.predictions_column] = predictions
        if 'name' not in metadata:
            raise ValueError('expected a name metadata')
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{metadata['name']}"
        print(f'saving predictions at: {os.path.join(self.path, filename)}')
        self.save_method(df_save, os.path.join(self.path, filename), **self.params)
