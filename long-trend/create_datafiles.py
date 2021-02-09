"""
This file creates the required datafiles given the main datafile with the
raw stock information
"""

import csv
import pandas as pd

file_paths = {
    "daily_change": "data/daily-change-1971Feb-2021Jan.csv",
    "daily_data": "data/nasdaq-1971Feb-2021Jan.csv",
    "monthly_absolute_change": "data/results/monthly_absolute_change_2per.csv"
}


def daily_change():
    """
    Extracts daily info from nasdaq datafile and creates a new datafile with
    daily info with the following columns date, change, volume 
    """
    columns = ["Date",
               # "Open","High","Low","Close","Volume",
               "Change"]
    # Read from csv file
    in_df = pd.read_csv(file_paths["daily_data"])

    # Get daily change
    change_list = []

    list1 = in_df["Close"].to_list()
    list1.pop()
    list1.insert(0, list1[0])

    zip_object = zip(list1,
                     in_df["Close"].to_list())

    for close1, close2 in zip_object:
        change_list.append((close1-close2)*100/close1)

    out_df = pd.DataFrame({'Date': in_df["Date"],
                           'Change': change_list})

    # Write out CSV files
    out_df.to_csv(path_or_buf=file_paths["daily_change"],
                  columns=columns,
                  header=False,
                  index=False)


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

    with open(file_paths["monthly_absolute_change"], 'w+', newline='') as f:
        w = csv.writer(f)
        w.writerows(df_out.items())


def volume_change():
    """
    Volume change (to be decided)
    """
    pass


def after_hours():
    """
    Gets change of after hours and pre-market
    """
    pass


def main():
    # daily_change()
    monthly_absolute_change_count(2)


if __name__ == "__main__":
    main()
