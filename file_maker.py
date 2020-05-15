import pandas as pd 
import random

column_names = ["Timestamp", "TrackingNum", "StockSymbol", "MessageType", "OrderNum", "ShareNum", "BuySell", "Price"]
df = pd.DataFrame(columns=column_names)

df["Timestamp"] = range(1,1000001)
df["TrackingNum"] = range(1234560, 2234560)
df["StockSymbol"] = random.choices(["AAPL", "GOOGL", "TSLA"], k=1000000)
df["MessageType"] = random.choices(["A", "X", "Y"], k=1000000)
df["OrderNum"] = range(2234560, 3234560)
df["ShareNum"] = random.choices(range(10, 1001), k=1000000)
df["BuySell"] = random.choices(["B", "S"], k=1000000)
df["Price"] = random.choices(range(23, 1345), k=1000000)

df.to_csv("sample_HFT.csv", header=True, index=False)

