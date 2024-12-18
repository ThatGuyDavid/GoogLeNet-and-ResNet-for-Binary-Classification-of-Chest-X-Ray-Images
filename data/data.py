import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_data():
    api = KaggleApi()
    api.authenticate()

    dataset = "paultimothymooney/chest-xray-pneumonia"
    output_dir = "data/"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    print(f"Downloading dataset: {dataset}")
    api.dataset_download_files(dataset, path=output_dir, unzip=True)
    print(f"Dataset downloaded and extracted to: {output_dir}")

if __name__ == "__main__":
    download_data()