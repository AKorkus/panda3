import pandas as pd
import matplotlib.pyplot as pyplok
from plotly import graph_objects as go
import plotly as ply


prices = [
	(1, 2.12),
	(2, 2.56),
	(3, 3.10),
	(4, 3.16),
	(5, 3.58),
	(6, 5.12),
	(7, 5.16),
	(8, 5.20),
	(9, 4.12),
	(10, 4.10),
	(11, 3.65),
	(12, 4.25),

]

df = pd.DataFrame(prices, columns=["month", "price"], index="month")
df = df.set_index("month")
print(df)

dolares = df['price'].apply(lambda price: price/4)
df["priceUSD"] = dolares
print(df)

pyplok.title("Price of goods (USD)")
pyplok.plot(df.index, df["priceUSD"], "--", color = "red")
pyplok.plot(df.index, df["price"], "--", color = "blue")

#df["priceUSD"].plot(kind="line", color = "red")
