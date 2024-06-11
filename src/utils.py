from pathlib import Path

import pandas
from config import DATA_DIR
from pandas import DataFrame


def save_dataset(data: DataFrame, path: Path| str = DATA_DIR / 'dataset.pickle'):
    with open(path, 'wb') as _:
        data.to_pickle(path, compression='infer')


def load_dataset(path: Path| str= DATA_DIR / 'dataset.pickle') -> DataFrame:
    with open(path, 'rb') as output:
        return pandas.read_pickle(output)