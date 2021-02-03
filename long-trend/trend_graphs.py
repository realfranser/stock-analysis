"""
Graph and analyse the fluctuation of volume and stock volatility comparing
years before .com bubble and years prior to 2021
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_paths = {
        "daily_change": "daily-change-1971Feb-2021Jan.csv",
        "daily_data": "nasdaq-1971Feb-2021Jan.csv"
        }

ax1 = plt.subplot(111)

def daily_change_graph():
    global ax1
    data = np.genfromtxt(file_paths["daily_change"], delimiter=",", names=["x", "y"])
    ax1.plot(range(len(data['x'])), [abs(elem) for elem in data['y']])

def daily_price_graph():
    global ax1
    df = pd.read_csv(file_paths["daily_data"])
    ax2 = ax1.twinx()
    ax2.plot(range(len(df['Close'])), df['Close'], color='r')
    ax2.set_yscale('log')
    plt.show()

def main():
    daily_change_graph()
    daily_price_graph()
    

if __name__ == "__main__":
    main()
