#!/usr/bin/env python3

import pandas as pd
input_df = f"/workspace/aoc2021/day2/input_day2.txt"
df = pd.read_csv(input_df, sep=" ", header=None, names=["movement", "value"])
#print(df.head())
total_moves = df['value'].groupby(df['movement'])
print(total_moves.sum())
print((2063-973)*1868)