"""
This script aims to put together all the major evidende that will tell us that
the market is, indeed,  about to experience a .com bubble scenario
"""
import pandas as pd
import csv

from matplotlib import pyplot as plt
import matplotlib as matp
from matplotlib import gridspec

import statistics as stat

data_files = {
    "nasdaq_data": "data/nasdaq-1971Feb-2021Jan.csv",
    "daily_change": "data/daily-change-1971Feb-2021Jan.csv",
    "monthly_volume": "data/results/monthly_volume.csv"
}


def vix(days=200):
    """
    This is my own volatility index based on the daily absolute change in the nasdaq
    Returns a list of the monthly vix for the nasdaq
    VIX = mean(day0**2 + ... + dayN**2)
    """
    day_changes = []
    month_list = []
    df = pd.read_csv(data_files["daily_change"])

    for index in range(len(df)):
        day_vol = abs(df["Change"][index])**1.5
        day_changes.append(day_vol)

        if index+1 == len(df):
            month_list.append(stat.mean(day_changes))
            break

        if df["Date"][index][0:7] != df["Date"][index+1][0:7]:
            month_list.append(stat.mean(day_changes))
            day_changes = []

    return month_list


def volume():

    df = pd.read_csv(data_files["nasdaq_data"])
    month_list = []
    day_volume = []

    for index in range(len(df)):
        day_volume.append(df["Volume"][index])

        if index+1 == len(df):
            month_list.append(stat.mean(day_volume))
            break

        if df["Date"][index][0:7] != df["Date"][index+1][0:7]:
            month_list.append(stat.mean(day_volume))
            day_volume = []

    return month_list


def main():

    # Get data
    close_prices = pd.read_csv(data_files["nasdaq_data"])["Close"]
    monthly_dates = pd.read_csv(data_files["monthly_volume"])["Date"]
    monthly_volume = volume()
    VIX = vix()

    gs = gridspec.GridSpec(3, 1, height_ratios=[1, 1, 1.5])

    # Create graphs
    fig = plt.figure()
    ax = fig.add_subplot(111, label="VIX")
    ax2 = fig.add_subplot(111, label="NASDAQ", frame_on=False)
    ax3 = fig.add_subplot(gs[2], label="Volume", frame_on=False)

    ax.fill(monthly_dates, VIX, color='b', label='VIX')
    ax.set_xticks(monthly_dates[::32])
    ax.set_xticklabels(monthly_dates[::32], rotation=45)
    ax.set_ylim([0, 7])
    ax.axes.get_yaxis().set_visible(False)

    ax2.plot(range(len(close_prices)), close_prices, color="k", label='NASDAQ')
    ax2.set_yscale('log')
    ax2.axes.get_xaxis().set_visible(False)
    ax2.set_yticks([100, 500, 1000, 2000, 5000, 8000, 13000, 16000])
    ax2.get_yaxis().set_major_formatter(matp.ticker.ScalarFormatter())

    ax3.plot(range(len(monthly_volume)),
             monthly_volume, color='c', label='Volume')
    ax3.set_yscale('log')
    ax3.yaxis.tick_right()
    ax3.axes.get_xaxis().set_visible(False)

    lines = []
    labels = []

    for ax in fig.axes:
        axLine, axLabel = ax.get_legend_handles_labels()
        lines.extend(axLine)
        labels.extend(axLabel)

    ax.legend(lines, labels, loc='upper left', fancybox=True)

    ax2.axvline(x=7351, c='r', ls='--', label='SELL .Com')
    ax2.axvline(x=7998, c='g', ls='--', label='BUY .Com')

    ax2.legend(loc='upper left')

    plt.show()


if __name__ == '__main__':
    main()
