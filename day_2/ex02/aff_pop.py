import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
from load_csv import load


def convert_pop(x):
    if x.endswith("B"):
        return float(x[:-1]) * 1000
    if x.endswith("M"):
        return float(x[:-1])
    if x.endswith("k"):
        return float(x[:-1]) / 1000
    return float(x)

def main():
    df = load("population_total.csv")

    if df is None:
        return

    years = df.columns[1:].astype(int)
    mask = years <= 2050
    years = years[mask].tolist()

    df_france = df[df["country"] == "France"]
    df_belgium = df[df["country"] == "Belgium"]

    fr = (
        df_france.iloc[0, 1:][mask]
        .apply(convert_pop)
        .tolist()
    )

    bg = (
        df_belgium.iloc[0, 1:][mask]
        .apply(convert_pop)
        .tolist()
    )

    plt.plot(years, fr)
    plt.plot(years, bg)
    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(lambda x, pos: f"{int(x)}M")
    )
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title('Population Projections')
    plt.show()


if __name__ == "__main__":
    main()
