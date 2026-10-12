import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"   #윈도우는Malgun Gothic
prices = [2960, 2970, 2785, 2935, 2995]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)
for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
        xytext=(0, 8), ha="center")
ax.set_title("더즌의 일별 종가 변화")
fig.savefig("my_first_chart.png")

