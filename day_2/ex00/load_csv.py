import pandas as pd
import os


def load(path: str) -> pd.:
    try:
        if not os.path.isfile(path):
            raise AssertionError("Invalid path, file does not exist.")
        if not path.lower().endswith(".csv"):
            raise AssertionError("Path extension is not .csv")
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None
