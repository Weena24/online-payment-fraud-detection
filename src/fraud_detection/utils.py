from pathlib import Path

import pandas
from pandas import DataFrame

from fraud_detection.config import DATA_DIR, DATA_FILENAME_PICKLE



def save_pickle_dataset(data: DataFrame, path: Path| str = DATA_DIR / DATA_FILENAME_PICKLE):
    with open(path, 'wb') as _:
        data.to_pickle(path, compression='infer')


def load_pickle_dataset(path: Path| str= DATA_DIR / DATA_FILENAME_PICKLE) -> DataFrame:
    with open(path, 'rb') as output:
        return pandas.read_pickle(output)