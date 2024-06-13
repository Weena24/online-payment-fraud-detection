
# Data sources
DATA_DIR=./raw_data
PICKLE_DATA_FILE_LINK=https://drive.google.com/uc?id=1_ChwkYI-ZgRNhWV3wXMGsuDzI0svNh_D
CSV_DATA_FILE_LINK=https://drive.google.com/uc?id=1TBeQP8g1iWx80SEJBBV9vrFE-XyNl6Zf

initialize_raw_data:
	@python -m gdown ${PICKLE_DATA_FILE_LINK} --output ${DATA_DIR}/dataset.pickle
	@python -m gdown ${CSV_DATA_FILE_LINK} --output ${DATA_DIR}/dataset.csv


# Package installation
reinstall_packages:
	@pip uninstall -y fraud_detection || :
	@pip install -e .

