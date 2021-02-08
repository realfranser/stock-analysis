"""
Graph and analyse the fluctuation of volume and stock volatility comparing
years before .com bubble and years prior to 2021
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_paths = {
    "daily_change": "data/daily-change-1971Feb-2021Jan.csv",
    "daily_data": "data/nasdaq-1971Feb-2021Jan.csv"
}


def daily_change_graph():
    data = np.genfromtxt(
        file_paths["daily_change"], delimiter=",", names=["x", "y"])

    return [abs(elem) for elem in data['y']]


def daily_price_graph():
    df = pd.read_csv(file_paths["daily_data"])

    return df['Close']


def monthly_absolute_change_count(change):
    """
    Returns the number of days in a month that the index has make a daily value change above change input
    in absolute numbers
    """
    df_in = pd.read_csv(file_paths["daily_change"])
    df_out = {}  # month-year: number of days

    monthly_count = 0

    for i in range(len(df_in["Change"])):
        if abs(df_in["Change"][i]) > change:
            monthly_count += 1

        if i != len(df_in["Date"])-1 and df_in["Date"][i][0:7] != df_in["Date"][i+1][0:7]:
            df_out[df_in["Date"][i][2:7]] = monthly_count
            monthly_count = 0

    return df_out


def main():
    daily_change = daily_change_graph()
    close_prices = daily_price_graph()
    #change_dict = monthly_absolute_change_count(2)

    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)

    #ax.bar(change_dict.keys(), change_dict.values(), color="b")
    # ax.set_xticks(ax.get_xticks()[::64])
    ax.bar(range(len(daily_change)), daily_change, color="b")

    ax2.plot(range(len(close_prices)), close_prices, color="r")
    ax2.axis('off')

    plt.show()


if __name__ == "__main__":
    main()
