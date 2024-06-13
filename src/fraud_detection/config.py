from pathlib import Path

ROOT_DIR= Path(__file__).absolute().parent.parent.parent

SRC_DIR=ROOT_DIR / 'src'
DATA_DIR=ROOT_DIR / 'raw_data'

DATA_FILENAME_CSV='dataset.csv'
DATA_FILENAME_PICKLE='dataset.pickle'