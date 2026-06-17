import matplotlib.pyplot as plt
from load_csv import load


def main():
    df = load("life_expectancy_years.csv")
    if not df:
        return

    df_france = df[df["country"] == "France"]

    values = df_france.iloc[0, 1:].astype(float).values
    years = df.columns[1:].astype(int)
    plt.plot(years, values)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title('Population Projections')
    plt.show()


if __name__ == "__main__":
    main()
