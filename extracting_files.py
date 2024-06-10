# extract_data.py
import tarfile
import gzip
import shutil
import os

def extract_files(tar_path, combined_path, extract_path):
    # Extract tar.gz file
    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=extract_path)

    # Extract combined.txt.gz file
    with gzip.open(combined_path, "rb") as f_in:
        with open(os.path.join(extract_path, "twitter_combined.txt"), "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

if __name__ == "__main__":
    tar_path = "/Users/rohan/Desktop/social-network-anomaly-detection/twitter.tar.gz"
    combined_path = "/Users/rohan/Desktop/social-network-anomaly-detection/twitter_combined.txt.gz"
    extract_path = "/Users/rohan/Desktop/social-network-anomaly-detection/extracted files"
    extract_files(tar_path, combined_path, extract_path)
