import pandas as pd

df = pd.read_csv("nasdaq-1971Feb-2021Jan.csv")

list1 = df["Close"].to_list()
list1.pop()
list1.insert(0, list1[0])

print(list1)
