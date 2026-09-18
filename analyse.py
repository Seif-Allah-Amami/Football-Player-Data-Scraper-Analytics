import pandas as pd
import matplotlib.pyplot as plt         


data=pd.read_csv("ballon_dor_2025_26_clean.csv")
print(data.head().reset_index(drop=True))
print("-------------------------------------------------")


top_goals=data.sort_values(by="goals",ascending=False).reset_index(drop=True)

print( top_goals[[
    "player",
    "goals",
    "assists",
    "matches"
]].head(10))
print("----------------------------------------------")
data["total_contributions"]= data["goals"]+ data["assists"]

top_contributions = data.sort_values(

    by="total_contributions",
    ascending=False
).reset_index(drop=True)
print(top_contributions[[
    "player",
    "goals",
    "assists",
    "total_contributions",
    "matches"
]].head(10))
print("----------------------------------------------------------")
top_players=data.sort_values(
    by="goals",
    ascending=False

).head(10)
plt.figure(figsize=(12,6))
plt.bar(
    top_players["player"],
    top_players["goals"]
)   

plt.title("Top 10 Players by Goals -25/26 ")
plt.xlabel("Player")
plt.ylabel("Goals")
plt.xticks(rotation=45,ha="right")

plt.tight_layout()
plt.show()
#know we are going tp compare goals and asists

plt.figure(figsize=(10,6))

plt.scatter(
    data["goals"],
    data["assists"],
    s=80,
    alpha=0.8
)
for _, row in data.iterrows():
    plt.annotate(
        row["player"],
        (row["goals"], row["assists"]),
        xytext=(6, 6),
        textcoords="offset points",
        fontsize=9
    )

plt.title("Goals VS Assists- 25/26",
    fontsize=16,
    fontweight="bold"
)


plt.xlabel("Goals")
plt.ylabel("Assists")

plt.grid(True, 
    linestyle="--",
    alpha=0.4)
plt.tight_layout()
plt.show()
print("-------------------------------------------------------------------")
data["goal_contributions_per_match"] = (data["goals"] + data["assists"]) / data["matches"]

ranking = data.sort_values(
    by="goal_contributions_per_match",
    ascending=False
)

print(ranking[[
    "player",
    "goals",
    "assists",
    "goal_contributions_per_match",
    "matches"
]].head(10))
print("---------------------------------------------------------")
top_efficiency = data.sort_values(
    by="goal_contributions_per_match",
    ascending=False
).head(10)

plt.figure(figsize=(12, 6))

plt.bar(
    top_efficiency["player"],
    top_efficiency["goal_contributions_per_match"]
)

plt.title("Top 10 Players by Goal Contributions per Match")
plt.xlabel("Player")
plt.ylabel("Contributions per Match")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()