import pandas as pd

df = pd.read_csv("long-trend/data/nasdaq-1971Feb-2021Jan.csv")

list1 = df["Close"].to_list()
list1.pop()
list1.insert(0, list1[0])

lista = [1, 2, 3, 4, 5]
lista.pop(0)
print(lista)

min_val = 99990
min_index = 0

for i in range(7000, len(list1)):
    if list1[i] < min_val:
        min_val = list1[i]
        min_index = i

print(min_index)
